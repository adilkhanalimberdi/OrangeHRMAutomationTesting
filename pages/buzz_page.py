import json
import requests
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class BuzzPage(BasePage):
    TEXT_API_URL = "https://fish-text.ru/get"
    TEXTAREA_LOCATOR = (By.CSS_SELECTOR, "textarea.oxd-buzz-post-input")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    TOAST = (By.CSS_SELECTOR, 'div.oxd-toast')

    def open(self, path="buzz/viewBuzz"):
        super().open(path)

    def post_random_text(self):
        response = requests.get(self.TEXT_API_URL, params={"format": "json"})

        data = json.loads(response.text)
        self.post(data['text'])

    def post(self, text):
        self.find_element(self.TEXTAREA_LOCATOR).send_keys(text)
        self.find_element(self.SUBMIT_BUTTON).click()

    def check_if_posted(self):
        toaster_text = self.find_element(self.TOAST).text
        return "success" in toaster_text.lower()
