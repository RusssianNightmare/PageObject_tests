# test_main_page.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage

def test_saucedemo_inventory(browser):
    """Тест проверяет авторизацию, наличие товаров и работу корзины"""
    # 1. Открываем страницу логина
    browser.get("https://www.saucedemo.com/")

    # 2. Быстрая авторизация
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    # 3. Ждём загрузки инвентаря и проверяем
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    # 4. Простая проверка: есть ли товары?
    items = browser.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(items) > 0, "Товары не найдены!"

    # 5. Добавляем первый товар в корзину
    first_item = items[0]
    first_item.find_element(By.CSS_SELECTOR, ".btn_inventory").click()

    # 6. Проверяем корзину
    cart_badge = browser.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1", "Товар не добавился в корзину"

    print("✅ Тест пройден: авторизация, товары, корзина работают")

@pytest.mark.xfail(reason="Этот тест должен упасть с понятным сообщением об ошибке")
def test_guest_should_see_login_link(browser):
    """Тест проверяет наличие ссылки на логин (должен упасть)"""
    link = "https://www.saucedemo.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
# test_main_page.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage

def test_saucedemo_inventory(browser):
    """Тест проверяет авторизацию, наличие товаров и работу корзины"""
    # 1. Открываем страницу логина
    browser.get("https://www.saucedemo.com/")
    
    # 2. Быстрая авторизация
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    
    # 3. Ждём загрузки инвентаря и проверяем
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    
    # 4. Простая проверка: есть ли товары?
    items = browser.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(items) > 0, "Товары не найдены!"
    
    # 5. Добавляем первый товар в корзину
    first_item = items[0]
    first_item.find_element(By.CSS_SELECTOR, ".btn_inventory").click()
    
    # 6. Проверяем корзину
    cart_badge = browser.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1", "Товар не добавился в корзину"
    
    print("✅ Тест пройден: авторизация, товары, корзина работают")

@pytest.mark.xfail(reason="Этот тест должен упасть с понятным сообщением об ошибке")
def test_guest_should_see_login_link(browser):
    """Тест проверяет наличие ссылки на логин (должен упасть)"""
    link = "https://www.saucedemo.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
