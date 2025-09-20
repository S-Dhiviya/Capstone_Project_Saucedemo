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
class TestCartIcon:

    # test_cart_icon() navigates to inventory page and checks cart icon visibility
    def test_cart_icon(self):

        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
        login_page = LoginPage(self.driver)
        # login_page object calls login() and enters username and password
        login_page.login(valid_username,valid_password)

        # Check the navigation of inventory URL
        inventory_url = "https://www.saucedemo.com/inventory.html"
        assert inventory_url in login_page.get_current_url()

        # Creates instance of InventoryPage class and locates the CART ICON
        inventory_page=InventoryPage(self.driver)
        cart_icon=inventory_page.find_element(inventory_page.CART_ICON)

        # Assertions for Cart icon to check visibility and accessibility
        assert cart_icon.is_displayed(),"Cart icon is not visible"
        assert cart_icon.is_enabled(), "Cart icon is not clickable"
        print("Cart icon is visible and enabled")

