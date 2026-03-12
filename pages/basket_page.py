from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_empty_message()
    
    def should_be_basket_url(self):
        # Проверяем, что мы на странице корзины
        assert "basket" in self.browser.current_url, "This is not a basket page"
    
    def should_be_basket_empty_message(self):
        # Проверяем, что есть текст о пустой корзине
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
            "Basket empty message is not presented"
        empty_message_text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text
        assert "empty" in empty_message_text.lower(), \
            f"Expected 'empty' in message, got '{empty_message_text}'"
    
    def should_not_be_basket_items(self):
        # Проверяем, что в корзине нет товаров
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket contains items, but should be empty"
    
    def should_be_basket_empty(self):
        # Комбинированная проверка пустой корзины
        self.should_not_be_basket_items()
        self.should_be_basket_empty_message() 
