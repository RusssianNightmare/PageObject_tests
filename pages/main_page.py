from .base_page import BasePage
from .locators import LoginPageLocators

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
    
    def login_as_standard_user(self):
        """Метод для авторизации стандартного пользователя на SauceDemo"""
        # Вводим имя пользователя
        username_input = self.browser.find_element(*LoginPageLocators.USERNAME_INPUT)
        username_input.send_keys("standard_user")
        
        # Вводим пароль
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys("secret_sauce")
        
        # Нажимаем кнопку логина
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()