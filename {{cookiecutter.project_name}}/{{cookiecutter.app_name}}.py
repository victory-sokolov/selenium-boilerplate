import os
import logging
from datetime import datetime
from random import randint
from time import sleep

from pages.base_page import BasePage
from pages.login_page import LoginPage

from utils.Driver import Driver
from config import Config
from pages.login_page import LoginPage
from pages.main_page import MainPage

if not os.path.exists('debug'):
    os.mkdir('debug')

logging.basicConfig(filename='debug/Teezily.log',
                    level=logging.ERROR,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s'
                    )
logger = logging.getLogger(__name__)

class Base(BasePage):

    def __init__(self, driver: Driver):
        self.driver = driver
        super().__init__(driver=driver)

    def run_process(self):
        try:
            self.driver.get(self.url)
            sleep(5)
            if 'sign_in' in self.driver.current_url:
                LoginPage(self.driver).sign_in()
                sleep(30)

            main = MainPage(self.driver)
            main.email_popup()
            main.upload_design()
        except Exception as err:
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(f'debug/{now}.png')
            logger.error(err)
            print(err)


if __name__ == "__main__":
    driver = Driver.chrome()
    base = Base(driver)
    base.run_process()
