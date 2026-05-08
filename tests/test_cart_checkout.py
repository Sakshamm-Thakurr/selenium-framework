import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class TestCartAndCheckout:

    def setup_method(self):
        self.login_page = LoginPage()
        self.login_page.open()
        self.login_page.login("standard_user", "secret_sauce")
        assert self.login_page.is_logged_in()
        self.driver = self.login_page.driver
        self.inventory = InventoryPage(self.driver)
        self.cart = CartPage(self.driver)
        self.checkout = CheckoutPage(self.driver)

    def teardown_method(self):
        self.login_page.quit()

    # --- CART TESTS ---

    def test_cart_empty_initially(self):
        """Cart shuru mein empty honi chahiye"""
        self.inventory.go_to_cart()
        assert self.cart.get_cart_item_count() == 0

    def test_add_item_appears_in_cart(self):
        """Add kiya item cart mein dikhna chahiye"""
        self.inventory.add_first_item_to_cart()
        self.inventory.go_to_cart()
        assert self.cart.get_cart_item_count() == 1

    def test_remove_item_from_cart(self):
        """Cart se item remove hona chahiye"""
        self.inventory.add_first_item_to_cart()
        self.inventory.go_to_cart()
        self.cart.remove_first_item()
        assert self.cart.get_cart_item_count() == 0

    def test_multiple_items_in_cart(self):
        """Multiple items cart mein add ho sakti hain"""
        self.inventory.add_all_items_to_cart()
        self.inventory.go_to_cart()
        assert self.cart.get_cart_item_count() == 6

    def test_continue_shopping_redirects(self):
        """Continue Shopping se wapas inventory pe aana chahiye"""
        self.inventory.go_to_cart()
        self.cart.continue_shopping()
        assert "inventory" in self.driver.current_url

    def test_cart_item_names_not_empty(self):
        """Cart items ke naam empty nahi hone chahiye"""
        self.inventory.add_first_item_to_cart()
        self.inventory.go_to_cart()
        names = self.cart.get_item_names()
        assert all(name != "" for name in names)

    # --- CHECKOUT TESTS ---

    def test_checkout_with_valid_info(self):
        """Valid info se checkout complete hona chahiye"""
        self.inventory.add_first_item_to_cart()
        self.inventory.go_to_cart()
        self.cart.click_checkout()
        self.checkout.fill_info("Saksham", "Thakur", "140001")
        self.checkout.click_continue()
        self.checkout.click_finish()
        success = self.checkout.get_success_message()
        assert "Thank you" in success

    def test_checkout_empty_firstname(self):
        """Empty first name pe error aana chahiye"""
        self.inventory.add_first_item_to_cart()
        self.inventory.go_to_cart()
        self.cart.click_checkout()
        self.checkout.fill_info("", "Thakur", "140001")
        self.checkout.click_continue()
        assert self.checkout.get_error() != ""

    def test_checkout_empty_lastname(self):
        """Empty last name pe error aana chahiye"""
        self.inventory.add_first_item_to_cart()
        self.inventory.go_to_cart()
        self.cart.click_checkout()
        self.checkout.fill_info("Saksham", "", "140001")
        self.checkout.click_continue()
        assert self.checkout.get_error() != ""

    def test_checkout_empty_postal(self):
        """Empty postal code pe error aana chahiye"""
        self.inventory.add_first_item_to_cart()
        self.inventory.go_to_cart()
        self.cart.click_checkout()
        self.checkout.fill_info("Saksham", "Thakur", "")
        self.checkout.click_continue()
        assert self.checkout.get_error() != ""

    def test_checkout_cancel_returns_to_cart(self):
        """Cancel karne pe cart pe wapas aana chahiye"""
        self.inventory.add_first_item_to_cart()
        self.inventory.go_to_cart()
        self.cart.click_checkout()
        self.checkout.cancel()
        assert "cart" in self.driver.current_url

    def test_order_total_visible(self):
        """Checkout summary mein total dikhna chahiye"""
        self.inventory.add_first_item_to_cart()
        self.inventory.go_to_cart()
        self.cart.click_checkout()
        self.checkout.fill_info("Saksham", "Thakur", "140001")
        self.checkout.click_continue()
        total = self.checkout.get_total()
        assert "Total" in total