import pytest
from selenium import webdriver
import sys
import os

# Добавляем корневую директорию проекта в sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
  # Импортируем Urls после добавления пути
from urls import Urls



@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.SCOOTER_URL)
    driver.maximize_window()
    yield  driver

    driver.quit()