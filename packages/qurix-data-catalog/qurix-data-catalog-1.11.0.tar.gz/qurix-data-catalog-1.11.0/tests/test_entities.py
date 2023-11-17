import pytest

from qurix.data.catalog.entities import CatalogDataSource
from tests.utils import TEST_RESOURCES_PATH


@pytest.fixture
def sample_catalog_data():
    return {
        "name": "Sample",
        "location": f"{str(TEST_RESOURCES_PATH)}/source_a.csv",
        "has_obj_columns": True,
        "has_num_columns": True,
        "row_count": 10,
    }


def test_catalog_data_source_creation(sample_catalog_data):
    data_source = CatalogDataSource(**sample_catalog_data)
    assert data_source.name == sample_catalog_data["name"]
    assert data_source.location == sample_catalog_data["location"]
    assert data_source.table_schema is None
    assert data_source.table is None
    assert data_source.has_obj_columns == sample_catalog_data["has_obj_columns"]
    assert data_source.has_num_columns == sample_catalog_data["has_num_columns"]
    assert data_source.row_count == sample_catalog_data["row_count"]
