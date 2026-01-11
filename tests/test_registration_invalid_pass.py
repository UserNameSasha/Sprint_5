from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from helper import generate_registration_data_invalid



class TestRegistrationWithInvalidData:
    def test_reg_new_user_invalid_pass(self, drivers):
        
        
        driver = drivers 
        password = generate_registration_data_invalid()

        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys(Data.name)
        driver.find_element(*Locators.EMAIL).send_keys(Data.email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)         
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        pass_text = WebDriverWait(driver, 10, poll_frequency=0.1).until(EC.visibility_of_element_located(Locators.ERROR_PASS)).text
        assert pass_text == 'Некорректный пароль'
        driver.quit()