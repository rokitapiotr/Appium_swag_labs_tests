import configparser


def get_config():
    config = configparser.ConfigParser()
    config.read('file_utils/properties.ini')
    return config
