from pages.main_page import MainPage
from pages.contacts_page import ContactsPage

class TestSecondScenario():
    REGION = "Иркутская обл."
    NEW_REGION = "Камчатский край"
    NEW_URL = "41-kamchatskij-kraj"

    def test_change_region(self, browser):
        # Переход на страницу с контактами
        main_page = MainPage(browser)
        main_page.open()
        main_page.should_be_contacts_nav()
        main_page.open_contacts_nav()
        main_page.should_be_more_contacts()
        main_page.open_more_contacts_page()
        
        # Проверка корректности определённого региона
        contacts_page = ContactsPage(browser)
        contacts_page.is_needed_region_loaded(self.REGION)
        contacts_page.should_be_contacts_list()
        contacts_list_before = contacts_page.get_contacts_list()

        # Открытие панели со списком регионов и переключение на нужный
        contacts_page.open_region_panel()
        contacts_page.wait_for_search()
        contacts_page.should_be_the_region_in_panel(self.NEW_REGION)
        contacts_page.change_region(self.NEW_REGION)

        # Проверка корректности переключённого региона, ссылки, наименования вкладки, обновление списка партнёров
        contacts_page.is_needed_region_loaded(self.NEW_REGION)
        contacts_page.should_be_new_contacts_list(contacts_list_before)
        contacts_page.is_url_right(self.NEW_URL)
        contacts_page.is_tab_name_right(self.NEW_REGION)

