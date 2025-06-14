from selenium.webdriver.common.by import By

class MainPageLocators():
    NAV_CONTACTS = (By.CSS_SELECTOR, ".sbisru-Header__menu-link.sbis_ru-Header__menu-link.sbisru-Header__menu-link--hover")
    MORE_CONTACTS = (By.CSS_SELECTOR, "a[href=\"/contacts\"]")
    DOWNLOAD = (By.XPATH, "//*[@class=\"sbisru-Footer__container\"]//a[@class=\"sbisru-Footer__link\"][text()=\"Скачать локальные версии\"]")

class ContactsPageLocators():
    TENSOR_LINK = (By.CSS_SELECTOR, ".s-Grid-container a[title=\"tensor.ru\"]")
    CURRENT_REGION = (By.CSS_SELECTOR, "div.sbis_ru-container.sbisru-Contacts__relative .sbis_ru-Region-Chooser__text.sbis_ru-link")
    CURRENT_CONTACTS_LIST = (By.CSS_SELECTOR, "#contacts_list [name=\"itemsContainer\"]")
    REGION_PANEL = (By.CLASS_NAME, "sbis_ru-Region-Panel__container")
    SEARCH_INPUT = (By.XPATH, "//*[contains(@class, \"sbis_ru-Region-Panel__container\")]//div[contains(@class, \"sbis_ru-Region-Panel__search\")]")
    @staticmethod
    def get_region_by_name(region_name):
        return (By.XPATH, f"//*[@class=\"sbis_ru-link\"][@title=\"{region_name}\"]")
    @staticmethod
    def get_header_region_by_name(region_name):
        return (By.XPATH, f"//div[@class=\"sbis_ru-container sbisru-Contacts__relative\"]//*[@class=\"sbis_ru-Region-Chooser__text sbis_ru-link\"][text()=\"{region_name}\"]")

class TensorMainPageLocators():
    MORE_INFO = (By.XPATH, ".//a[text()=\"Подробнее\"]")
    @staticmethod
    def get_block_by_name(block_name):
        return (By.XPATH, f"//*[@class=\"tensor_ru-container tensor_ru-section\"]//p[text()=\"{block_name}\"]/..")

class MoreInfoPageLocators():
    PICTURES = (By.XPATH, "./following-sibling::div[1]//img")
    @staticmethod
    def get_block_by_name(block_name):
        return (By.XPATH, f"//h2[text()=\"{block_name}\"]/..")

class DownloadPageLocators():
    @staticmethod
    def get_left_tab_by_name(tab_name):
        return (By.XPATH, f"//div[@class=\"sbis_ru-VerticalTabs__left\"]//div[text()=\"{tab_name}\"]")
    @staticmethod
    def get_upper_tab_by_name(tab_name):
        return (By.XPATH, f"//div[@class=\"controls-TabControl-tabButtons\"]//span[text()=\"{tab_name}\"]")
    @staticmethod
    def get_download(name):
        return (By.XPATH, f"//h3[contains(text(),\"{name}\")]/../following-sibling::div[1]//a")