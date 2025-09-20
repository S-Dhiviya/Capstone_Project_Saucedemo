# Test Classes contains test scripts and calling actions
# Importing pytest modules
import pytest
# Importing login page to use methods in it.
from Pages.login_page import LoginPage
# Importing inventory page to use methods in it.
from Pages.inventory_page import InventoryPage
# To reuse data from Utils folder like valid credentials
from Utils.config import valid_username,valid_password


# To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestLogout:

    # test_validate_logout() enters valid data and navigates to inventory page and clicks logout
    def test_validate_logout(self):

        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
        login_page = LoginPage(self.driver)
        # login_page object calls login() and enters username and password
        login_page.login(valid_username,valid_password)

        # Check the navigation of inventory URL
        inventory_url = "https://www.saucedemo.com/inventory.html"
        assert inventory_url in login_page.get_current_url()

        # Creates instance of InventoryPage class
        inventory_page = InventoryPage(self.driver)
        # Clicks Burger menu and Clicks Logout
        inventory_page.logout()
        print("Successfully logged out")

        # After Logout verifying the login URL whether it properly navigated to login page
        login_url="https://www.saucedemo.com/"
        assert login_url in login_page.get_current_url()


    # test_invalid_logout() enters valid data and navigates to inventory page and clicks other options
    # Asserts whether it navigates to login page without clicking logout
    def test_invalid_logout(self):

        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
        login_page = LoginPage(self.driver)
        # login_page object calls login() and enters username and password
        login_page.login(valid_username,valid_password)

        # Check the navigation of inventory URL
        inventory_url = "https://www.saucedemo.com/inventory.html"
        assert inventory_url in login_page.get_current_url()

        # Creates instance of InventoryPage class
        inventory_page = InventoryPage(self.driver)
        inventory_page.random_products(4)

        # After Logout verifying the login URL whether it properly navigated to login page
        # Assertion errors since navigation to login page doesn't occur
        assert "https://www.saucedemo.com/"==inventory_page.get_current_url(),"Invalid logout"

