import pytest, time
from pages.directory_page import DirectoryPage
from data.directory_data import SEARCH_DATA


@pytest.mark.parametrize("name, job_title, location", SEARCH_DATA)
@pytest.mark.regression
def test_search_and_email(driver, name, job_title, location):
    page = DirectoryPage(driver)
    page.open()

    page.search(name, job_title, location)
    time.sleep(1)

    assert page.check_if_found()
