from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SIGN_IN_BTN = (By.ID, "login-submit")

class MainPageLocators:
    pass
