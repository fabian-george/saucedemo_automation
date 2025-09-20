from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage


class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[id*='remove']")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")

    def get_cart_items_count(self):
        try:
            items = self.find_elements(self.CART_ITEMS)
            return len(items)
        except:
            return 0

    def remove_item_by_index(self, index):
        remove_buttons = self.find_elements(self.REMOVE_BUTTONS)
        if index < len(remove_buttons):
            remove_buttons[index].click()

    def click_checkout(self):
        self.click_element(self.CHECKOUT_BUTTON)
        if "checkout-step-one.html" in self.driver.current_url:
            return CheckoutPage(self.driver)
        return CheckoutPage(self.driver)

    def is_on_cart_page(self):
        return "cart.html" in self.driver.current_url
