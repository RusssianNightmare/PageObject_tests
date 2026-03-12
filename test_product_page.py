import pytest
import sys
import os
import time

# Добавляем путь к корневой директории проекта
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage

class TestUserAddToBasketFromProductPage():
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Открываем страницу регистрации
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        self.login_page = LoginPage(browser, link)
        self.login_page.open()
        
        # Генерируем email с использованием текущего времени
        email = str(time.time()) + "@fakemail.org"
        password = "testpassword123"
        
        # Регистрируем нового пользователя
        self.login_page.register_new_user(email, password)
        
        # Проверяем, что пользователь залогинен
        self.login_page.should_be_authorized_user()
        
        # Сохраняем browser для использования в тестах
        self.browser = browser
    
    def test_user_cant_see_success_message(self, browser):
        # Открываем страницу товара
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        
        # Проверяем, что нет сообщения об успехе
        page.should_not_be_success_message()
    
    def test_user_can_add_product_to_basket(self, browser):
        # Открываем страницу товара
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        
        # Получаем название и цену товара до добавления в корзину
        product_name = page.get_product_name()
        product_price = page.get_product_price()
        
        # Добавляем товар в корзину
        page.add_product_to_basket()
        
        # Проверяем, что название товара в сообщении совпадает с добавленным
        page.should_be_success_message_with_product_name(product_name)
        
        # Проверяем, что стоимость корзины совпадает с ценой товара
        page.should_be_basket_total_equal_product_price(product_price)


class TestProductPage():
    
    def test_guest_can_add_product_to_basket(self, browser):
        # Открываем страницу товара с промо-кодом
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        
        # Получаем название и цену товара до добавления в корзину
        product_name = page.get_product_name()
        product_price = page.get_product_price()
        
        # Добавляем товар в корзину
        page.add_product_to_basket()
        
        # Решаем математическое выражение и получаем проверочный код
        page.solve_quiz_and_get_code_for_product()
        
        # Проверяем, что название товара в сообщении совпадает с добавленным
        page.should_be_success_message_with_product_name(product_name)
        
        # Проверяем, что стоимость корзины совпадает с ценой товара
        page.should_be_basket_total_equal_product_price(product_price)
    
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
    
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
    
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        # Открываем страницу товара
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        
        # Переходим в корзину по кнопке в шапке сайта
        page.go_to_basket_page()
        
        # Создаем объект страницы корзины
        basket_page = BasketPage(browser, browser.current_url)
        
        # Ожидаем, что в корзине нет товаров
        basket_page.should_not_be_basket_items()
        
        # Ожидаем, что есть текст о том, что корзина пуста
        basket_page.should_be_basket_empty_message()