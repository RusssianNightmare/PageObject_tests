from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    
    def open(self):
        self.browser.get(self.url)
    
    def is_element_present(self, how, what):
        """
        Проверяет наличие элемента на странице
        how: способ поиска (By.ID, By.CSS_SELECTOR и т.д.)
        what: селектор элемента
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True