from pages.base_page import BasePage
from pages.locators import MainPageLocators

class MainPage(BasePage):
    url = "https://saby.ru/"
    
    def should_be_contacts_nav(self):
        assert self.is_element_present(*MainPageLocators.NAV_CONTACTS), "Отсутствует раздел с контактами"

    def should_be_more_contacts(self):
        assert self.is_element_present(*MainPageLocators.MORE_CONTACTS), "Отсутствует переход в полный список контактов"

    def open_contacts_nav(self):
        contacts_nav = self.browser.find_element(*MainPageLocators.NAV_CONTACTS)
        contacts_nav.click()

    def open_more_contacts_page(self):
        contacts_link = self.browser.find_element(*MainPageLocators.MORE_CONTACTS)
        contacts_link.click()