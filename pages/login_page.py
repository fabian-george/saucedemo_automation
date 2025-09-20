from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.inventory_page import InventoryPage
from utilities.test_data import TestData


class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def open_page(self):
        self.driver.get(TestData.BASE_URL)

    def enter_username(self, username):
        self.set_value(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.set_value(self.PASSWORD_FIELD, password)

    def click_login_button(self):
        self.click_element(self.LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

        if "inventory.html" in self.driver.current_url:
            return InventoryPage(self.driver)
        else:
            return self

    def get_error_message(self):
        return self.get_value(self.ERROR_MESSAGE)
