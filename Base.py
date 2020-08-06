import os
from random import randint
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.Config import Config
from utils.Driver import Driver
from utils.helpers import get_file_entries


class Base:

    def __init__(self, url, config: Config):
        self.url = url
        self.config = config
        self.driver = Driver.chrome() if self.config.BROWSER == 'Chrome' else Driver.firefox()

    @classmethod
    def factory(cls, url):
        base = cls(url, Config)
        return base
