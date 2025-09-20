# Test Classes contains test scripts and calling actions
# Importing pytest modules to use in test cases
import pytest
# Importing CSV and OS for utilizing CSV file[CSV File is stored under Data folder]
import csv
import os
# Importing login page to use methods in it.
from Pages.login_page import LoginPage


# get_login_data() locates the CSV file and reads the data
def get_login_data():
    login_data = []
    # Get the directory of the current script
    current_dir = os.path.dirname(__file__)
    # Construct the correct path to the CSV file
    data_file = os.path.join(current_dir, '../Data', 'login_data.csv')


    # Read the CSV file
    with open(data_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Ensure each row is treated as a dictionary
            username = row['username']
            password = row['password']
            login_data.append((username, password))
    return login_data


#To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestLogin:

    # Parameters username and password are used in test function and get_login_data() method is called.
    # This runs multiple times with different sets of username and password
    @pytest.mark.parametrize("username, password", get_login_data())
    def test_login(self, username, password):

        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to
        login_page = LoginPage(self.driver)
        # Calls login method from LoginPage
        login_page.login(username, password)

        # Exception Handling
        try:
            # With valid credentials it navigates to inventory page and asserts the URL
            inventory_url = "https://www.saucedemo.com/inventory.html"
            assert inventory_url in login_page.get_current_url()

        except AssertionError:
            # With invalid credentials, Assertion error occurs
            assert False,"Access Denied"



