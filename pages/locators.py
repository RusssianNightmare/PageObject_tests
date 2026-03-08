# pages/locators.py
from selenium.webdriver.common.by import By

class MainPageLocators():
    """Локаторы для главной страницы (страницы логина)"""
    LOGIN_BUTTON = (By.ID, "login-button")
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

class LoginPageLocators():
    """Локаторы для страницы логина (та же главная страница)"""
    LOGIN_FORM = (By.CSS_SELECTOR, ".login-box")
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

class InventoryPageLocators():
    """Локаторы для страницы инвентаря"""
    INVENTORY_CONTAINER = (By.CLASS_NAME, "inventory_container")
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")