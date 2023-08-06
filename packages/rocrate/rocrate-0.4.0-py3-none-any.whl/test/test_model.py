# Copyright 2019-2021 The University of Manchester, UK
# Copyright 2020-2021 Vlaams Instituut voor Biotechnologie (VIB), BE
# Copyright 2020-2021 Barcelona Supercomputing Center (BSC), ES
# Copyright 2020-2021 Center for Advanced Studies, Research and Development in Sardinia (CRS4), IT
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import uuid

import pytest
from rocrate.rocrate import ROCrate
from rocrate.model.file import File
from rocrate.model.computationalworkflow import ComputationalWorkflow
from rocrate.model.person import Person


RAW_REPO_URL = "https://raw.githubusercontent.com/ResearchObject/ro-crate-py"


def test_dereferencing(test_data_dir, helpers):
    crate = ROCrate(gen_preview=True)

    # verify default entities
    root_dataset = crate.dereference('./')
    assert crate.root_dataset is root_dataset
    metadata_entity = crate.dereference(helpers.METADATA_FILE_NAME)
    assert crate.metadata is metadata_entity
    preview_entity = crate.dereference(helpers.PREVIEW_FILE_NAME)
    assert preview_entity is crate.preview

    # dereference added files
    sample_file = test_data_dir / 'sample_file.txt'
    file_returned = crate.add_file(sample_file)
    assert isinstance(file_returned, File)
    dereference_file = crate.dereference("sample_file.txt")
    assert file_returned is dereference_file
    readme_url = f'{RAW_REPO_URL}/master/README.md'
    readme_entity = crate.add_file(readme_url)
    assert crate.dereference(readme_url) is readme_entity


@pytest.mark.parametrize("name", [".foo", "foo.", ".foo/", "foo./"])
def test_dereferencing_equivalent_id(test_data_dir, name):
    test_ids = [name, f'./{name}', f'.//{name}', f'./a/../{name}']
    path = test_data_dir / name
    if name.endswith("/"):
        path.mkdir()
        test_ids.extend([f"{name}/", f"{name}//"])
    else:
        path.touch()
    for id_ in test_ids:
        crate = ROCrate()
        if name.endswith("/"):
            entity = crate.add_directory(path, name)
        else:
            entity = crate.add_file(path, name)
        deref_entity = crate.dereference(id_)
        assert deref_entity is entity


def test_contextual_entities():
    crate = ROCrate()
    new_person = crate.add(Person(crate, '#joe', {'name': 'Joe Pesci'}))
    person_dereference = crate.dereference('#joe')
    assert person_dereference is new_person
    assert person_dereference.type == 'Person'
    person_prop = person_dereference.properties()
    assert person_prop['@type'] == 'Person'
    assert person_prop['name'] == 'Joe Pesci'
    assert not new_person.datePublished
    id_ = "https://orcid.org/0000-0002-1825-0097"
    new_person = crate.add(Person(crate, id_, {'name': 'Josiah Carberry'}))
    person_dereference = crate.dereference(id_)
    assert person_dereference is new_person


def test_properties():
    crate = ROCrate()

    crate_name = "new crate"
    crate.name = crate_name
    assert crate.name == crate_name

    crate_description = "this is a new crate"
    crate.description = crate_description
    assert crate.description == crate_description

    assert crate.datePublished == crate.root_dataset.datePublished
    assert isinstance(crate.root_dataset.datePublished, datetime.datetime)
    assert isinstance(crate.root_dataset["datePublished"], str)
    crate_datePublished = datetime.datetime.now()
    crate.datePublished = crate_datePublished
    assert crate.datePublished == crate_datePublished

    new_person = crate.add(Person(crate, '#001', {'name': 'Lee Ritenour'}))
    crate.creator = new_person
    assert crate.creator is new_person
    assert isinstance(crate.creator, Person)
    assert crate.creator['name'] == 'Lee Ritenour'
    assert crate.creator.type == 'Person'

    new_person2 = crate.add(Person(crate, '#002', {'name': 'Lee Ritenour'}))
    crate.creator = [new_person, new_person2]
    assert isinstance(crate.creator, list)
    assert crate.creator[0] is new_person
    assert crate.creator[1] is new_person2


def test_uuid():
    crate = ROCrate()
    new_person = crate.add(Person(crate, properties={"name": "No Identifier"}))
    jsonld = new_person.as_jsonld()
    assert "Person" == jsonld["@type"]
    assert jsonld["@id"].startswith("#")
    # Check it made a valid UUIDv4
    u = uuid.UUID(jsonld["@id"][1:])
    assert 4 == u.version


def test_update(test_data_dir, tmpdir, helpers):
    crate = ROCrate()
    assert not crate.root_dataset["hasPart"]
    wf_path = test_data_dir / "test_galaxy_wf.ga"
    john = crate.add(Person(crate, '#john', {'name': 'John Doe'}))
    file_ = crate.add_file(wf_path)
    assert crate.root_dataset["hasPart"] == [file_]
    file_["author"] = john
    assert isinstance(file_, File)
    assert crate.mainEntity is None
    wf = crate.add_workflow(wf_path, main=True, lang="galaxy")
    assert isinstance(wf, ComputationalWorkflow)
    assert wf["author"] is None
    assert crate.mainEntity is wf
    assert crate.dereference(john.id) is john
    assert crate.dereference(file_.id) is wf
    assert crate.root_dataset["hasPart"] == [wf]
    assert crate.root_dataset.properties()["hasPart"] == [{"@id": "test_galaxy_wf.ga"}]

    out_path = tmpdir / "ro_crate_out"
    out_path.mkdir()
    crate.write_crate(out_path)
    json_entities = helpers.read_json_entities(out_path)
    helpers.check_wf_crate(json_entities, wf.id)
