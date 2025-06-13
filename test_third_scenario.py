from pages.main_page import MainPage
from pages.download_page import DownloadPage
import os
import time

class TestSecondScenario():
    LINK_NAME = "Скачать локальные версии"
    LEFT_TAB_NAME = "Saby Desktop"
    UPPER_TAB_NAME = "Windows"
    DOWNLOAD_NAME = "Веб-установщик"

    def test_download_file(self, browser):
        # main_page = MainPage(browser)
        # main_page.open()
        # main_page.should_be_download_link()
        # download_link = main_page.get_download_link()
        # main_page.scroll(download_link)
        # main_page.open_download_link()

        download_page = DownloadPage(browser)
        download_page.open()
        download_page.should_be_left_tab(self.LEFT_TAB_NAME)
        download_page.switch_left_tab(self.LEFT_TAB_NAME)
        download_page.should_be_upper_tab(self.UPPER_TAB_NAME)
        download_page.switch_upper_tab(self.UPPER_TAB_NAME)
        download_page.should_be_download_link(self.DOWNLOAD_NAME)

        dir = f"{os.path.abspath(os.path.dirname(__file__))}\\files\\"
        file_name = dir + download_page.get_file_name(self.DOWNLOAD_NAME)
        print(file_name)
        if os.path.exists(file_name):
            os.remove(file_name)
        
        file_size = download_page.get_file_size(self.DOWNLOAD_NAME)
        download_page.click_download(self.DOWNLOAD_NAME)
        self.wait_for_download(file_name)
        self.check_size(file_name, file_size)

    def wait_for_download(self, file_name, timeout=60):
        print(file_name)
        start_time = time.time()
        while not os.path.exists(file_name):
            if time.time() - start_time > timeout:
                raise TimeoutError(f'Download timeout: {file_name}')
            time.sleep(1)
        return True
    
    def check_size(self, file_name, file_size):
        downloaded_file_size = os.path.getsize(file_name)
        assert f"{(downloaded_file_size / 1024 / 1024):.2f}" == str(file_size), "Размер файла, указанный на сайте, не совпадает с размером скачанного файла"
