from curl import URL
from locators import Locators
from data import Data


class TestTransitionRolls:
    def test_transition_rolls(self, drivers):

        driver = drivers
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.ENTER_ACCOUNT_TEXT_EMAIL).send_keys(Data.email)
        driver.find_element(*Locators.ENTER_ACCOUNT_TEXT_PASSWORD).send_keys(Data.password)
        driver.find_element(*Locators.DESINGER_BUTTON).click()
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        driver.find_element(*Locators.ROLLS_BUTTON).click()
        driver.find_element(*Locators.BREAD).click()
        assert driver.current_url == URL.main_site + 'ingredient/61c0c5a71d1f82001bdaaa6d'
        