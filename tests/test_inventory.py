import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

class TestInventory:

    def setup_method(self):
        self.login_page = LoginPage()
        self.login_page.open()
        self.login_page.login("standard_user", "secret_sauce")
        assert self.login_page.is_logged_in()
        self.inventory = InventoryPage(self.login_page.driver)

    def teardown_method(self):
        self.login_page.quit()

    def test_products_visible(self):
        """6 products dikhne chahiye"""
        items = self.inventory.get_all_items()
        assert len(items) == 6, f"Expected 6 items, got {len(items)}"

    def test_add_one_item_to_cart(self):
        """Ek item add karne pe cart count 1 hona chahiye"""
        self.inventory.add_first_item_to_cart()
        assert self.inventory.get_cart_count() == 1

    def test_add_all_items_to_cart(self):
        """Sab items add karne pe cart count 6 hona chahiye"""
        self.inventory.add_all_items_to_cart()
        assert self.inventory.get_cart_count() == 6

    def test_product_names_not_empty(self):
        """Kisi bhi product ka naam empty nahi hona chahiye"""
        names = self.inventory.get_item_names()
        assert all(name != "" for name in names)

    def test_product_prices_positive(self):
        """Sab prices positive honi chahiye"""
        prices = self.inventory.get_item_prices()
        assert all(price > 0 for price in prices)

    def test_sort_by_price_low_to_high(self):
        """Price low to high sort sahi kaam kare"""
        self.inventory.sort_by("lohi")
        prices = self.inventory.get_item_prices()
        assert prices == sorted(prices), "Prices sorted nahi hain"

    def test_sort_by_price_high_to_low(self):
        """Price high to low sort sahi kaam kare"""
        self.inventory.sort_by("hilo")
        prices = self.inventory.get_item_prices()
        assert prices == sorted(prices, reverse=True)

    def test_sort_by_name_a_to_z(self):
        """Name A-Z sort sahi kaam kare"""
        self.inventory.sort_by("az")
        names = self.inventory.get_item_names()
        assert names == sorted(names)

    def test_logout_works(self):
        """Logout karne pe login page pe aana chahiye"""
        self.inventory.logout()
        assert "saucedemo.com" in self.login_page.driver.current_url