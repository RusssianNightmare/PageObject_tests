import sys
import os
import pytest
from selenium.webdriver.common.by import By

# Добавляем путь к корневой директории проекта
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pages.login_page import LoginPage
from pages.locators import LoginPageLocators

class TestLoginPage:
    def test_guest_should_see_login_form(self, browser):
        """Тест проверяет наличие формы логина на главной странице"""
        link = "https://www.saucedemo.com/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_form()
        print("✅ Форма логина успешно проверена")

    def test_guest_can_login_with_valid_credentials(self, browser):
        """Тест проверяет успешную авторизацию с валидными данными"""
        link = "https://www.saucedemo.com/"
        page = LoginPage(browser, link)
        page.open()
        
        # Проверяем, что форма логина отображается
        page.should_be_login_form()
        
        # Выполняем авторизацию
        page.login_user("standard_user", "secret_sauce")
        
        # Проверяем, что авторизация прошла успешно
        page.should_be_authorized_user()
        print("✅ Успешная авторизация проверена")

    def test_guest_cannot_login_with_invalid_password(self, browser):
        """Тест проверяет, что с неправильным паролем авторизация не проходит"""
        link = "https://www.saucedemo.com/"
        page = LoginPage(browser, link)
        page.open()
        
        # Выполняем авторизацию с неправильным паролем
        page.login_user("standard_user", "wrong_password")
        
        # Проверяем, что появилось сообщение об ошибке
        assert page.is_element_present(*LoginPageLocators.ERROR_MESSAGE), "Сообщение об ошибке не появилось"
        error_text = browser.find_element(*LoginPageLocators.ERROR_MESSAGE).text
        assert "Epic sadface" in error_text, f"Неожиданный текст ошибки: {error_text}"
        
        # Проверяем, что мы остались на странице логина
        assert "inventory" not in browser.current_url, "Произошел переход на страницу инвентаря"
        print("✅ Неверный пароль обработан корректно")

    def test_guest_cannot_login_with_invalid_username(self, browser):
        """Тест проверяет, что с неправильным username авторизация не проходит"""
        link = "https://www.saucedemo.com/"
        page = LoginPage(browser, link)
        page.open()
        
        # Выполняем авторизацию с неправильным username
        page.login_user("wrong_user", "secret_sauce")
        
        # Проверяем, что появилось сообщение об ошибке
        assert page.is_element_present(*LoginPageLocators.ERROR_MESSAGE), "Сообщение об ошибке не появилось"
        print("✅ Неверный username обработан корректно")

    def test_guest_cannot_login_with_empty_fields(self, browser):
        """Тест проверяет, что с пустыми полями авторизация не проходит"""
        link = "https://www.saucedemo.com/"
        page = LoginPage(browser, link)
        page.open()
        
        # Пытаемся авторизоваться с пустыми полями
        page.login_user("", "")
        
        # Проверяем, что появилось сообщение об ошибке
        assert page.is_element_present(*LoginPageLocators.ERROR_MESSAGE), "Сообщение об ошибке не появилось"
        print("✅ Пустые поля обработаны корректно")

    @pytest.mark.parametrize('username', [
        'standard_user',
        'locked_out_user',
        'problem_user',
        'performance_glitch_user'
    ])
    def test_different_users_can_see_login_page(self, browser, username):
        """Тест проверяет, что разные пользователи видят страницу логина"""
        link = "https://www.saucedemo.com/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_form()
        print(f"✅ Пользователь {username} видит форму логина")