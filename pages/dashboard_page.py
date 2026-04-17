from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    USER_DROPDOWN = (By.CSS_SELECTOR, 'p.oxd-userdropdown-name')
    LOGOUT_LINK = (By.CSS_SELECTOR, 'a[href="/web/index.php/auth/logout"]')
    TOP_BAR_TITLE = (By.CSS_SELECTOR, 'h6.oxd-topbar-header-breadcrumb-module')

    def open(self, path="dashboard/index"):
        super().open(path)

    def check_if_logged_in(self):
        return "auth/login" not in self.driver.current_url

    def logout(self):
        self.find_element(self.USER_DROPDOWN).click()
        self.find_element(self.LOGOUT_LINK).click()

        from pages.login_page import LoginPage
        return LoginPage(self.driver)
