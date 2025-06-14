from pages.main_page import MainPage
from pages.download_page import DownloadPage
import os
import time

def wait_for_download(file_path : str, timeout=60):
    """
    Ожидание загрузки указанного файла
    :param file_path: Полный путь к файлу
    :param timeout: Время, после которого надо выкинуть ошибку времени загрузки
    """
    start_time = time.time()
    while not os.path.exists(file_path):
        if time.time() - start_time > timeout:
            raise TimeoutError(f'Таймаут во время загрузки: {file_path}')
        time.sleep(1)
    return True

def check_size(file_name : str, file_size : float):
    """
    Проверка размера файла, находящегося по пути file_name, с ожидаемым размером
    :param file_name: Полный путь к файлу
    :param file_size: Ожидаемый размер файла
    """
    downloaded_file_size = os.path.getsize(file_name)
    assert f"{(downloaded_file_size / 1024 / 1024):.2f}" == str(file_size), "Размер файла, указанный на сайте, не совпадает с размером скачанного файла"

class TestThirdScenario():
    LINK_NAME = "Скачать локальные версии"
    LEFT_TAB_NAME = "Saby Desktop"
    UPPER_TAB_NAME = "Windows"
    DOWNLOAD_NAME = "Веб-установщик"

    @classmethod
    def setup_class(cls):
        """
        Удаление файлов с расширением exe из папки с загруженными файлами
        для упрощения отслежвания загрузки скачанного файла
        """
        file_path = f"{os.path.abspath(os.path.dirname(__file__))}\\downloaded_files"

        if os.path.exists(file_path):
            files = os.listdir(file_path)
            for file in files:
                if file.endswith(".exe"):
                    os.remove(f"{file_path}\\{file}") 

    def test_download_file(self, browser):
        # Поиск в футере "Скачать локальные версии", переход на страницу с загрузками
        main_page = MainPage(browser)
        main_page.open()
        main_page.should_be_download_link()
        download_link = main_page.get_download_link()
        main_page.scroll(download_link)
        main_page.open_download_link()

        # Проверка нахождения на верных вкладках и наличия возможности скачать нужный файл
        download_page = DownloadPage(browser)
        download_page.should_be_left_tab(self.LEFT_TAB_NAME)
        download_page.switch_left_tab(self.LEFT_TAB_NAME)
        download_page.should_be_upper_tab(self.UPPER_TAB_NAME)
        download_page.switch_upper_tab(self.UPPER_TAB_NAME)
        download_page.should_be_download_link(self.DOWNLOAD_NAME)

        # Скачивание файла, ожидание его загрузки и проверка размера файла с размером, указанным на сайта
        dir = f"{os.path.abspath(os.path.dirname(__file__))}\\downloaded_files"
        file_path = f"{dir}\\{download_page.get_file_name(self.DOWNLOAD_NAME)}"
        file_size = download_page.get_file_size(self.DOWNLOAD_NAME)
        download_page.download_file(self.DOWNLOAD_NAME)
        wait_for_download(file_path)
        check_size(file_path, file_size)