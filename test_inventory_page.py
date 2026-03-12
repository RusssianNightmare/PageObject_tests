import sys
import os
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Добавляем путь к корневой директории проекта
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pages.main_page import MainPage
from pages.inventory_page import InventoryPage

def test_inventory_page_after_login(browser):
    """Тест проверяет страницу инвентаря после авторизации"""
    link = "https://www.saucedemo.com/"
    
    # Авторизуемся через главную страницу
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.login_as_standard_user()
    
    # Ждем загрузки страницы инвентаря
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    
    # Переходим к странице инвентаря
    inventory_page = InventoryPage(browser, browser.current_url)
    
    # Проверяем страницу инвентаря
    inventory_page.should_be_inventory_page()
    inventory_page.should_be_items_present()
    
    # Добавляем товар в корзину
    inventory_page.add_first_item_to_cart()
    inventory_page.should_be_cart_badge_with_count(1)
    
    print("✅ Все проверки страницы инвентаря пройдены")