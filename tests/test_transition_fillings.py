#from curl import URL
from locators import Locators
from data import Data
from selenium.webdriver.support.wait import WebDriverWait


class TestTransitionFillings:
    def test_transition_fillings(self, drivers):

        driver = drivers
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.ENTER_ACCOUNT_TEXT_EMAIL).send_keys(Data.email)
        driver.find_element(*Locators.ENTER_ACCOUNT_TEXT_PASSWORD).send_keys(Data.password)
        driver.find_element(*Locators.DESINGER_BUTTON).click()
        driver.find_element(*Locators.FILLINGS_BUTTON).click()
        #driver.find_element(*Locators.FILLINGS).click()
        element = driver.find_element(*Locators.NAME_FILLINGS)
        WebDriverWait(driver, 5)
        assert element == element

       
        