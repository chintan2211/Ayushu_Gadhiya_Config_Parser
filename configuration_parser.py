import os
import yaml
import configparser
import json

class ConfigParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config_data = {}

    def read_yaml_file(self):
        with open(self.file_path, 'r') as file:
            self.config_data = yaml.safe_load(file)
            print(self.config_data,"--------------------")

    def read_config_file(self, file_format):
        if file_format == '.yaml':
            self.read_yaml_file()
        elif file_format == '.cfg' or file_format == '.conf':
            self.read_configparser()

    def read_configparser(self):
        config = configparser.RawConfigParser()
        config.read(self.file_path)
        self.config_data = {}
        for section in config.sections():
            self.config_data[section] = {}
            for option in config.options(section):
                self.config_data[section][option] = config.get(section, option)

    def generate_flat_dict(self):
        flat_dict = {}
        self.flatten_dict(self.config_data, flat_dict)
        return flat_dict

    def flatten_dict(self, data, flat_dict, prefix=''):
        for key, value in data.items():
            if isinstance(value, dict):
                self.flatten_dict(value, flat_dict, prefix + key + '.')
            else:
                flat_dict[prefix + key] = value

    def write_env_file(self, file_path):
        with open(file_path, 'w') as file:
            for key, value in self.config_data.items():
                file.write(f"{key}={value}\n")
        with open(file_path,'r') as file:
            print(file.read())

    def write_json_file(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.config_data, file, indent=4)

    def set_os_environment(self):
        for key, value in self.config_data.items():
            os.environ[key] = str(value)
