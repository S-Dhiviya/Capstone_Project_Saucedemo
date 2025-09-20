# Importing os and time for screenshot in order summary
import os
import time
# Importing By classes from selenium for locators
from selenium.webdriver.common.by import By
# To use the methods from base_page importing Class BasePage.
from Pages.base_page import BasePage
#Importing exceptions to raise when error occurs
from selenium.common.exceptions import TimeoutException


# CheckoutPage inherits BasePage. CheckoutPage contains locators and methods to interact with locators.
class CheckoutPage(BasePage):

    # LOCATORS - Uses BasePage methods to locate these elements while doing interactions.
    # Checkout Information-First name,Last name, Postal Code locators
    FIRST_NAME_INPUT = (By.ID, 'first-name')
    LAST_NAME_INPUT = (By.ID, 'last-name')
    POSTAL_CODE_INPUT= (By.ID, 'postal-code')

    # Error message,Continue button locators
    ERROR_MESSAGE=(By.XPATH,'//div[@class="error-message-container error"]//h3')
    CONTINUE_BUTTON = (By.ID, 'continue')

    # Checkout Overview-Order Summary,Finish button locators
    ORDER_CONTAINER = (By.ID, 'contents_wrapper')
    FINISH_BUTTON = (By.ID, 'finish')

    # Checkout Completion-Confirmation and Order Message locators
    CONFIRMATION_MESSAGE=(By.XPATH, '//h2[text()="Thank you for your order!"]')
    ORDER_MESSAGE=(By.CLASS_NAME,'complete-text')


    # METHODS TO INTERACT WITH THE ELEMENTS
    # enter_checkout_information() is used to interact with first name, last name and postal code
    # send_keys() enters the data provided in keywords file
    def enter_checkout_information(self, first_name, last_name, postal_code):
        self.wait_for_element_clickable(self.FIRST_NAME_INPUT).send_keys(first_name)
        self.wait_for_element_clickable(self.LAST_NAME_INPUT).send_keys(last_name)
        self.wait_for_element_clickable(self.POSTAL_CODE_INPUT).send_keys(postal_code)


    # checkout_error() displays error message if any checkout information is left and clicked continue
    def checkout_error(self):
        try:
            error_element = self.wait_for_element(self.ERROR_MESSAGE)
            return error_element.text
        except TimeoutException:
            return "No error message found"


    # click_continue() clicks continue button and enters order summary page
    def click_continue(self):
        self.wait_for_element_clickable(self.CONTINUE_BUTTON).click()


    # order_summary() locates the order container and takes screenshot of the ordered items
    def order_summary(self):
        try:
            self.find_element(self.ORDER_CONTAINER)

            # Checks 'Screenshots' folder exists or not and creates folder if not exists
            screenshot_dir = os.path.join(os.getcwd(), 'Screenshots')
            os.makedirs(screenshot_dir, exist_ok=True)

            # Creates screenshot file along with datetime
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_path = os.path.join(screenshot_dir, f'screenshot_{timestamp}.png')

            # Throws exception when screenshot cannot be taken
            if self.driver.get_full_page_screenshot_as_file(screenshot_path):
                print(f"Screenshot saved at: {screenshot_path}")
            else:
                print("Failed to save screenshot.")
        except Exception as e:
            print(f"Error in order_summary: {e}")

        # Firefox browser full page screenshot
        # self.driver.get_full_page_screenshot_as_file(screenshot_path)
        # Firefox or Chrome browser screenshot
        # self.driver.save_screenshot(screenshot_path)


    # click_finish() clicks FINISH and enters the Checkout Completion Page
    def click_finish(self):
        self.wait_for_element_clickable(self.FINISH_BUTTON).click()


    # confirmation_message() displays the confirmation message upon order completion after clicking finish
    def confirmation_message(self):
        thanks_message=self.find_element(self.CONFIRMATION_MESSAGE)
        assert thanks_message.text == "Thank you for your order!"
        order_message=self.find_element(self.ORDER_MESSAGE)
        print(thanks_message.text,order_message.text)




