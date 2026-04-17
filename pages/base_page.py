from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/"

    def __init__(self, driver):
        self.driver = driver

    def open(self, path=""):
        return self.driver.get(self.BASE_URL + path)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message = f"element located {locator} not found"
        )

    def find_element_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator),
            message = f"element located {locator} not found"
        )

    def find_element_disappear(self, locator, time=10):
        WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"element located {locator} not found"
        )
        return WebDriverWait(self.driver, time).until(
            EC.invisibility_of_element_located(locator)
        )
