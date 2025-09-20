# conftest.py is used to define fixtures that can be reused across multiple test files.
#To import pytest modules
import pytest
#Importing Webdriver module from Selenium library
from selenium import webdriver
# Importing Service and GeckoDriverManager from Selenium library
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


# Fixtures are functions in pytest used to prepare environment for test execution.Scope by default it is "function".
#Scope="class" defines set up and tear down for each class
@pytest.fixture(scope="class")
# request is a built-in pytest fixture that gives you access to the test context. setup is fixture name
def setup(request):

    # Creates Webdriver instance
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    # If GekoDriver already installed in the path then use the below
    # driver = webdriver.Firefox(service=Service())
    # get() navigates to Sauce Demo Webpage and opens in Firefox Browser
    driver.get("https://www.saucedemo.com/")
    #This is used to view the  Browser in maximized window
    driver.maximize_window()

    # request.cls.driver = driver lets self.driver to be used inside test class methods.
    request.cls.driver = driver
    # yield is used for setup and teardown logic
    yield
    # Closes the Firefox Window and ends the WebDriver session
    driver.quit()
