from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/"

    def open(self, path=""):
        return self.driver.get(self.base_url + path)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message = f"element located {locator} not found"
        )