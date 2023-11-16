from unittest.mock import patch

import pandas as pd
import pytest

from qurix.data.catalog.dataloader import (CsvDataLoader, DB2DataLoader,
                                           ParquetDataLoader,
                                           PostgresDataLoader,
                                           SQLiteDataLoader, XlsxDataLoader)
from tests.utils import TEST_RESOURCES_PATH

# Mock data for testing
MOCK_DATA_FRAME_SQLITE = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'name': ["Alice", "Bob", "Charlie", "David", "Eva"],
    'age': [25, 30, 22, 28, 35]
})
MOCK_DATA_FRAME_CSV = pd.DataFrame({
    'Username': ['booker12', 'grey07', 'johnson81', 'jenkins46', 'smith79'],
    ' Identifier': [9012, 2070, 4081, 9346, 5079],
    'One-time password': ['12se74', '04ap67', '30no86', '14ju73', '09ja61'],
    'Recovery code': ['rb9012', 'lg2070', 'cj4081', 'mj9346', 'js5079'],
    'First name': ['Rachel', 'Laura', 'Craig', 'Mary', 'Jamie'],
    'Last name': ['Booker', 'Grey', 'Johnson', 'Jenkins', 'Smith'],
    'Department': ['Sales', 'Depot', 'Depot', 'Engineering', 'Engineering'],
    'Location': ['Manchester', 'London', 'London', 'Manchester', 'Manchester']
})
MOCK_DATA_FRAME_CSV_ERROR = pd.DataFrame({
    'Username': ['booker12', 'grey07', 'johnson81', 'jenkins46', 'smith79', 'test1'],
    ' Identifier': [9012, 2070, 4081, 9346, 5079, 42],
    'One-time password': ['12se74', '04ap67', '30no86', '14ju73', '09ja61', 'somepassword'],
    'Recovery code': ['rb9012', 'lg2070', 'cj4081', 'mj9346', 'js5079', '123'],
    'First name': ['Rachel', 'Laura', 'Craig', 'Mary', 'Jamie', 'John'],
    'Last name': ['Booker', 'Grey', 'Johnson', 'Jenkins', 'Smith', 'BonJov'],
    'Department': ['Sales', 'Depot', 'Depot', 'Engineering', 'Engineering', 'Engineering'],
    'Location': ['Manchester', 'London', 'London', 'Manchester', 'Manchester', 'Wales']
})
MOCK_SCHEMA = "schema"
MOCK_TABLE = "table"
MOCK_DATA_DB_DATA = pd.DataFrame({
    'Name': ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hank", "Ivy", "Jack"],
    'Age': [25, 30, 22, 35, 28, 40, 29, 27, 32, 26],
    'Email': ["alice@example.com", "bob@example.com", "charlie@example.com", "david@example.com", "eva@example.com", "frank@example.com", "grace@example.com", "hank@example.com", "ivy@example.com", "jack@example.com"],
    'Address': ["123 Main St", "456 Elm St", "789 Oak St", "101 Maple Ave", "202 Pine Rd", "123 Main St", "456 Elm St", "789 Oak St", "101 Maple Ave", "202 Pine Rd"]
})


@pytest.fixture
def mock_postgres_data_loader():
    return PostgresDataLoader("postgresql://{user}:{password}@{server}/{database}", MOCK_TABLE, MOCK_SCHEMA)


@pytest.fixture
def mock_db2_data_loader():
    return DB2DataLoader("ibm_db_sa://user:password@host:port/database", MOCK_TABLE, MOCK_SCHEMA)


@pytest.fixture
def mock_sqlite_data_loader():
    return SQLiteDataLoader(f"{str(TEST_RESOURCES_PATH)}/source_g.db", "users")


@pytest.fixture
def mock_csv_data_loader():
    return CsvDataLoader(f"{str(TEST_RESOURCES_PATH)}/source_a.csv")


@pytest.fixture
def mock_xlsx_data_loader():
    return XlsxDataLoader(f"{str(TEST_RESOURCES_PATH)}/source_e.xlsx")


@pytest.fixture
def mock_parquet_data_loader():
    return ParquetDataLoader(f"{str(TEST_RESOURCES_PATH)}/source_d.parquet")


def test_postgres_data_loader_load(mock_postgres_data_loader):
    with patch.object(PostgresDataLoader, "_load", return_value=MOCK_DATA_DB_DATA):
        result = mock_postgres_data_loader.load()
        assert result.equals(MOCK_DATA_DB_DATA)


def test_db2_data_loader_load(mock_db2_data_loader):
    with patch.object(DB2DataLoader, "_load", return_value=MOCK_DATA_DB_DATA):
        result = mock_db2_data_loader.load()
        assert result.equals(MOCK_DATA_DB_DATA)


def test_sqlite_data_loader_load(mock_sqlite_data_loader):
    result = mock_sqlite_data_loader.load()
    assert result.equals(MOCK_DATA_FRAME_SQLITE)


def test_csv_data_loader_load(mock_csv_data_loader):
    result = mock_csv_data_loader.load(sep=";")
    assert result.equals(MOCK_DATA_FRAME_CSV)


def test_csv_data_loader_load_error(mock_csv_data_loader):
    result = mock_csv_data_loader.load(sep=";")
    assert not result.equals(MOCK_DATA_FRAME_CSV_ERROR)


def test_xlsx_data_loader_load(mock_xlsx_data_loader):
    # TODO
    result = mock_xlsx_data_loader.load()
    test_data = pd.read_csv(
        f"{str(TEST_RESOURCES_PATH)}/source_e.csv", sep=";")
    assert not result.equals(test_data)


def test_parquet_data_loader_load(mock_parquet_data_loader):
    result = mock_parquet_data_loader.load()
    test_data = pd.read_csv(f"{str(TEST_RESOURCES_PATH)}/source_d.csv")
    assert result.equals(test_data)


def test_postgres_data_loader_get_row_count(mock_postgres_data_loader):
    with patch.object(PostgresDataLoader, "_get_row_count", return_value=10):
        result = mock_postgres_data_loader.get_row_count()
        test_result = len(MOCK_DATA_DB_DATA)
        assert result == test_result


def test_db2_data_loader_get_row_count(mock_db2_data_loader):
    with patch.object(DB2DataLoader, "_get_row_count", return_value=10):
        result = mock_db2_data_loader.get_row_count()
        test_result = len(MOCK_DATA_DB_DATA)
        assert result == test_result


def test_sqlite_data_loader_get_row_count(mock_sqlite_data_loader):
    result = mock_sqlite_data_loader.get_row_count()
    test_result = len(MOCK_DATA_FRAME_SQLITE)
    assert result == test_result


def test_csv_data_loader_get_row_count(mock_csv_data_loader):
    result = mock_csv_data_loader.get_row_count()
    test_result = len(MOCK_DATA_FRAME_CSV)
    assert result == test_result


def test_xlsx_data_loader_get_row_count(mock_xlsx_data_loader):
    result = mock_xlsx_data_loader.get_row_count()
    test_result = len(pd.read_csv(
        f"{str(TEST_RESOURCES_PATH)}/source_e.csv", sep=";"))
    assert result == test_result


def test_parquet_data_loader_get_row_count(mock_parquet_data_loader):
    result = mock_parquet_data_loader.get_row_count()
    test_result = len(pd.read_csv(f"{str(TEST_RESOURCES_PATH)}/source_d.csv"))
    assert result == test_result


def test_postgres_data_loader_get_str(mock_postgres_data_loader):
    result = mock_postgres_data_loader.__str__()
    assert result == "<PostgresDataLoader>"


def test_db2_data_loader_get_str(mock_db2_data_loader):
    result = mock_db2_data_loader.__str__()
    assert result == "<DB2DataLoader>"


def test_sqlite_data_loader_get_str(mock_sqlite_data_loader):
    result = mock_sqlite_data_loader.__str__()
    assert result == "<SQLiteDataLoader>"


def test_csv_data_loader_get_str(mock_csv_data_loader):
    result = mock_csv_data_loader.__str__()
    assert result == "<CsvDataLoader>"


def test_xlsx_data_loader_get_str(mock_xlsx_data_loader):
    result = mock_xlsx_data_loader.__str__()
    assert result == "<XlsxDataLoader>"


def test_parquet_data_loader_get_str(mock_parquet_data_loader):
    result = mock_parquet_data_loader.__str__()
    assert result == "<ParquetDataLoader>"
