import pytest
from pages.login_page import LoginPage

class TestLogin:
    
    def setup_method(self):
        self.login_page = LoginPage()
        self.login_page.open()

    def teardown_method(self):
        self.login_page.quit()

    def test_valid_login(self):
        """Valid credentials se login hona chahiye"""
        self.login_page.login("standard_user", "secret_sauce")
        assert self.login_page.is_logged_in(), "Login failed with valid credentials"

    def test_invalid_password(self):
        """Wrong password pe error aana chahiye"""
        self.login_page.login("standard_user", "wrong_password")
        error = self.login_page.get_error_message()
        assert error != "", "Error message nahi aaya invalid password pe"

    def test_invalid_username(self):
        """Wrong username pe error aana chahiye"""
        self.login_page.login("wrong_user", "secret_sauce")
        error = self.login_page.get_error_message()
        assert error != "", "Error message nahi aaya invalid username pe"

    def test_empty_credentials(self):
        """Empty fields pe error aana chahiye"""
        self.login_page.login("", "")
        error = self.login_page.get_error_message()
        assert error != "", "Error message nahi aaya empty credentials pe"

    def test_locked_out_user(self):
        """Locked user ko login nahi hone dena chahiye"""
        self.login_page.login("locked_out_user", "secret_sauce")
        error = self.login_page.get_error_message()
        assert "locked" in error.lower(), "Locked user error message nahi aaya"