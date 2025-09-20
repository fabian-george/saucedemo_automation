import time


class TestCartOperations:

    def test_add_three_products_to_cart(self, driver, inventory_page):
        inventory_page.add_multiple_products_to_cart(3)
        time.sleep(3)

        cart_count = inventory_page.get_cart_count()
        assert cart_count == 3, f"Expected 3 items in cart, but found {cart_count}"

    def test_remove_second_product_from_cart(self, inventory_page):
        inventory_page.add_multiple_products_to_cart(3)
        time.sleep(3)

        cart_page = inventory_page.click_cart()
        assert cart_page.is_on_cart_page()
        time.sleep(3)

        initial_count = cart_page.get_cart_items_count()
        assert initial_count == 3, "Expected 3 items in cart initially"
        time.sleep(3)

        cart_page.remove_item_by_index(1)
        time.sleep(3)

        final_count = cart_page.get_cart_items_count()
        assert final_count == 2, f"Expected 2 items after removal, but found {final_count}"
