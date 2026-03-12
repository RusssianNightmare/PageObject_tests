import pytest
import sys
import os

# Добавляем путь к корневой директории проекта
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pages.main_page import MainPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage

import time

class TestMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
    
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
    
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        # Открываем главную страницу
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        
        # Переходим в корзину по кнопке в шапке сайта
        page.go_to_basket_page()
        
        # Создаем объект страницы корзины
        basket_page = BasketPage(browser, browser.current_url)
        
        # Ожидаем, что в корзине нет товаров
        basket_page.should_not_be_basket_items()
        
        # Ожидаем, что есть текст о том, что корзина пуста
        basket_page.should_be_basket_empty_message()