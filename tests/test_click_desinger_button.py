from locators import Locators
from curl import URL


class TestClickDesingerButton:
    def test_click_desinger_button(self, drivers):
        
        driver = drivers
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.DESINGER_BUTTON).click()
        assert driver.current_url == URL.main_site
        driver.quit()