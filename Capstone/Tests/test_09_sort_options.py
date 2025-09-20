# Test Classes contains test scripts and calling actions
# Importing pytest modules
import pytest
# Importing login page to use methods in it.
from Pages.login_page import LoginPage
# Importing inventory page to use methods in it.
from Pages.inventory_page import InventoryPage
# To reuse data from Utils folder like valid credentials
from Utils.config import *


# To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestSortFunctionality:

    # test_sort_option() navigates to Inventory page and Selects Sorting Options and displays the product details
    def test_sort_option(self):

        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
        login_page = LoginPage(self.driver)
        # login_page object calls login() and enters username and password
        login_page.login(valid_username,valid_password)

        # Check the navigation of inventory URL
        inventory_url = "https://www.saucedemo.com/inventory.html"
        assert inventory_url in login_page.get_current_url()

        # Creates instance of InventoryPage class
        inventory_page = InventoryPage(self.driver)

        # Sorts the inventory items based on Name Z-A and displays the inventory item names
        print("\nSorting Name Z-A:")
        inventory_page.sorting_name(sort_name_option)

        # Sorts the inventory items based on Price Low to High and displays the inventory item prices
        print("\nSorting price low to high:")
        inventory_page.sorting_price(sort_price_option)


    # test_invalid_sort_option() navigates to Inventory page and Checks for Invalid Sort Option
    # This test fails since the invalid option is not available on webpage
    def test_invalid_sort_option(self):
        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
        login_page = LoginPage(self.driver)
        # login_page object calls login() and enters username and password
        login_page.login(valid_username, valid_password)

        # Check the navigation of inventory URL
        inventory_url = "https://www.saucedemo.com/inventory.html"
        assert inventory_url in login_page.get_current_url()

        # Creates instance of InventoryPage class
        inventory_page = InventoryPage(self.driver)

        # Sorts the inventory items based on invalid sorting name and throws error
        print("Sorting Name C to H:")
        inventory_page.sorting_name(invalid_sorting_name)








