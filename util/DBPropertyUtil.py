import configparser

def get_property_string(property_file):
    config = configparser.ConfigParser()
    config.read(property_file)
    
    return (f"mysql+pymysql://{config['DATABASE']['user']}:{config['DATABASE']['password']}"
            f"@{config['DATABASE']['host']}:{config['DATABASE']['port']}"
            f"/{config['DATABASE']['database']}")
