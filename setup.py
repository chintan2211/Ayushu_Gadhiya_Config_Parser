from setuptools import setup

setup(
    name='configuration-parser',
    version='1.0',
    py_modules=['configuration_parser'],
    install_requires=[
        'pyyaml',
        'configparser',
        'json5',
    ],
)
