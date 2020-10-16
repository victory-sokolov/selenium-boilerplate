from config import Config
from selenium.common.exceptions import (ElementClickInterceptedException, NoSuchElementException,
                                        TimeoutException)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.Driver import Driver


class BasePage:

    def __init__(self, driver, url='https://www.example.com/'):
        self.url = url
        self.driver = driver

    def hover(self, *locator, delay=10):
        element = self.find_element(*locator)
        self.driver.implicitly_wait(delay)
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

    def wait_until_element_is_clickable(self, locator, delay=10):
        try:
            return WebDriverWait(self.driver, delay).until(
                EC.element_to_be_clickable((locator))
            )
        except ElementClickInterceptedException:
            print("\n * ELEMENT IS NOT CLICKABLE! --> %s" %
                  (locator[1]))
            self.driver.quit()

    def wait_until_element_is_invisible(self, locator, delay=10):
        try:
            return WebDriverWait(self.driver, delay).until(
                EC.invisibility_of_element_located((locator))
            )
        except:
            print("\n * ELEMENT IS FOUND ON THE PAGE! --> %s" %
                  (locator[1]))
            self.driver.quit()

    def is_element_present(self, *locator, delay=10):
        self.driver.implicitly_wait(delay)
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        return True
