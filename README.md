Configuration Parser:
This is a Python module for parsing and processing configuration files in various formats such as YAML, CFG, and CONF. It provides functionality to read configuration files, generate a flat dictionary, write configurations to different file formats, and set configurations in the OS environment.

Installation:
1.Clone the repository:
    git clone https://github.com/chintan2211/Ayushu_Gadhiya_Config_Parser.git
2.Navigate to the project directory:
    cd Ayushu_Gadhiya_Config_Parser
3.Install the required dependencies:
    pip install -r requirements.txt

Usage:
1.Import the ConfigurationParser class
    from configuration_parser import ConfigParser
2.Create an instance of ConfigurationParser by specifying the path to your configuration file:
    config_parser = ConfigurationParser('/path/to/config.yaml')
3.Read and process the configuration file:
    config_parser.read_config_file('.yaml')
4.Access the configuration data:
    flat_dict = config_parser.generate_flat_dict()
    print(flat_dict)
5.Write configurations to different file formats:
    config_parser.write_env_file('/path/to/config.env')
    config_parser.write_json_file('/path/to/config.json')
6.Set configurations in the OS environment:
    config_parser.set_os_environment()

