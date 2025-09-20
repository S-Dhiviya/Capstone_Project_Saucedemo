# Importing random to select random products
import random
# Importing By classes from selenium for locators
from selenium.webdriver.common.by import By
# To use the methods from base_page importing Class BasePage.
from Pages.base_page import BasePage
# Importing Select for dropdown element
from selenium.webdriver.support.select import Select


#InventoryPage inherits BasePage. InventoryPage contains locators and methods to interact with locators.
class InventoryPage(BasePage):

    # LOCATORS - Uses BasePage methods to locate these elements while doing interactions.
    # Inventory Page - Container,Item name and Price locators
    ITEM_CONTAINER=(By.CLASS_NAME,'inventory_item')
    ITEM_NAME=(By.CLASS_NAME,'inventory_item_name')
    ITEM_PRICE=(By.CLASS_NAME,'inventory_item_price')

    # Add to Cart,Cart Icon and Cart badge locators
    ADD_TO_CART_BUTTON = (By.XPATH, './/button[contains(text(),"Add to cart")]')
    CART_ICON=(By.CLASS_NAME,'shopping_cart_link')
    CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')

    # Dropdown options-Select Option Container,Sort Options locators
    SELECT_OPTION_CONTAINER=(By.CLASS_NAME,'select_container')
    SORT_OPTIONS=(By.CLASS_NAME,'product_sort_container')

    # Burger menu,Reset App and Logout locators
    BURGER_MENU = (By.ID, 'react-burger-menu-btn')
    RESET_MENU=(By.ID,'reset_sidebar_link')
    LOGOUT = (By.XPATH, '//a[text()="Logout"]')


    # METHODS TO INTERACT WITH THE ELEMENTS
    # random_products() is used to select 4 random items from the total six items in inventory page
    # count-no. of inventory items to be selected
    def random_products(self,count):
        products = self.driver.find_elements(*self.ITEM_CONTAINER)
        selected=random.sample(products,count)
        return selected


    # fetch_product_details() is used display all selected inventory items name and price details
    def fetch_product_details(self,selected_items):
        print("\nINVENTORY ITEMS:")
        item_info = []

        # For each item selected it extracts the name and price using Exception Handling
        for item in selected_items:
            try:
                name = item.find_element(*self.ITEM_NAME).text
                price = item.find_element(*self.ITEM_PRICE).text
                item_info.append((name, price))
            except Exception as e:
                print(f'Error fetching item details: {e}')

        # Displays name and price of randomly selected inventory items
        for name, price in item_info:
            print (f'{name}:{price}')
        return item_info


    # add_to_cart() for each selected item it clicks ADD_TO_CART_BUTTON and adds it to cart
    def add_to_cart(self,selected_items):
        try:
         for item in selected_items:
               inventory_items=item.find_element(*self.ADD_TO_CART_BUTTON)
               inventory_items.click()
        except Exception as e:
                print(f"Cannot be added to cart:{e}")


    #  cart_count() displays the number of items added to cart using cart badge
    # CART_BADGE contains total number of items in the cart
    def cart_count(self):
        self.wait_for_element_clickable(self.CART_ICON)
        cart_items_count=self.find_element(self.CART_BADGE)

        # Checks if cart badge value is present else prints the message
        if cart_items_count is not None:
            return cart_items_count.text
        else:
             print("No cart items found")


     # sorting_name() selects the Sorting Option "Name (Z to A)" and displays the sorted item names
    def sorting_name(self,sort_name_option):

        # Locates the Select Option container and Sort options like A to Z or Z to A
        self.wait_for_element_clickable(self.SELECT_OPTION_CONTAINER).click()
        select_element=self.driver.find_element(*self.SORT_OPTIONS)

        # Uses Select Object to select Z to A using "select_by_visible_text"
        select_object=Select(select_element)
        select_object.select_by_visible_text(sort_name_option)

        # After sorting Z to A,it displays the inventory item names
        products = self.driver.find_elements(*self.ITEM_CONTAINER)
        for name in products:
            item_name = name.find_element(*self.ITEM_NAME).text
            print(item_name)


    # sorting_price() selects the Sorting Option "Price (low to high)" and displays the sorted item prices
    def sorting_price(self,sort_price_option):

        # Locates the Select Option container and Sort options like High to Low or Low to High
        self.wait_for_element_clickable(self.SELECT_OPTION_CONTAINER).click()
        select_element = self.driver.find_element(*self.SORT_OPTIONS)

        # Uses Select Object to select using "Price (low to high)"
        select_object = Select(select_element)
        select_object.select_by_visible_text(sort_price_option)

        # After sorting low to high,it displays the inventory items price
        products = self.driver.find_elements(*self.ITEM_CONTAINER)
        for price in products:
            item_price = price.find_element(*self.ITEM_PRICE).text
            print(item_price)


    # reset_app() locates the burger menu in inventory page and clicks the RESET APP menu
    # To show the StaleElement Reference Cart Badge is used, after 'reset' cart badge disappears
    def reset_app(self):
        self.wait_for_element_clickable(self.CART_ICON)
        cart_items_count = self.find_element(self.CART_BADGE)
        self.wait_for_element(self.BURGER_MENU).click()
        self.wait_for_element_clickable(self.RESET_MENU).click()
        return cart_items_count.text


    # logout() locates the burger menu in inventory page and clicks the LOGOUT menu
    def logout(self):
        self.click_element(self.BURGER_MENU)
        self.click_element(self.LOGOUT)


    # go_to_cart() clicks the cart icon and enters the Cart Page
    def go_to_cart(self):
        self.click_element(self.CART_ICON)













