# pages/login_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        """Комплексная проверка страницы логина"""
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_error_message_not_present()

    def should_be_login_url(self):
        """Проверка URL страницы логина"""
        current_url = self.browser.current_url
        assert "saucedemo.com" in current_url, f"Страница {current_url} не является страницей saucedemo"
        assert "inventory" not in current_url, "Мы уже на странице инвентаря, а не на странице логина"

    def should_be_login_form(self):
        """Проверка наличия формы логина"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма логина не найдена на странице"
        assert self.is_element_present(*LoginPageLocators.USERNAME_FIELD), "Поле ввода username не найдено"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_FIELD), "Поле ввода password не найдено"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Кнопка логина не найдена"
        print("✅ Форма логина присутствует на странице")

    def should_be_error_message_not_present(self):
        """Проверка отсутствия сообщения об ошибке"""
        assert not self.is_element_present(*LoginPageLocators.ERROR_MESSAGE), "Присутствует сообщение об ошибке"

    def login_user(self, username, password):
        """Метод для авторизации пользователя"""
        self.browser.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys(username)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        print(f"✅ Авторизация выполнена: {username}")

    def should_be_authorized_user(self):
        """Проверка успешной авторизации"""
        assert self.is_element_present(By.CLASS_NAME, "inventory_container"), "Страница инвентаря не загрузилась"
        assert "inventory" in self.browser.current_url, "URL не соответствует странице инвентаря"
        print("✅ Пользователь успешно авторизован")