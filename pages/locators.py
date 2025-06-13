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
    CURRENT_CONTACTS_LIST = (By.CLASS_NAME, "sbisru-Contacts-List__col-1")
    REGION_PANEL = (By.CLASS_NAME, "sbis_ru-Region-Panel__container")
    @staticmethod
    def get_region_by_name(region_name):
        return (By.XPATH, f"//*[@class=\"sbis_ru-link\"][@title=\"{region_name}\"]")

class TensorMainPageLocators():
    # CONTAINERS = (By.CSS_SELECTOR, ".tensor_ru-container.tensor_ru-section")
    POWER = (By.XPATH, "//*[@class=\"tensor_ru-container tensor_ru-section\"]//p[text()=\"Сила в людях\"]")
    # POWER = (By.XPATH, "//p[text()=\"Сила в людях\"]")
    MORE_INFO = (By.XPATH, "//*[@class=\"tensor_ru-container tensor_ru-section\"]//p[text()=\"Сила в людях\"]/parent::*//a[text()=\"Подробнее\"]")#(By.CSS_SELECTOR, "a[href=\"/about\"]")

class MoreInfoPageLocators():
    WORKING = (By.XPATH, "//h2[text()=\"Работаем\"]")
    PHOTOS = (By.XPATH, "//h2[text()=\"Работаем\"]/parent::*/following-sibling::div[1]//img")
    # PHOTO = (By.TAG_NAME, "img")