from selenium.webdriver.common.by import By

class MainPageLocators():
    NAV_CONTACTS = (By.CSS_SELECTOR, ".sbisru-Header__menu-link.sbis_ru-Header__menu-link.sbisru-Header__menu-link--hover")
    MORE_CONTACTS = (By.CSS_SELECTOR, "a[href=\"/contacts\"]")

class ContactsPageLocators():
    TENSOR_LINK = (By.CSS_SELECTOR, ".s-Grid-container a[title=\"tensor.ru\"]")
    @staticmethod
    def get_header_region_by_name(region_name):
        return (By.XPATH, f"//div[@class=\"sbis_ru-container sbisru-Contacts__relative\"]//*[@class=\"sbis_ru-Region-Chooser__text sbis_ru-link\"][text()=\"{region_name}\"]")
    CURRENT_REGION = (By.CSS_SELECTOR, "div.sbis_ru-container.sbisru-Contacts__relative .sbis_ru-Region-Chooser__text.sbis_ru-link")
    CURRENT_CONTACTS_LIST = (By.CSS_SELECTOR, "#contacts_list [name=\"itemsContainer\"]")
    REGION_PANEL = (By.CLASS_NAME, "sbis_ru-Region-Panel__container")
    @staticmethod
    def get_region_by_name(region_name):
        return (By.XPATH, f"//*[@class=\"sbis_ru-link\"][@title=\"{region_name}\"]")
    SEARCH_INPUT = (By.XPATH, "//*[contains(@class, \"sbis_ru-Region-Panel__container\")]//div[contains(@class, \"sbis_ru-Region-Panel__search\")]")

class TensorMainPageLocators():
    @staticmethod
    def get_block_by_name(block_name):
        return (By.XPATH, f"//*[@class=\"tensor_ru-container tensor_ru-section\"]//p[text()=\"{block_name}\"]/..")
    MORE_INFO = (By.XPATH, ".//a[text()=\"Подробнее\"]")

class MoreInfoPageLocators():
    @staticmethod
    def get_block_by_name(block_name):
        return (By.XPATH, f"//h2[text()=\"{block_name}\"]/..")
    PICTURES = (By.XPATH, "./following-sibling::div[1]//img")