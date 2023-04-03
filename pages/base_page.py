from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .locators import MainPageLocators

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    def open(self): 
        print("Открытие сайта")
        self.browser.get(self.url)  
    def should_be_login_link(self):
        print("Проверка наличия ссылки на авторизыцию")
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
    def is_element_present(self, how, what):
        try:
           self.browser.find_element(how, what)
        except (NoSuchElementException):
           return False
        return True