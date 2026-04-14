import json, os
from pages.login_page import LoginPage
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("ORANGE_USER")
PASSWORD = os.getenv("ORANGE_PASS")


def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open()

    login_page.enter_credentials(USERNAME, PASSWORD)
    home_page = login_page.click_login()

    assert home_page.check_if_logged_in()