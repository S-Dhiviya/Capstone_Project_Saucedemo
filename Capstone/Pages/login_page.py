# Importing By classes from selenium for locators
from selenium.webdriver.common.by import By
# To use the methods from base_page importing Class BasePage.
from Pages.base_page import BasePage


# LoginPage inherits BasePage. LoginPage contains locators and methods to interact with locators.
class LoginPage(BasePage):

    # LOCATORS - Uses BasePage methods to locate these elements while doing interactions.
    # Username and password fields locator
    USERNAME_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')

    # Login button, Error message locator
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR_MESSAGE=(By.XPATH,'//h3[contains(text(),"Epic sadface:")]')


    # METHODS TO INTERACT WITH THE ELEMENTS
    # login() is used to locate username and password and enter the valid data and to click login button
    # After login it enters inventory page
    def login(self, username, password):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)


    # login_error_message() is used to return the error message if there is invalid credentials
    def login_error_message(self):
        error_message=self.find_element(self.ERROR_MESSAGE)
        return error_message.text




