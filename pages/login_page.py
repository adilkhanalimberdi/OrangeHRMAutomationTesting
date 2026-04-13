from selenium.webdriver.common.by import By
from base_page import BasePage
from dashboard_page import DashboardPage

class LoginPage(BasePage):
    LOGIN_FIELD = (By.CSS_SELECTOR, 'input[name="username"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[name="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')

    def open(self):
        self.driver.get(self.base_url + "auth/login")

    def enter_credentials(self, username, password):
        self.find_element(self.LOGIN_FIELD).send_keys(username)
        self.find_element(self.PASSWORD_FIELD).send_keys(password)

    def click_login(self):
        return DashboardPage(self.find_element(self.LOGIN_BUTTON).click())