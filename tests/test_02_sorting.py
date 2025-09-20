import time

from utilities.test_data import TestData


class TestSorting:

    def test_sort_by_name_z_to_a(self, driver, inventory_page):
        inventory_page.sort_products(TestData.SORT_NAME_Z_TO_A)
        time.sleep(3)

        product_names = inventory_page.get_product_names()
        sorted_names = sorted(product_names, reverse=True)
        time.sleep(3)

        assert product_names == sorted_names, "Products are not sorted by name Z to A"

    def test_sort_by_price_high_to_low(self, driver, inventory_page):
        inventory_page.sort_products(TestData.SORT_PRICE_HIGH_TO_LOW)
        time.sleep(3)

        product_prices = inventory_page.get_product_prices()
        sorted_prices = sorted(product_prices, reverse=True)
        time.sleep(3)

        assert product_prices == sorted_prices, "Products are not sorted by price high to low"
