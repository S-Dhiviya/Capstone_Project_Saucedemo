                  ** Automated Testing of E-commerce Web Application(SAUCE DEMO) **
		
This project automates the testing of the web application (https://www.saucedemo.com/) by simulating user actions and validating its core functionalities. The key modules covered include logging in with different user roles, navigating the product catalog, adding items to the cart, and completing the purchase flow.It ensures the reliability of critical components through both positive and negative test scenarios.

The test scripts are developed using Selenium with Python and Pytest, following the Hybrid framework [Page Object Model (POM),Data Driven,Keyword Driven framework] and adhering to Object-Oriented Programming (OOP) principles. The test data is externalized (CSV) using Data Driven framework,Keyword Driven Testing framework and common configurations are handled in config.py.The valid and invalid login data are externalized (CSV) using Data Driven framework.Keywords are stored as CSV file which access the methods in keywords.py file using Keyword Driven Testing framework.The suite includes 10 detailed test cases focused on verifying page behavior, accessibility of essential elements, navigation flows, and login/logout processes.



**Project Architecture :**

**Capstone/**
│
├── **Data/**
│   ├── __init__.py
│   ├── invalid_login_data.csv
│   ├── keywords_05_select_products.csv
│   ├── keywords_06_add_to_cart.csv
│   ├── keywords_06_invalid_cart_count.csv
│   ├── keywords_07_validate_cart_items.csv
│   ├── keywords_08_complete_checkout.csv
│   ├── keywords_08_error_checkout.csv
│   ├── login_data.csv
│
├── **Pages/**
│   ├── __init__.py
│   ├── base_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── inventory_page.py
│   ├── login_page.py
│
├── **Screenshots/**
│   ├──screenshot.png
│
├── **Tests/**
│   ├── __init__.py
│   ├── conftest.py
│   ├── keywords.py
│   ├── test_01_validate_login.py
│   ├── test_02_invalid_credentials.py
│   ├── test_03_validate_logout.py
│   ├── test_04_check_cart_icon.py
│   ├── test_05_select_items.py
│   ├── test_06_add_to_cart.py
│   ├── test_06_invalid_cart_count.py
│   ├── test_07_validate_cart_items.py
│   ├── test_08_complete_checkout.py
│   ├── test_08_invalid_checkout.py
│   ├── test_09_sort_options.py
│   ├── test_10_reset_app_state.py
│
├── **Utils/**
│   ├── __init__.py
│   ├── config.py
│
├── requirements.txt
├── README.md



**Tools & Technologies:**
*     Selenium WebDriver
*     Python 
*     Pytest
*     OOPS
*     Page Object Model (POM)
*     Data Driven framework
*     Keyword Driven framework
*     Test Data(CSV file)
*     Explicit Waits
*     Exception Handling
*     Pytest HTML Reports




**Test Suite :**

Test Case 1: Validates login functionality with different predefined usernames using external CSV file

	* Positive case: Properly enters Saucedemo login page and navigates to inventory page
	* Negative case: Enters Saucedemo login page and throws assertion error for "locked_out_user"
 
Test Case 2: Validates login functionality with different invalid credentials using external CSV file

	* Negative case: Login with invalid credentials and displays the error message

Test Case 3: Validates logout functionality

	* Positive case: Checks whether the logout button is visible after login and properly logs the user out and asserts the login URL
	* Negative case: Checks whether the logout button is visible and doesn't logs the user out and asserts the login URL

Test Case 4: Verify if the cart icon is visible on the product listing page post login

	* Navigates to inventory page and checks cart icon is visible
	* Also checks cart icon is accessible at all times after login.

Test Case 5: Random selection of inventory products and data extraction

	* Navigates to inventory page and randomly selects 4 inventory items out of total 6 inventory items using Keyword Driven.
	* Displays the selected inventory items name and price.
 
Test Case 6: Add selected products to cart and validate the cart items 

	* Positive case: Selected inventory items are added to cart and validate the cart count==4 and displays the cart items
	* Negative case: Adds to cart only 2 inventory items and validate the cart count==4 and throws Assertion Error.

Test Case 7: Validate product details inside the cart

	* Navigates to cart page and validates the products in the cart matches with the added inventory items
	* If there is mismatch in cart items and added inventory items it shows an error message
 
Test Case 8: Complete checkout and validate order

	* Positive case: Naviagates to checkout page and fills the checkout information and takes screenshot of order summary and displays confirmation message
	* Negative case: Navigates to checkout page and unfills few data and clicks continue. Displays error message to fill the data.

Test Case 9: Validate sorting functionality on the products page

	* Naviagates to Inventory page and clicks sorting option like 'Name (Z to A)(A to Z),Price (low to high)(high to low)'
 	* Verifies products get sorted based on the options and displays the items name and price depending on the selected option

Test Case 10: Validate "Reset App State" functionality

	* Adds products to cart and navigates to cart page and returns back to inventory page and cart icon shows items count in cart badge
	* Under burger menu clicks Reset App State and cart badge disappears. StaleElementReference exception raises after cart badge is searched.



**Instructions:**

1.Ensure Selenium,Python and any Browser(Chrome,Firefox,Edge) installed in your system. 

2.To create a virtual environment,

	>python -m venv venv
 
	>source venv/bin/activate(macOS)
 
	>venv\scripts\activate(Windows)

3.To install the dependencies,

	>pip install -r requirements.txt

4.To execute all the test files,

	>pytest -v -s Tests/

	>pytest pytest -v -s Tests/test_01_validate_login.py(for any specific file)

	>pytest pytest -v -s Tests/test_01_validate_login.py::test_login(for specific method in a test file)



**To Generate HTML Report:**

To install pytest–html package

	>pip install pytest–html

To execute all the test files and generate html report,

	>pytest -v -s Tests/   --html=reports.html    --self-contained-html

To execute single file and generate html report,

	>pytest -v -s Tests/test_01_validate_login.py   --html=case01_report.html   --self-contained-html


**Screen Recording**: https://drive.google.com/file/d/1s-chh-h0DhXVq9wAOmhqyWQNR2OaSzZ_/view?usp=sharing




