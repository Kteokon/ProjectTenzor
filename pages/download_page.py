from pages.base_page import BasePage
from pages.locators import DownloadPageLocators
import re

class DownloadPage(BasePage):
    url = "https://saby.ru/download/"
    
    def should_be_download_link(self, name):
        assert self.is_element_present(*DownloadPageLocators.get_download(name)), f"Отсутствует файл \"{name}\""

    def should_be_left_tab(self, tab_name):
        assert self.is_element_present(*DownloadPageLocators.get_left_tab_by_name(tab_name)), f"Отсутствует вкладка {tab_name}"

    def should_be_upper_tab(self, tab_name):
        assert self.is_element_present(*DownloadPageLocators.get_upper_tab_by_name(tab_name)), f"Отсутствует вкладка {tab_name}"

    def click_download(self, name):
        download = self.browser.find_element(*DownloadPageLocators.get_download(name))
        download.click()

    def get_file_size(self, name):
        download = self.browser.find_element(*DownloadPageLocators.get_download(name))
        file_size = re.findall("\d+\.\d+", download.text)[0]
        return file_size

    def get_file_name(self, name):
        download = self.browser.find_element(*DownloadPageLocators.get_download(name))
        file_name = download.get_attribute("href").split("/")[-1]
        return file_name

    def switch_left_tab(self, tab_name):
        tab = self.browser.find_element(*DownloadPageLocators.get_left_tab_by_name(tab_name))
        tab.click()

    def switch_upper_tab(self, tab_name):
        tab = self.browser.find_element(*DownloadPageLocators.get_upper_tab_by_name(tab_name))
        tab.click()