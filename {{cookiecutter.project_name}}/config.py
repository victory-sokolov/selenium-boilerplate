import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    VERSION = 0.1
    BROWSER = os.getenv('BROWSER')
    CAPTCHA_KEY = os.getenv('CAPTCHA_API_KEY')
    PROXY_API = os.getenv('PROXY_API')
    PROXY_FILE = os.getenv('PROXY_FILE')
    INTERFACE = os.getenv('NO_INTERFACE')
    DOWNLOAD_DIR = os.getenv('DOWNLOAD_DIR')
    INPUT = os.getenv('INPUT')
    OUTPUT = os.getenv('OUTPUT')
    PAGELOAD_TIMEOUT = os.getenv('PAGELOAD_TIMEOUT')
