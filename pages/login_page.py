from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_FIELD = (By.CSS_SELECTOR, 'input[name="username"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[name="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')

    TOP_BAR_TITLE = (By.CSS_SELECTOR, '.oxd-topbar-header-breadcrumb-module')
    ERROR_ALERT = (By.CSS_SELECTOR, '.oxd-alert-content-text')

    def open(self, path="auth/login"):
        super().open(path)

    def enter_credentials(self, username, password):
        self.find_element(self.LOGIN_FIELD).send_keys(username)
        self.find_element(self.PASSWORD_FIELD).send_keys(password)

    def click_login(self):
        self.find_element(self.LOGIN_BUTTON).click()

    def is_logged_in(self):
        try:
            element = self.find_element(self.TOP_BAR_TITLE)
            return element.text == "Dashboard"
        except TimeoutException:
            return False

    def is_login_failed(self):
        try:
            return self.find_element(self.ERROR_ALERT, 5) is not None
        except TimeoutException:
            return False

    def is_logged_out(self):
        return "auth/login" in self.driver.current_url
