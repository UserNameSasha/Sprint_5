import pytest
from curl import URL
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def drivers():
    options = Options()
    options.add_argument("--window-size=1600,900")
    browser = webdriver.Chrome(options=options)
    browser.get(URL.main_site)
    yield browser
    browser.quit()

