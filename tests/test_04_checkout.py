import time

from utilities.test_data import TestData


class TestCheckout:

    def test_successful_checkout_process(self, driver, inventory_page):
        inventory_page.add_multiple_products_to_cart(3)
        time.sleep(3)

        cart_page = inventory_page.click_cart()
        assert cart_page.is_on_cart_page()

        cart_page.remove_item_by_index(1)
        time.sleep(3)

        checkout_page = cart_page.click_checkout()
        assert checkout_page.is_on_checkout_step_one()
        time.sleep(3)

        checkout_page.fill_checkout_information(
            TestData.FIRST_NAME,
            TestData.LAST_NAME,
            TestData.POSTAL_CODE
        )
        time.sleep(3)

        assert checkout_page.is_on_checkout_step_two()

        checkout_page.click_finish()
        time.sleep(3)

        assert checkout_page.is_on_checkout_complete()
        success_message = checkout_page.get_success_message()
        assert TestData.SUCCESS_MESSAGE in success_message
