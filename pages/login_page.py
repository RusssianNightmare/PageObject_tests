from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
    
    def should_be_login_url(self):
        # Проверяем, что мы на странице логина SauceDemo
        assert "saucedemo.com" in self.browser.current_url, "This is not a saucedemo login page"
    
    def should_be_login_form(self):
        # Проверяем наличие формы логина на SauceDemo
        assert self.is_element_present(*LoginPageLocators.USERNAME_INPUT), "Username input is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_INPUT), "Password input is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"
    
    def login_user(self, username, password):
        """Метод для авторизации пользователя на SauceDemo"""
        # Вводим имя пользователя
        username_input = self.browser.find_element(*LoginPageLocators.USERNAME_INPUT)
        username_input.clear()
        username_input.send_keys(username)
        
        # Вводим пароль
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)
        
        # Нажимаем кнопку логина
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()
    
    def should_be_authorized_user(self):
        """Проверяем, что пользователь авторизован (находится на странице инвентаря)"""
        assert "inventory" in self.browser.current_url, "User is not authorized - not on inventory page"