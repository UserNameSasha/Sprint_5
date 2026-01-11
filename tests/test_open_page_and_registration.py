from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data


class TestStellarBurgersOpenAndRegistration:
    def test_reg_new_user(self, drivers):
        
        driver = drivers
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys(Data.name)
        driver.find_element(*Locators.EMAIL).send_keys(Data.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Data.password)        
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys(Data.name)
        driver.find_element(*Locators.EMAIL).send_keys(Data.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Data.password)        
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        reg_text = WebDriverWait(driver, 10, poll_frequency=0.1).until(EC.visibility_of_element_located(Locators.REG_TEXT)).text
        assert reg_text == 'Такой пользователь уже существует'
        driver.quit()
