from utils.helpers import read_configs

config = read_configs()


class Config:
    BROWSER = config['BROWSER']
    CAPTCHA_KEY = config['CAPTCHA_API_KEY']
    PROXY_API = config['PROXY_API']
    PROXY_FILE = config['PROXY_FILE']
    INTERFACE = config['NO_INTERFACE']
    DOWNLOAD_DIR = config['DOWNLOAD_DIR']
    INPUT = config['INPUT']
    OUTPUT = config['OUTPUT']
    USERNAME = config['USERNAME']
    PASSWORD = config['PASSWORD']
