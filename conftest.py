import pytest
from selenium import webdriver
from urls import Urls



@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.SCOOTER_URL)
    driver.maximize_window()
    yield  driver

    driver.quit()