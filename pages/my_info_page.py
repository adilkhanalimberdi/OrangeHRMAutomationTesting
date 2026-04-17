from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MyInfoPage(BasePage):
    FIRST_NAME_INPUT = (By.NAME, 'firstName')
    MIDDLE_NAME_INPUT = (By.NAME, 'middleName')
    LAST_NAME_INPUT = (By.NAME, 'lastName')

    EMP_ID_INPUT = (By.XPATH, "//label[text()='Employee Id']/following::input[1]")
    OTH_ID_INPUT = (By.XPATH, "//label[text()='Other Id']/following::input[1]")
    LIC_INPUT = (By.XPATH, '//label[text()="Driver\'s License Number"]/following::input[1]')
    EXP_DATE = (By.XPATH, "//label[text()='License Expiry Date']/following::input[1]")
    BIRTH_DATE = (By.XPATH, "//label[text()='Date of Birth']/following::input[1]")

    SAVE_BUTTON = (By.XPATH, "(//button[@type='submit'])[1]")

    TOAST = (By.CSS_SELECTOR, '.oxd-toast')
    SPINNER = (By.CSS_SELECTOR, '.oxd-form-loader')

    def open(self, path="pim/viewPersonalDetails/empNumber/7"):
        super().open(path)

    def fill_field(self, locator, value):
        element = self.find_element(locator)
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(value)

    def change_info(self):
        self.find_element_disappear(self.SPINNER)

        self.fill_field(self.FIRST_NAME_INPUT, "SDU_AUTOMATION_TESTING")
        self.fill_field(self.MIDDLE_NAME_INPUT, "SDU_AUTOMATION_TESTING")
        self.fill_field(self.LAST_NAME_INPUT, "SDU_AUTOMATION_TESTING")

        self.fill_field(self.EMP_ID_INPUT, "TEST_ID")
        self.fill_field(self.OTH_ID_INPUT, "TEST_ID")
        self.fill_field(self.LIC_INPUT, "55555555555")
        self.fill_field(self.EXP_DATE, "1111-11-11")
        self.fill_field(self.BIRTH_DATE, "1010-10-10")

        self.find_element_clickable(self.SAVE_BUTTON).click()

    def check_if_success(self):
        toaster_text = self.find_element(self.TOAST).text
        return "success" in toaster_text.lower()
