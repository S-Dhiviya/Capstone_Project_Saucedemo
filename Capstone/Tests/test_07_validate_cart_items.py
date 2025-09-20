# Importing CSV,OS to access the keyword.csv file
import csv
import os
# Importing pytest modules to use in test cases
import pytest
# To use the methods from keywords importing Class KeywordDriven
from Tests.keywords import KeywordDriven


# read_keywords() locates the CSV file and reads the data
def read_keywords(file_name):
    try:
        # Get the directory of the current script
        current_dir = os.path.dirname(__file__)
        # Construct the correct path to the CSV file
        file_path = os.path.join(current_dir, '../Data', file_name)

        # Read the CSV file
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return [row for row in reader]

    # Raises FileNotFoundError if file doesn't exist
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found")


# To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestValidateCartItems:

    # test_validate_cart_items() navigates to cart page and checks whether cart and inventory items matches
    # Throws error message when items doesn't match
    def test_validate_cart_items(self):

        # Reads the Keywords in CSV file
        keywords = read_keywords('../Data/keywords_07_validate_cart_items.csv')
        # Create an instance of the keyword-driven framework
        framework = KeywordDriven(self.driver)

        # Loops through each row in CSV to perform actions
        for step in keywords:
            # Extract the keyword and its optional arguments from the CSV row
            keyword = step['Keyword']
            arg1 = step.get('Argument1')
            arg2 = step.get('Argument2')
            arg3 = step.get('Argument3')

            # Dynamically execute the method based on the keyword
            method = getattr(framework, keyword)
            # If the argument is "selected_items", replace it with the actual selected_items list from the framework
            if arg1 == "selected_items":
                arg1 = framework.selected_items

            # Calls the method based on the number of arguments present
            if arg3:
                method(arg1, arg2, arg3)
            elif arg2 and not arg3:
                method(arg1, arg2)
            elif arg1 and not arg2:
                method(arg1)
            # If there are no arguments it calls method()
            else:
                method()


