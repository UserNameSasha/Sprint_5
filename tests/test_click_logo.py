from locators import Locators
from curl import URL


class TestClickLogo:
    def test_click_Logo(self, drivers):
        
        driver = drivers
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.LOGO).click()
        assert driver.current_url == URL.main_site
        driver.quit()