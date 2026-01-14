from curl import URL
from locators import Locators
from data import Data

class TestEnterPersonalAccountWithEnterButton:
    def test_enter_personal_account(self, drivers):
        
        driver = drivers
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()       
        driver.find_element(*Locators.ENTER_ACCOUNT_WIHT_ENTER_BUTTON).click()        
        driver.find_element(*Locators.ENTER_ACCOUNT_TEXT_EMAIL).send_keys(Data.email)
        driver.find_element(*Locators.ENTER_ACCOUNT_TEXT_PASSWORD).send_keys(Data.password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        assert driver.current_url == URL.main_site + "login"
        