from curl import URL
from locators import Locators
from data import Data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogOut:
    def test_log_out(self, drivers):
        
        driver = drivers
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.ENTER_ACCOUNT_TEXT_EMAIL).send_keys(Data.email)
        driver.find_element(*Locators.ENTER_ACCOUNT_TEXT_PASSWORD).send_keys(Data.password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EXIT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_contains(URL.main_site + "login"))
        assert driver.current_url == URL.main_site + "login"
