import pytest
from pages.buzz_page import BuzzPage


@pytest.mark.regression
def test_post(driver):
    buzz_page = BuzzPage(driver)
    buzz_page.open()

    buzz_page.post_random_text()

    assert buzz_page.check_if_posted()