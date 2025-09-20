# Importing By classes from selenium for locators
from selenium.webdriver.common.by import By
# To use the methods from base_page importing Class BasePage.
from Pages.base_page import BasePage


# CartPage inherits BasePage. CartPage contains locators and methods to interact with locators.
class CartPage(BasePage):

    # LOCATORS - Uses BasePage methods to locate these elements while doing interactions.
    # Cart items,Item name locators
    CART_ITEMS=(By.CLASS_NAME,'cart_item')
    ITEM_NAME = (By.CLASS_NAME, 'inventory_item_name')

    # Item Price, Checkout Button locators
    ITEM_PRICE = (By.CLASS_NAME, 'inventory_item_price')
    CHECKOUT_BUTTON = (By.ID, 'checkout')


    # METHODS TO INTERACT WITH THE ELEMENTS
    # get_cart_items() is used to locate the cart container and returns all the cart items
    def get_cart_items(self):
        cart_items=self.driver.find_elements(*self.CART_ITEMS)
        return cart_items


    #fetch_product_details() is used display all the cart items name and price details
    def fetch_product_details(self, selected_items):
        print("\nCART ITEMS:")
        item_info = []

        # For each item in cart it extracts the name and price using Exception Handling
        for item in selected_items:
            try:
                name = item.find_element(*self.ITEM_NAME).text
                price = item.find_element(*self.ITEM_PRICE).text
                item_info.append((name, price))
            except Exception as e:
                print(f'Error fetching item details: {e}')

        # Displays name and price of cart items
        for name, price in item_info:
            print(f'{name}: {price}')
        return item_info


    # click_checkout() clicks checkout button and enters Checkout Page
    def click_checkout(self):
       self.wait_for_element_clickable(self.CHECKOUT_BUTTON).click()

