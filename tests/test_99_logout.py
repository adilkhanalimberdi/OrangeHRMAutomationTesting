from pages.dashboard_page import DashboardPage


def test_logout(driver):
    dashboard_page = DashboardPage(driver)
    dashboard_page.open()
    dashboard_page.logout()

    assert "/auth/login" in driver.current_url