from pages.base_page import BasePage
from pages.locators import MoreInfoPageLocators

class TensorMoreInfoPage(BasePage):
    url = "https://tensor.ru/about"
    
    def should_be_the_block(self, block_name):
        assert self.is_element_present(*MoreInfoPageLocators.get_block_by_name(block_name)), f"Блок \"{block_name}\" не был найден"
    
    def should_be_pictures(self, the_block):
        assert the_block.find_elements(*MoreInfoPageLocators.PICTURES), "В блоке не были найдены фотографии"

    def is_pictures_same_size(self, the_block):
        pictures = the_block.find_elements(*MoreInfoPageLocators.PICTURES)
        widths, heights = set(), set()
        for photo in pictures:
            widths.add(photo.get_attribute("width"))
            heights.add(photo.get_attribute("height"))
        assert len(widths) == 1 and len(heights) == 1, "Фотографии разных размеров"

    def get_the_block(self, block_name):
        return self.browser.find_element(*MoreInfoPageLocators.get_block_by_name(block_name))

    def get_pictures(self, the_block):
        return the_block.find_elements(*MoreInfoPageLocators.PICTURES)