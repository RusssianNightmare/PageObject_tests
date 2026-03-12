from .base_page import BasePage
from .locators import InventoryPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage(BasePage):
    def should_be_inventory_page(self):
        self.should_be_inventory_url()
        self.should_be_inventory_container()
    
    def should_be_inventory_url(self):
        assert "inventory" in self.browser.current_url, "This is not an inventory page"
    
    def should_be_inventory_container(self):
        assert self.is_element_present(*InventoryPageLocators.INVENTORY_CONTAINER), "Inventory container is not presented"
    
    def should_be_items_present(self):
        assert self.is_element_present(*InventoryPageLocators.INVENTORY_ITEMS), "No inventory items presented"
    
    def add_first_item_to_cart(self):
        add_button = self.browser.find_element(*InventoryPageLocators.ADD_TO_CART_BUTTON_FIRST)
        add_button.click()
    
    def should_be_cart_badge_with_count(self, expected_count):
        assert self.is_element_present(*InventoryPageLocators.CART_BADGE), "Cart badge is not presented"
        badge_text = self.browser.find_element(*InventoryPageLocators.CART_BADGE).text
        assert badge_text == str(expected_count), f"Cart count is {badge_text}, expected {expected_count}"
    
    def go_to_cart(self):
        cart_link = self.browser.find_element(*InventoryPageLocators.CART_LINK)
        cart_link.click()