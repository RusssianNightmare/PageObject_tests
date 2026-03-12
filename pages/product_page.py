from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
    
    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text
    
    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text
    
    def get_product_name_in_success_message(self):
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        return success_message.text
    
    def get_basket_total_price(self):
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE)
        return basket_total.text
    
    def should_be_success_message_with_product_name(self, expected_product_name):
        actual_product_name = self.get_product_name_in_success_message()
        assert actual_product_name == expected_product_name, \
            f"Product name in success message '{actual_product_name}' doesn't match expected '{expected_product_name}'"
    
    def should_be_basket_total_equal_product_price(self, expected_price):
        actual_basket_total = self.get_basket_total_price()
        assert actual_basket_total == expected_price, \
            f"Basket total '{actual_basket_total}' doesn't match product price '{expected_price}'"
    
    def solve_quiz_and_get_code_for_product(self):
        self.solve_quiz_and_get_code()
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
    
    def should_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"
    
    def should_be_success_message_present(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented"