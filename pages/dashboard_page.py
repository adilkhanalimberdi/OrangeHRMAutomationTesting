from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    USER_DROPDOWN = (By.CSS_SELECTOR, 'p.oxd-userdropdown-name')
    LOGOUT_LINK = (By.XPATH, '/html/body/div/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[4]/a')

    def ope(self, path="dashboard/index"):
        super().open(path)

    def check_if_logged_in(self):
        title = self.find_element((By.CSS_SELECTOR, 'h6.oxd-topbar-header-breadcrumb-module'), 10).text
        return title == "Dashboard"

    def logout(self):
        self.find_element(self.USER_DROPDOWN).click()
        self.find_element(self.LOGOUT_LINK).click()

        from pages.login_page import LoginPage
        return LoginPage(self.driver)
