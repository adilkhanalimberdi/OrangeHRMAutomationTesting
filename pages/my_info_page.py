from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MyInfoPage(BasePage):
    FIRST_NAME_INPUT = (By.NAME, 'firstName')
    MIDDLE_NAME_INPUT = (By.NAME, 'middleName')
    LAST_NAME_INPUT = (By.NAME, 'lastName')
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    INPUT = (By.CSS_SELECTOR, ".oxd-input--active")
    TOAST = (By.CSS_SELECTOR, 'div.oxd-toast')

    def open(self, path="pim/viewPersonalDetails/empNumber/7"):
        super().open(path)

    def fill_field(self, locator, value):
        elem = self.find_element(locator)
        elem.send_keys(Keys.CONTROL, 'a')
        elem.send_keys(Keys.BACKSPACE)
        elem.send_keys(value)

    def change_info(self):
        # TODO

        self.find_element(self.SAVE_BUTTON).click()

    def check_if_success(self):
        toaster_text = self.driver.find_element(self.TOAST).text
        return "success" in toaster_text.lower()
