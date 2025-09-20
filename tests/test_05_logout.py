import time

from utilities.test_data import TestData


class TestLogout:

    def test_logout_functionality(self, driver, inventory_page):
        inventory_page.logout()
        time.sleep(3)

        assert TestData.BASE_URL == driver.current_url