import pytest, os
from pages.login_page import LoginPage
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")


def test_login(driver):
    login_page = LoginPage(driver)

    login_page.enter_credentials(USERNAME, PASSWORD)
    home_page = login_page.click_login()

    assert home_page.check_if_logged_in()