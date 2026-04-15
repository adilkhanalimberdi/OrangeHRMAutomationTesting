from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    LOGIN_FIELD = (By.CSS_SELECTOR, 'input[name="username"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[name="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')

    def open(self, path="auth/login"):
        super().open(path)

    def enter_credentials(self, username, password):
        self.find_element(self.LOGIN_FIELD).send_keys(username)
        self.find_element(self.PASSWORD_FIELD).send_keys(password)

    def click_login(self):
        self.find_element(self.LOGIN_BUTTON).click()

        if "dashboard" in self.driver.current_url:
            from pages.dashboard_page import DashboardPage
            return DashboardPage(self.driver)
        else:
            return self.driver