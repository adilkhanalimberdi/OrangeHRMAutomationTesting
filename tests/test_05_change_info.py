import pytest
from pages.my_info_page import MyInfoPage


@pytest.mark.skip
def test_change_info(driver):
    my_info_page = MyInfoPage(driver)
    my_info_page.open()

    # TODO
    my_info_page.change_info()

    assert my_info_page.check_if_success()