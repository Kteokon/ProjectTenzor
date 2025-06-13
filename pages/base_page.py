# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException

# class BasePage():
#     url = ""

#     def __init__(self, browser, timeout=10):
#         self.browser = browser
#         self.browser.implicitly_wait(timeout)
#         assert self.url != ""
    
#     def is_appeared(self, how, what, timeout=4):
#         try:
#             WebDriverWait(self.browser, timeout, 1, TimeoutException).\
#                 until(EC.presence_of_element_located((how, what)))
#         except TimeoutException:
#             return False
#         return True
    
#     def is_clickable(self, how, what, timeout=4):
#         try:
#             WebDriverWait(self.browser, timeout, 1, TimeoutException).\
#                 until(EC.element_to_be_clickable((how, what)))
#         except TimeoutException:
#             return False
#         return True
    
#     def wait_to_be_clickable(self, how, what, timeout=4):
#         try:
#             WebDriverWait(self.browser, timeout, 1, TimeoutException).\
#                 until(EC.element_to_be_clickable((how, what)))
#         except TimeoutException:
#             return False

#         return True

#     def is_element_present(self, how, what):
#         try:
#             self.browser.find_element(how, what)
#         except (NoSuchElementException):
#             return False
#         return True

#     def is_element_present_by_name(self, name, how, what):
#         try:
#             self.browser.find_element(how, what)
#         except (NoSuchElementException):
#             return False
#         return True

#     def open(self):
#         self.browser.get(self.url)

#     def scroll(self, what):
#         self.browser.execute_script("return arguments[0].scrollIntoView(true);", what)

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage():
    url = ""    

    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        assert self.url != ""

    def is_appeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_new_text(self, text, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.text_to_be_present_in_element((how, what), text))
        except TimeoutException:
            return False
        return True

    def open(self):
        self.browser.get(self.url)

    def scroll(self, what):
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", what)