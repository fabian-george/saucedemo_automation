import time

import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from utilities.test_data import TestData


def pytest_configure(config):
    config.stash[metadata_key]["Author"] = "Fabian Parsia George"


@pytest.fixture
def driver():
    chrome_options = Options()

    if TestData.HEADLESS:
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=PasswordManager")
    chrome_options.add_experimental_option("detach", True)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    driver.close()


@pytest.fixture
def inventory_page(driver):
    login_page = LoginPage(driver)
    login_page.open_page()
    time.sleep(1)
    inventory_page = login_page.login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
    time.sleep(2)

    assert inventory_page.is_on_inventory_page()
    return inventory_page
