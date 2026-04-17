from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DirectoryPage(BasePage):
    EMPLOYEE_NAME_INPUT = (By.CSS_SELECTOR, ".oxd-autocomplete-wrapper input")
    JOB_TITLE_SELECT = (By.XPATH, "//label[text()='Job Title']/following::div[@class='oxd-select-text-input'][1]")
    LOCATION_SELECT = (By.XPATH, "//label[text()='Location']/following::div[@class='oxd-select-text-input'][1]")

    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    CARD = (By.CSS_SELECTOR, ".orangehrm-directory-card")
    RECORD_COUNT = (By.CSS_SELECTOR, ".orangehrm-horizontal-padding .oxd-text--span")

    def open(self, path="directory/viewDirectory"):
        super().open(path)

    def search(self, name, job_title, location):
        actions = ActionChains(self.driver)

        element = self.find_element_clickable(self.EMPLOYEE_NAME_INPUT) # ENTERING AND CHOOSING THE FIRST OPTION
        actions.move_to_element_with_offset(element, 0, 0) \
            .click() \
            .send_keys(name) \
            .pause(2) \
            .move_by_offset(0, 50) \
            .click() \
            .perform()

        self.find_element_clickable(self.JOB_TITLE_SELECT).click() # SELECTING JOB TITLE
        self.find_element_clickable(
            (By.XPATH, f"//div[@role='listbox']//span[contains(text(), '{job_title}')]")
        ).click()

        self.find_element_clickable(self.LOCATION_SELECT).click() # SELECTING LOCATION
        self.find_element_clickable(
            (By.XPATH, f"//div[@role='listbox']//span[text()='{location}']")
        ).click()

        self.find_element_clickable(self.SEARCH_BUTTON).click() # CLICKING TO THE SEARCH BUTTON
        self.find_element_clickable(self.CARD).click() # CLICKING THE CARD

    def check_if_found(self):
        record_count = self.find_element(self.RECORD_COUNT).text
        print(f"DEBUG: '{record_count}'")

        if record_count == 'No Records Found':
            return False

        total = record_count.split("(")[1].split(")")[0]
        return int(total) > 0
