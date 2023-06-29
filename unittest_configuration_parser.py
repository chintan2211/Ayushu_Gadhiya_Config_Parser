import pytest
import os
from configuration_parser import ConfigParser

@pytest.fixture
def config_parser():
    return ConfigParser('config.yaml')

def test_read_yaml(config_parser):
    config_parser.read_config_file('.yaml')
    assert config_parser.config_data == {'database': {'host': 'localhost', 'port': 5432, 'username': 'admin', 'password': 'password123'}}

def test_generate_flat_dict(config_parser):
    config_parser.config_data = {'database': {'host': 'localhost', 'port': 5432}}
    flat_dict = config_parser.generate_flat_dict()
    assert flat_dict == {'database.host': 'localhost', 'database.port': 5432}

def test_write_env_file(tmp_path, config_parser):
    config_parser.config_data = {'key1': 'value1', 'key2': 'value2'}
    file_path = tmp_path / 'config.env'
    config_parser.write_env_file(file_path)
    assert file_path.read_text() == 'key1=value1\nkey2=value2\n'

def test_set_os_environment(config_parser, monkeypatch):
    config_parser.config_data = {'key1': 'value1', 'key2': 'value2'}
    config_parser.set_os_environment()
    assert os.environ.get('key1') == 'value1'
    assert os.environ.get('key2') == 'value2'
