from pages.base_page import BasePage
from pages.locators import TensorMainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TensorMainPage(BasePage):
    url = "https://tensor.ru/"
    
    def should_be_the_block(self, block_name):
        assert self.is_element_present(*TensorMainPageLocators.get_block_by_name(block_name)), f"Блок \"{block_name}\" не был найден"

    def should_be_more_info(self, the_block):
        assert the_block.find_element(*TensorMainPageLocators.MORE_INFO), "В блоке не была найдена ссылка \"Подробнее\""
    
    def get_the_block(self, block_name):
        return self.browser.find_element(*TensorMainPageLocators.get_block_by_name(block_name))

    def open_more_info(self, the_block):
        more_info_link = the_block.find_element(*TensorMainPageLocators.MORE_INFO)
        more_info_link.click()