from src.data.data_loader import DataLoader
import pytest

@pytest.fixture
def data_loader():
    return DataLoader()

def test_load_raw_data(data_loader):
    raw_data = data_loader.load_raw_data()
    assert raw_data is not None
    assert len(raw_data) > 0  # Ensure that raw data is loaded and not empty

def test_load_processed_data(data_loader):
    processed_data = data_loader.load_processed_data()
    assert processed_data is not None
    assert len(processed_data) > 0  # Ensure that processed data is loaded and not empty

def test_load_raw_data_structure(data_loader):
    raw_data = data_loader.load_raw_data()
    assert isinstance(raw_data, dict)  # Assuming raw data is loaded as a dictionary

def test_load_processed_data_structure(data_loader):
    processed_data = data_loader.load_processed_data()
    assert isinstance(processed_data, dict)  # Assuming processed data is loaded as a dictionary