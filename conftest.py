import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox
import os

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--user_language', action='store', default="ru",
                     help="Choose language: eng or ru")


@pytest.fixture(scope="class")
def browser(request):
    user_language = request.config.getoption("user_language")

    options = Options()
    dir = f"{os.path.abspath(os.path.dirname(__file__))}\\downloaded_files"

    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("prefs", {"intl.accept_languages": user_language
                                                , "download.default_directory" : dir
                                                , 'download.prompt_for_download': False
                                                , 'download.directory_upgrade': True
                                                , 'safebrowsing.enabled': True})
    
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = OptionsFirefox()
        options.set_preference("intl.accept_languages", user_language)
        options.set_preference("download.default_directory", dir)
        options.set_preference("download.prompt_for_download", False)
        options.set_preference("download.directory_upgrade", True)
        options.set_preference("safebrowsing.enabled", True)
        
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()