from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    FINISH_BUTTON = (By.ID, "finish")
    CANCEL_BUTTON = (By.ID, "cancel")

    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")

    def enter_first_name(self, first_name):
        self.set_value(self.FIRST_NAME_FIELD, first_name)

    def enter_last_name(self, last_name):
        self.set_value(self.LAST_NAME_FIELD, last_name)

    def enter_postal_code(self, postal_code):
        self.set_value(self.POSTAL_CODE_FIELD, postal_code)

    def click_continue(self):
        self.click_element(self.CONTINUE_BUTTON)

    def fill_checkout_information(self, first_name, last_name, postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        self.click_continue()

    def click_finish(self):
        self.click_element(self.FINISH_BUTTON)

    def get_success_message(self):
        return self.get_value(self.SUCCESS_MESSAGE)

    def is_on_checkout_step_one(self):
        return "checkout-step-one.html" in self.driver.current_url

    def is_on_checkout_step_two(self):
        return "checkout-step-two.html" in self.driver.current_url

    def is_on_checkout_complete(self):
        return "checkout-complete.html" in self.driver.current_url
