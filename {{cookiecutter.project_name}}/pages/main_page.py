from utils.Driver import Driver

from pages.base_page import BasePage
from pages.locators import MainPageLocators

class MainPage(BasePage):

    def __init__(self, driver: Driver):
        self.locators = MainPageLocators
        super().__init__(driver=driver)