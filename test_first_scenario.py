from pages.main_page import MainPage
from pages.contacts_page import ContactsPage
from pages.tensor_main_page import TensorMainPage
from pages.tensor_more_info_page import TensorMoreInfoPage

class TestFirstScenario():
    def test_user_can_go_to_contacts_page(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        main_page.should_be_contacts_nav()
        main_page.open_contacts_nav()

        main_page.should_be_more_contacts()
        main_page.open_more_contacts_page()
        
        contacts_page = ContactsPage(browser)
        contacts_page.should_be_tensor_link()
        contacts_page.open_tensor_site()

        browser.switch_to.window(browser.window_handles[1])
        tensor_main_page = TensorMainPage(browser)
        tensor_main_page.should_be_power()
        power_block = tensor_main_page.get_power_block()
        tensor_main_page.scroll(power_block)
        tensor_main_page.should_be_more_info()
        tensor_main_page.open_more_info()

        tensor_more_info_page = TensorMoreInfoPage(browser)
        working_block = tensor_more_info_page.get_working_block()
        tensor_more_info_page.scroll(working_block)

        tensor_more_info_page.should_be_working_photos()
        tensor_more_info_page.should_be_same_size()