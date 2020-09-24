from pages.base_page import BasePage
from pages.locators import LoginPageLocator


class LoginPage(BasePage):

    def __init__(self, driver):
        self.locator = LoginPageLocator
        super().__init__(driver)

    def enter_username(self, username):
        self.find_element(*self.locator.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.find_element(*self.locator.PASSWORD).send_keys([password])

    def click_login_button(self):
        self.find_element(*self.locator.LOGIN_BTN).click()

    def sign_in(self):
        pass