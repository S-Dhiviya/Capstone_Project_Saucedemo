# Test Classes contains test scripts and calling actions
# Importing pytest modules
import pytest
# Importing login page to use methods in it.
from Pages.login_page import LoginPage
# Importing inventory page to use methods in it.
from Pages.inventory_page import InventoryPage
#Importing exceptions to raise when error occurs
from selenium.common.exceptions import StaleElementReferenceException
# To reuse data from Utils folder like valid credentials
from Utils.config import valid_username,valid_password


# To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestResetApp:

    # test_reset_app() navigates to inventory page and adds products to cart and clicks reset to view cart count
    # This test raises StaleElementException
    def test_reset_app(self):

        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
        login_page = LoginPage(self.driver)
        # login_page object calls login() from login_page.py and enters username and password
        login_page.login(valid_username,valid_password)

        # Check the navigation of inventory URL
        inventory_url = "https://www.saucedemo.com/inventory.html"
        assert inventory_url in login_page.get_current_url()

        # Creates instance of InventoryPage class and selects the products
        inventory_page = InventoryPage(self.driver)
        random_products = inventory_page.random_products(4)

        # Adds the selected products to cart and navigates to cart page
        inventory_page.add_to_cart(random_products)
        inventory_page.go_to_cart()

        # Navigates back to Inventory page
        self.driver.back()

        # Raises StaleElementReferenceException, because cart badge element disappears after reset
        with pytest.raises(StaleElementReferenceException):
            inventory_page.reset_app()
        print("No selections retained in cart")





