from pages.main_page import MainPage
from pages.contacts_page import ContactsPage
from pages.tensor_main_page import TensorMainPage
from pages.tensor_more_info_page import TensorMoreInfoPage

class TestFirstScenario():
    MAIN_BLOCK_NAME = "Сила в людях"
    MORE_INFO_BLOCK_NAME = "Работаем"

    def test_get_info_about_tensor(self, browser):
        # Переход на страницу с контактами
        main_page = MainPage(browser)
        main_page.open()
        main_page.should_be_contacts_nav()
        main_page.open_contacts_nav()
        main_page.should_be_more_contacts()
        main_page.open_more_contacts_page()
        
        # Переход на страницу tensor.ru по баннеру
        contacts_page = ContactsPage(browser)
        contacts_page.should_be_tensor_link()
        contacts_page.open_tensor_site()

        # Переключение на вкладку с tensor.ru, поиск нужного блока
        browser.switch_to.window(browser.window_handles[1])
        tensor_main_page = TensorMainPage(browser)
        tensor_main_page.should_be_the_block(self.MAIN_BLOCK_NAME)
        power_block = tensor_main_page.get_the_block(self.MAIN_BLOCK_NAME)
        tensor_main_page.scroll(power_block)
        tensor_main_page.should_be_more_info(power_block)
        tensor_main_page.open_more_info(power_block)

        # Поиск блока с фотографиями, проверка совпадения размеров фотографий
        tensor_more_info_page = TensorMoreInfoPage(browser)
        tensor_more_info_page.should_be_the_block(self.MORE_INFO_BLOCK_NAME)
        working_block = tensor_more_info_page.get_the_block(self.MORE_INFO_BLOCK_NAME)
        tensor_more_info_page.scroll(working_block)
        tensor_more_info_page.should_be_pictures(working_block)
        tensor_more_info_page.is_pictures_same_size(working_block)