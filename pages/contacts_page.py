from pages.base_page import BasePage
from pages.locators import ContactsPageLocators

class ContactsPage(BasePage):
    url = "https://saby.ru/contacts"

    def should_be_the_region_in_panel(self, region_name):
        assert self.is_appeared(*ContactsPageLocators.get_region_by_name(region_name))

    def should_be_contacts_list(self):
        assert self.is_appeared(*ContactsPageLocators.CURRENT_CONTACTS_LIST), "Список партнёров отсутствует"

    def should_be_new_contacts_list(self, contacts):
        assert self.is_new_text(contacts, *ContactsPageLocators.CURRENT_CONTACTS_LIST), "Список партнёров не изменился"
        assert self.get_contacts_list() != "", "Список партнёров пустой"

    def should_be_region_panel(self):
        assert self.is_appeared(*ContactsPageLocators.REGION_PANEL), "Панель выбора региона не загрузилась"

    def should_be_tensor_link(self):
        assert self.is_element_present(*ContactsPageLocators.TENSOR_LINK), "Ссылка на сайт tensor.ru отсутствует"

    def change_region(self, region_name):
        new_region = self.browser.find_element(*ContactsPageLocators.get_region_by_name(region_name))
        new_region.click()

    def get_contacts_list(self):
        contacts_list = self.browser.find_element(*ContactsPageLocators.CURRENT_CONTACTS_LIST).text
        return contacts_list
    
    def is_needed_region_loaded(self, region_name):
        assert self.is_appeared(*ContactsPageLocators.get_header_region_by_name(region_name)), "Текущий регион не совпадает с желаемым"

    def is_tab_name_right(self, region_name):
        assert self.browser.title == f"Saby Контакты — {region_name}", "title не совпадает с желаемым"

    def is_url_right(self, region_name):
        assert self.browser.current_url[:self.browser.current_url.find("?tab=clients")] == f"{self.url}/{region_name}", "url не совпадает с желаемым"
    
    def open_region_panel(self):
        region = self.browser.find_element(*ContactsPageLocators.CURRENT_REGION)
        region.click()

    def open_tensor_site(self):
        tensor_link = self.browser.find_element(*ContactsPageLocators.TENSOR_LINK)
        tensor_link.click()

    def wait_for_search(self):
        assert self.is_appeared(*ContactsPageLocators.SEARCH_INPUT)