import pytest
from pages.dashboard_page import DashboardPage


@pytest.mark.smoke
@pytest.mark.regression
def test_logout(driver):
    dashboard_page = DashboardPage(driver)
    dashboard_page.open()
    login_page = dashboard_page.logout()

    assert login_page.is_logged_out()