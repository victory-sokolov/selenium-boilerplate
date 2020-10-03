from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from utils.Driver import Driver
from config import Config

class BasePage:

    def __init__(self, driver, url='https://www.example.com/'):
        self.url = url
        self.driver = driver

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def wait_element(self, *locator, delay=10):
        
        try:
            return WebDriverWait(self.driver, delay).until(
                EC.presence_of_element_located((locator)))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %
                  (locator[1]))
            self.driver.quit()
