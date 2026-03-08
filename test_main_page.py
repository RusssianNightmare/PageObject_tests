# test_main_page.py
import sys
import os
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from pages.main_page import MainPage

def test_guest_can_see_login_form_on_main_page(browser):
    """Тест проверяет наличие формы логина на главной странице"""
    link = "https://www.saucedemo.com/"
    page = MainPage(browser, link)
    page.open()
    
    # Проверяем наличие формы логина
    page.should_be_login_form()
    
    print("✅ Форма логина отображается на главной странице")

def test_guest_can_login_from_main_page(browser):
    """Тест проверяет возможность авторизации с главной страницы"""
    link = "https://www.saucedemo.com/"
    page = MainPage(browser, link)
    page.open()
    
    # Выполняем авторизацию
    page.login_as_standard_user()
    
    # Проверяем, что мы на странице инвентаря
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    
    # Проверяем URL
    assert "inventory" in browser.current_url, "Переход на страницу инвентаря не произошел"
    
    # Проверяем наличие товаров
    items = browser.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(items) > 0, "Товары не отображаются"
    
    print("✅ Авторизация выполнена успешно, открыта страница инвентаря")