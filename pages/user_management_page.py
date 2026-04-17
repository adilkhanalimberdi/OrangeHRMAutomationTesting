from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.string_utils import get_random_symbols


class Locators:
    ADD_BUTTON = (By.XPATH, "//button[contains(., 'Add')]")

    USER_ROLE_SELECT = (By.CSS_SELECTOR, ".oxd-grid-item:nth-child(1) .oxd-select-text")
    USER_STATUS_SELECT = (By.CSS_SELECTOR, '.oxd-grid-item:nth-child(3) .oxd-select-text')

    ESS_OPTION = (By.XPATH, "//div[@role='listbox']//*[contains(text(), 'ESS')]")
    ENABLED_OPTION = (By.XPATH, "//div[@role='listbox']//*[contains(text(), 'Enabled')]")

    EMP_NAME_INPUT = (By.CSS_SELECTOR, '.oxd-autocomplete-text-input input')
    HINTS = (By.CSS_SELECTOR, 'div.oxd-autocomplete-dropdown')
    USERNAME_INPUT = (By.CSS_SELECTOR, '.oxd-grid-item:nth-child(4) input')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '.oxd-form-row:nth-child(2) .oxd-grid-item:nth-child(1) input')
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, '.oxd-form-row:nth-child(2) .oxd-grid-item:nth-child(2) input')

    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    TOAST_MESSAGE = (By.CSS_SELECTOR, '.oxd-toast')

    FIRST_USER_DELETE_BUTTON = (By.CSS_SELECTOR, ".oxd-table-body .oxd-table-card:nth-child(2) .bi-trash")
    CONFIRM_DELETE_BUTTON = (By.CSS_SELECTOR, ".oxd-button--label-danger .bi-trash")


class UserManagementPage(BasePage):
    def open(self, path="admin/viewSystemUsers"):
        super().open(path)

    def add_random_user(self):
        self.find_element(Locators.ADD_BUTTON).click() # CLICK ADD BUTTON

        self.find_element(Locators.USER_ROLE_SELECT).click() # SELECTING THE ROLE AS ESS
        self.find_element(Locators.ESS_OPTION).click()

        self.find_element(Locators.USER_STATUS_SELECT).click() # SELECTING THE STATUS AS ENABLED
        self.find_element(Locators.ENABLED_OPTION).click()

        elem = self.find_element(Locators.EMP_NAME_INPUT) # CHOOSING THE FIRST NAME THAT STARTS FROM 'a'
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(elem, 0, 0) \
            .click() \
            .send_keys('a') \
            .pause(2) \
            .move_by_offset(0, 50) \
            .click() \
            .perform()

        self.find_element(Locators.USERNAME_INPUT).send_keys(get_random_symbols(12)) # ENTERING USERNAME

        password = get_random_symbols(8)
        self.find_element(Locators.PASSWORD_INPUT).send_keys(password) # ENTERING PASSWORD
        self.find_element(Locators.CONFIRM_PASSWORD_INPUT).send_keys(password)

        self.find_element(Locators.SUBMIT_BUTTON).click() # SUBMIT

    def delete_first_user(self):
        self.find_element(Locators.FIRST_USER_DELETE_BUTTON).click()
        self.find_element(Locators.CONFIRM_DELETE_BUTTON).click()

    def check_if_success(self):
        toaster_text = self.find_element(Locators.TOAST_MESSAGE).text
        return "success" in toaster_text.lower()
