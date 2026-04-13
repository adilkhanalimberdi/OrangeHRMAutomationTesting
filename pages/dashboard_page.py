from selenium.webdriver.common.by import By
from base_page import BasePage

class DashboardPage(BasePage):
    def check_if_logged_in(self):
        return self.find_element((By.CSS_SELECTOR, 'li[class="oxd-topbar-header-breadcrumb-module"]'), 10).text == "Dashboard"