# pages/inventory_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import InventoryPageLocators

class InventoryPage(BasePage):
    def should_be_inventory_page(self):
        """Проверка, что мы на странице инвентаря"""
        assert "inventory" in self.browser.current_url, "Это не страница инвентаря"
        assert self.is_element_present(*InventoryPageLocators.INVENTORY_CONTAINER), "Контейнер инвентаря не найден"
        print("✅ Находимся на странице инвентаря")
    
    def should_be_items_present(self):
        """Проверка наличия товаров"""
        items = self.browser.find_elements(*InventoryPageLocators.INVENTORY_ITEM)
        assert len(items) > 0, "Товары не найдены"
        print(f"✅ Найдено товаров: {len(items)}")
        return items
    
    def add_first_item_to_cart(self):
        """Добавление первого товара в корзину"""
        items = self.browser.find_elements(*InventoryPageLocators.INVENTORY_ITEM)
        if items:
            add_button = items[0].find_element(*InventoryPageLocators.ADD_TO_CART_BUTTON)
            add_button.click()
            print("✅ Первый товар добавлен в корзину")
    
    def should_be_cart_badge_with_count(self, expected_count):
        """Проверка счетчика корзины"""
        cart_badge = self.browser.find_element(*InventoryPageLocators.CART_BADGE)
        assert cart_badge.text == str(expected_count), f"Ожидалось {expected_count}, получено {cart_badge.text}"
        print(f"✅ В корзине {expected_count} товар(ов)")