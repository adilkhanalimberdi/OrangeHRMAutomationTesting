import pytest
from pages.user_management_page import UserManagementPage


@pytest.mark.regression
def test_delete_user(driver):
    user_management_page = UserManagementPage(driver)
    user_management_page.open()

    user_management_page.delete_first_user()

    assert user_management_page.check_if_success()