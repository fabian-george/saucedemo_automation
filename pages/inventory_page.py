from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage
from pages.cart_page import CartPage


class InventoryPage(BasePage):
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button[id*='add-to-cart']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")

    def sort_products(self, sort_option):
        dropdown_element = self.find_element(self.SORT_DROPDOWN)
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text(sort_option)

    def add_multiple_products_to_cart(self, count=3):
        buttons = self.find_elements(self.ADD_TO_CART_BUTTONS)
        for i in range(min(count, len(buttons))):
            buttons[i].click()

    def get_cart_count(self):
        try:
            cart_badge = self.find_element(self.CART_BADGE)
            return int(cart_badge.text)
        except (NoSuchElementException, TimeoutException):
            return 0

    def click_cart(self):
        self.click_element(self.CART_LINK)

        if "cart.html" in self.driver.current_url:
            return CartPage(self.driver)
        else:
            return self

    def open_menu(self):
        self.click_element(self.MENU_BUTTON)

    def click_logout(self):
        self.click_element(self.LOGOUT_LINK)

    def logout(self):
        self.open_menu()
        self.click_logout()

    def get_product_names(self):
        elements = self.find_elements(self.PRODUCT_NAMES)
        return [element.text for element in elements]

    def get_product_prices(self):
        elements = self.find_elements(self.PRODUCT_PRICES)
        prices = []
        for element in elements:
            price_text = element.text.replace('$', '')
            prices.append(float(price_text))
        return prices

    def is_on_inventory_page(self):
        return "inventory.html" in self.driver.current_url
