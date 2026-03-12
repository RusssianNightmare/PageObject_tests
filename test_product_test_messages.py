import pytest
import sys
import os

# Добавляем текущую директорию в путь поиска модулей
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pages.product_page import ProductPage

import time
class TestProductPageMessages():
    
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # Открываем страницу товара
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        
        # Добавляем товар в корзину
        page.add_product_to_basket()
        
        # Проверяем, что нет сообщения об успехе
        page.should_not_be_success_message()
    
    def test_guest_cant_see_success_message(self, browser):
        # Открываем страницу товара
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        
        # Проверяем, что нет сообщения об успехе (до добавления в корзину)
        page.should_not_be_success_message()
    
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # Открываем страницу товара
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        
        # Добавляем товар в корзину
        page.add_product_to_basket()
        
        # Проверяем, что сообщение об успехе исчезло
        page.should_be_success_message_disappeared() 
