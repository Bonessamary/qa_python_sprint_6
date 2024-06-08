import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from data import URLs


@pytest.fixture
def driver():
    firefox_options = Options()
    firefox_options.set_preference("browser.privatebrowsing.autostart", True)
    driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()
    driver.get(URLs.MAIN_PAGE_URL)
    yield driver
    driver.quit()