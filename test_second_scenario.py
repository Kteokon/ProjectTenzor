from pages.main_page import MainPage
from pages.contacts_page import ContactsPage
from pages.tensor_main_page import TensorMainPage
from pages.tensor_more_info_page import TensorMoreInfoPage
import time

class TestSecondScenario():
    REGION = "г. Москва"
    NEW_REGION = "Камчатский край"
    NEW_URL = "41-kamchatskij-kraj"

    def is_region_loaded(self, page, region):
        # page.should_be_region()
        page.is_right_region_loaded(region)
        page.should_be_contacts_list()
        return page.get_contacts_list()
    
    def is_region_changed(contacts1, contacts2):
        assert contacts1 != contacts2

    def test_user_can_go_to_contacts_page(self, browser):
        # main_page = MainPage(browser)
        # main_page.open()
        # main_page.should_be_contacts_nav()
        # main_page.open_contacts_nav()

        # main_page.should_be_more_contacts()
        # main_page.open_more_contacts_page()
        
        contacts_page_before = ContactsPage(browser)
        contacts_page_before.open()
        # Ждём, что регион в верхней панели *загрузился* нужный нам
        # contacts_page_before.is_right_region_loaded(self.REGION)
        contacts_list_before = self.is_region_loaded(contacts_page_before, self.REGION)

        contacts_page_before.open_region_panel()
        contacts_page_before.should_be_region_panel()
        contacts_page_before.should_be_clickable_region(self.NEW_REGION)
        time.sleep(10)
        contacts_page_before.change_region(self.NEW_REGION)

        # # Подождать, пока загрузится регион с нужным названием
        # contacts_page_after = ContactsPage(browser)
        contacts_page_before.is_right_region_loaded(self.NEW_REGION)
        print(browser.title)
        # contacts_page_after.should_be_region()
        # contacts_page_after.should_be_region()
        # contacts_page_after.is_region_correct(self.NEW_REGION)
        # contacts_list_after = self.is_region_loaded(contacts_page_after, self.NEW_REGION)
        # self.is_region_changed(contacts_list_before, contacts_list_after)
        # contacts_page_after.should_be_region_contacts_url(self.NEW_URL)
        # contacts_page_after.should_be_region_contacts_tab(self.NEW_REGION)

