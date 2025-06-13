from pages.base_page import BasePage
from pages.locators import ContactsPageLocators

class ContactsPage(BasePage):
    url = "https://saby.ru/contacts"

    def should_be_clickable_region(self, region_name):
        assert self.is_clickable(*ContactsPageLocators.get_region_by_name(region_name))

    def should_be_contacts_list(self):
        assert self.is_element_present(*ContactsPageLocators.CURRENT_CONTACTS_LIST), "Список партнёров отсутствует"

    def should_be_region_contacts_tab(self, region_name):
        print(self.browser.title)
        # assert self.browser.title == f"{self.url}/{region_name}"

    def should_be_region_contacts_url(self, region_name):
        assert self.url[:self.url.find("?tab=clients")] == f"{self.url}/{region_name}"

    def should_be_region(self):
        assert self.is_appeared(*ContactsPageLocators.CURRENT_REGION)

    def should_be_region_panel(self):
        assert self.is_appeared(*ContactsPageLocators.REGION_PANEL)

    def should_be_tensor_link(self):
        assert self.is_element_present(*ContactsPageLocators.TENSOR_LINK)

    def change_region(self, region_name):
        new_region = self.browser.find_element(*ContactsPageLocators.get_region_by_name(region_name))
        new_region.click()

    def get_contacts_list(self):
        contacts_list_wb = self.browser.find_elements(*ContactsPageLocators.CURRENT_CONTACTS_LIST)
        contacts_list = []
        for contact in contacts_list_wb:
            contacts_list.append(contact.text)
        return contacts_list
    
    def is_right_region_loaded(self, region_name):
        assert self.is_appeared(*ContactsPageLocators.get_header_region_by_name(region_name))

    def is_region_correct(self, region_name):
        print(self.browser.find_element(*ContactsPageLocators.CURRENT_REGION).text, region_name)
        assert self.browser.find_element(*ContactsPageLocators.CURRENT_REGION).text == region_name, "Текущий регион не совпадает с желаемым регионом"
    
    def open_region_panel(self):
        region = self.browser.find_element(*ContactsPageLocators.CURRENT_REGION)
        region.click()

    def open_tensor_site(self):
        tensor_link = self.browser.find_element(*ContactsPageLocators.TENSOR_LINK)
        tensor_link.click()