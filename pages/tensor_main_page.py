from pages.base_page import BasePage
from pages.locators import TensorMainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TensorMainPage(BasePage):
    url = "https://tensor.ru/"
    
    def should_be_power(self):
        assert self.is_element_present(*TensorMainPageLocators.POWER)

    def should_be_more_info(self):
        assert self.is_element_present(*TensorMainPageLocators.MORE_INFO)
    
    def get_power_block(self):
        return self.browser.find_element(*TensorMainPageLocators.POWER)

    def open_more_info(self):
        more_info_link = self.browser.find_element(*TensorMainPageLocators.MORE_INFO)
        more_info_link.click()