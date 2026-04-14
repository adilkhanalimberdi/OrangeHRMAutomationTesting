# import time
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class UserManagementPage(BasePage):
    USER_DROPDOWN = (By.CSS_SELECTOR, 'p.oxd-userdropdown-name')
    DOCUMENT_BODY = (By.TAG_NAME, 'body')

    def open(self, path="admin/viewSystemUsers"):
        super().open(path)

    def add_random_user(self):
        # TODO

        """
        As the process went I understand that this is a terrible code,
        in fact it was obvious at the beginning,
        but that is all I could come up with

        actions = ActionChains(self.driver)

        self.find_element(self.DOCUMENT_BODY)
        body = self.driver.find_element(self.DOCUMENT_BODY)

        actions.move_to_element_with_offset(body, 0, 0) \
            .move_by_offset(385, 520) \
            .click() \
            .perform()

        self.find_element(self.USER_DROPDOWN)

        actions.move_to_element_with_offset(body, 0, 0) \
            .move_by_offset(530, 350) \
            .click() \
            .move_by_offset(530, 475) \
            .click() \
            .perform()
        """