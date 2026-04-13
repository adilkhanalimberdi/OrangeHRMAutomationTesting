import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()

    yield driver

    driver.quit()