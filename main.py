from configuration_parser import ConfigParser

#read the .ini,.cfg,.conf file and convert into flat dict
cnf = ConfigParser(file_path='/home/dell/Desktop/sacumen_assignment/sample.cfg')
cnf.read_configparser()
res=cnf.generate_flat_dict()
cnf.write_env_file(file_path='/home/dell/Desktop/sacumen_assignment/config.env')
cnf.set_os_environment()
cnf.write_json_file(file_path='/home/dell/Desktop/sacumen_assignment/config.json')
print(res)


#read yaml file and convert it into flat dict

cnf = ConfigParser(file_path='/home/dell/Desktop/sacumen_assignment/config.yaml')
cnf.read_config_file('.yaml')
res = cnf.generate_flat_dict()
print(res)
cnf.write_env_file(file_path='/home/dell/Desktop/sacumen_assignment/config.env')
cnf.set_os_environment()
cnf.write_json_file(file_path='/home/dell/Desktop/sacumen_assignment/config.json')
