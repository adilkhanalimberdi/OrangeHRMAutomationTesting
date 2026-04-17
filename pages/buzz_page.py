import json, requests
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
        try:
            response = requests.get(self.TEXT_API_URL, params={"format": "json"}, timeout=5) # REQUESTING TO THE EXTERNAL API
            response.raise_for_status()

            data = response.json()
            text = data.get("text") # GETTING RANDOM TEXT FROM API

            if not text:
                raise ValueError("No 'text' field in response")

            self.post(text) # POSTING TEXT
        except requests.exceptions.RequestException as e:
            print(f'Request error: {e}')
        except Exception as e:
            print(f'Unexpected error: {e}')

    def post(self, text):
        self.find_element(self.TEXTAREA_LOCATOR).send_keys(text)
        self.find_element(self.SUBMIT_BUTTON).click()

    def check_if_posted(self):
        toaster_text = self.find_element(self.TOAST).text
        return "success" in toaster_text.lower()
