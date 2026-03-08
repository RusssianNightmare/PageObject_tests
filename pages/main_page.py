# pages/main_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def should_be_login_form(self):
        """Проверяет наличие формы логина на главной странице"""
        assert self.is_element_present(*MainPageLocators.USERNAME_FIELD), "Поле username не найдено"
        assert self.is_element_present(*MainPageLocators.PASSWORD_FIELD), "Поле password не найдено"
        assert self.is_element_present(*MainPageLocators.LOGIN_BUTTON), "Кнопка логина не найдена"
        print("✅ Форма логина присутствует на главной странице")
    
    def login_as_standard_user(self):
        """Быстрая авторизация стандартного пользователя"""
        self.browser.find_element(*MainPageLocators.USERNAME_FIELD).send_keys("standard_user")
        self.browser.find_element(*MainPageLocators.PASSWORD_FIELD).send_keys("secret_sauce")
        self.browser.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        print("✅ Авторизация стандартного пользователя выполнена")