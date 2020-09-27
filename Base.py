import os
from random import randint
from time import sleep

from pages.base_page import BasePage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from utils.Driver import Driver
from utils.helpers import get_file_entries


class Base(BasePage):

    def __init__(self, driver: Driver):
        self.url = url
        self.locators = MainPageLocators
        super().__init__(driver=driver)

    def auth(self):
        self.driver.get(f'{self.url}/auth')
        LoginPage(self.driver).sign_in()


driver = Driver.chrome() if Config.BROWSER == 'Chrome' else Driver.firefox()

base = Base(driver)
base.auth()