# keywords.py file typically serves as a library of reusable keywords or actions
# All the keywords are stored in CSV file
# To use the methods from LoginPage, InventoryPage,CartPage,CheckoutPage
from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage
from Pages.cart_page import CartPage
from Pages.checkout_page import CheckoutPage


# KeywordDriven class contains methods for each keyword and actions to perform when keyword is called
class KeywordDriven:

    # Creates instance of each class
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.inventory_page = InventoryPage(driver)
        self.cart_page = CartPage(driver)
        self.checkout_page=CheckoutPage(driver)


    # login() calls LoginPage login method to pass the username and password
    def login(self, username, password):
        self.login_page.login(username, password)


    # select_products() calls InventoryPage to select the random products and fetch the details
    def select_products(self):
        self.selected_items = self.inventory_page.random_products(2)
        self.selected_elements = self.inventory_page.fetch_product_details(self.selected_items)


    # random_selected_products() calls InventoryPage to select 4 random products and fetch the details
    def random_selected_products(self):
        self.selected_items = self.inventory_page.random_products(4)
        self.selected_elements=self.inventory_page.fetch_product_details(self.selected_items)


    # inventory_items_details() displays the selected items details
    def inventory_items_details(self, selected_items=None):
        # selected_items=None to use the data from  random_selected_products()
        if selected_items is None:
            return self.selected_elements


    # adding_to_cart() adds the selected item to cart
    def adding_to_cart(self, selected_items=None):
        # selected_items=None to use the data from  random_selected_products()
        if selected_items is None:
            selected_items = self.selected_items
        self.inventory_page.add_to_cart(selected_items)


    # cart_count() calls the cart_count() and displays the cart count and asserts the count
    def cart_count(self):
        self.cart_count = self.inventory_page.cart_count()
        print(f'CART_COUNT:{self.cart_count}')
        expected_count = 4
        assert (self.cart_count) == expected_count, f"Expected {expected_count} items in cart but found {self.cart_count}"


    # cart_list() calls the cart_count() and displays the cart count
    # Enters the cart page using go_to_cart() and fetch the cart items details
    def cart_list(self):
        self.cart_count = self.inventory_page.cart_count()
        print(f'CART_COUNT:{self.cart_count}')
        self.inventory_page.go_to_cart()
        self.cart_items=self.cart_page.get_cart_items()
        self.cart_products=self.cart_page.fetch_product_details(self.cart_items)


    # cart_product_details() displays the cart items details
    def cart_product_details(self,selected_items=None):
        if selected_items is None:
            return self.cart_products


    # validate_cart() compares the selected inventory item matches with the cart items
    def validate_cart(self):
        self.inventory_items=self.inventory_items_details()
        self.cart_products=self.cart_product_details()
        assert self.inventory_items == self.cart_products, "Cart items do not match with selected inventory items"
        print("Cart items match with selected inventory items")


    # checkout() calls the Checkout Page methods to enter Checkout Information and clicks Continue
    def checkout(self, first_name, last_name, postal_code):
        self.cart_page.click_checkout()
        self.checkout_page.enter_checkout_information(first_name, last_name, postal_code)
        self.checkout_page.click_continue()


    # checkout_error_message() if any Checkout Information is unfilled, it throws error message
    def checkout_error_message(self):
        error = self.checkout_page.checkout_error()
        print(f"{error}")

        # Asserts the expected error matches the actual error in the page
        expected_error = "Error: Postal Code is required"
        assert error == expected_error, f"Expected error message '{expected_error}', but got '{error}'"


    # submit_order() shows the order summary and after finish it displays confirmation message
    def submit_order(self):
        self.checkout_page.order_summary()
        self.checkout_page.click_finish()
        self.checkout_page.confirmation_message()

