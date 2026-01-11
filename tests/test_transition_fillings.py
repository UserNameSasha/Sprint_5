from curl import URL
from locators import Locators
from data import Data


class TestTransitionFillings:
    def test_transition_fillings(self, drivers):

        driver = drivers
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.ENTER_ACCOUNT_TEXT_EMAIL).send_keys(Data.email)
        driver.find_element(*Locators.ENTER_ACCOUNT_TEXT_PASSWORD).send_keys(Data.password)
        driver.find_element(*Locators.DESINGER_BUTTON).click()
        driver.find_element(*Locators.FILLINGS_BUTTON).click()
        assert driver.current_url == URL.main_site
        driver.quit()