
class TestLogin:

    def test_login(self, driver, inventory_page):

        assert inventory_page.is_on_inventory_page()