from pages.user_management_page import UserManagementPage


def test_add_user(driver):
    user_management_page = UserManagementPage(driver)
    user_management_page.open()

    user_management_page.add_random_user()

    assert 1 == 1 # TODO