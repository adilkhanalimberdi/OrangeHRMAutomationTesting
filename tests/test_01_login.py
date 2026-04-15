import os, pytest
from pages.login_page import LoginPage
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("ORANGE_USER")
PASSWORD = os.getenv("ORANGE_PASS")


@pytest.mark.parametrize("username, password, expected", [
    ("some_username", "pass", "fail"),
    ("Admin", "wrong_pass", "fail"),
    ("idk", "just_password", "fail"),
    (USERNAME, PASSWORD, "success")
])
@pytest.mark.smoke
@pytest.mark.regression
def test_login(driver, username, password, expected):
    login_page = LoginPage(driver)
    login_page.open()

    login_page.enter_credentials(username, password)
    home_page = login_page.click_login()

    if expected == "success":
        assert home_page.check_if_logged_in()
    else:
        assert "auth/login" in driver.current_url