from qurix.data.catalog.client import DataCatalogClient
from qurix.data.catalog.entities import CatalogDataSource
import pytest
import subprocess


@pytest.fixture
def empty_catalog_client() -> DataCatalogClient:
    return DataCatalogClient()


@pytest.fixture
def data_catalog_entry_db2() -> CatalogDataSource:
    return CatalogDataSource(name="source g",
                             location="ibm_db_sa://db2dev:Welcome4$@localhost:50000/testdb",
                             table_schema="testschema",
                             table="dummy_data")


def test_load_db2(empty_catalog_client: DataCatalogClient, data_catalog_entry_db2: CatalogDataSource):
    subprocess.call("tests_integration/scripts_db2/tearup_db.sh")
    empty_catalog_client.add(dc_entry=data_catalog_entry_db2,
                             persist_data=True)
    result = empty_catalog_client.describe_obj("source_g")
    count_list = ([item for item in result["count"].to_list()])
    expected_list = ['10', '10', '10']
    assert count_list == expected_list
    subprocess.call("tests_integration/scripts_db2/teardown_db.sh")
