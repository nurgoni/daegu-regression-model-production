import pytest

from daegu_regression.config.core import app_config
from daegu_regression.processing.data_manager import load_dataset


@pytest.fixture()
def sample_input_data():
    return load_dataset(file_name=app_config.test_data_file)
