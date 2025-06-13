from pages.base_page import BasePage
from pages.locators import MoreInfoPageLocators
import time

class TensorMoreInfoPage(BasePage):
    url = "https://tensor.ru/about"

    def get_working_block(self):
        return self.browser.find_element(*MoreInfoPageLocators.WORKING)

    def get_working_photos(self):
        return self.browser.find_elements(*MoreInfoPageLocators.PHOTOS)
    
    def should_be_working_block(self):
        assert self.is_element_present(*MoreInfoPageLocators.WORKING)
    
    def should_be_working_photos(self):
        assert self.is_element_present(*MoreInfoPageLocators.PHOTOS)

    def should_be_same_size(self):
        time.sleep(20)
        photos = self.get_working_photos()
        widths, heights = set(), set()
        for photo in photos:
            widths.add(photo.get_attribute("width"))
            heights.add(photo.get_attribute("height"))
        assert len(widths) == 1 and len(heights) == 1, "Фото разных размеров"