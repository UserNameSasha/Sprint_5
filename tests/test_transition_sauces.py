#from curl import URL
from locators import Locators
from data import Data
from selenium.webdriver.support.wait import WebDriverWait


class TestTransitionSauces:
    def test_transition_sauces(self, drivers):

        driver = drivers
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.ENTER_ACCOUNT_TEXT_EMAIL).send_keys(Data.email)
        driver.find_element(*Locators.ENTER_ACCOUNT_TEXT_PASSWORD).send_keys(Data.password)
        driver.find_element(*Locators.DESINGER_BUTTON).click()
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        #driver.find_element(*Locators.SAUCES).click()
        element = driver.find_element(*Locators.NAME_SAUCES)
        WebDriverWait(driver, 5)
        assert element == element
        