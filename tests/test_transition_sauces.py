from locators import Locators
from data import Data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestTransitionSauces:
    def test_transition_sauces(self, drivers):

        driver = drivers
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.ENTER_ACCOUNT_TEXT_EMAIL).send_keys(Data.email)
        driver.find_element(*Locators.ENTER_ACCOUNT_TEXT_PASSWORD).send_keys(Data.password)
        driver.find_element(*Locators.DESINGER_BUTTON).click()
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        element = driver.find_element(*Locators.NAME_SAUCES)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.NAME_SAUCES))
        assert element.is_displayed()
        
        