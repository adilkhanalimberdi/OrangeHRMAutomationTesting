import pytest
from pages.login_page import LoginPage
from data.login_data import CREDENTIALS


@pytest.mark.parametrize("username, password, expected", CREDENTIALS)
@pytest.mark.test
@pytest.mark.smoke
@pytest.mark.regression
def test_login(driver, username, password, expected):
    page = LoginPage(driver)
    page.open()

    page.enter_credentials(username, password)
    page.click_login()

    if expected == "fail":
        assert page.is_login_failed()
    elif expected == "success":
        assert page.is_logged_in()
