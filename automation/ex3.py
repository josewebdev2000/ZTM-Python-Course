# Get information from HTML elements grabbed

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

import constants

# Make sure the driver you have and the browser are of the same version
def main() -> None:
    
    # Set up Firefox Options
    firefox_options = Options()
    
    # Do not open pop up window
    firefox_options.add_argument("-headless")
    
    # Create a new Firefox driver service
    firefox_service = Service(constants.DRIVER_PATH)
    
    # Create the Firefox driver
    firefox_driver = webdriver.Firefox(service = firefox_service, options = firefox_options)
    
    # Perform a get request to a website
    firefox_driver.get(constants.URL)
    
    # Grab label of next input HTML element
    user_message_label = firefox_driver.find_element(By.CSS_SELECTOR, "label[for='message']")
    
    # Grab an input HTML element
    user_message_input = firefox_driver.find_element(By.ID, "user-message")
    
    # Get value of a particular HTML attribute of the input
    user_message_placeholder = user_message_input.get_attribute("placeholder")
    
    # Get value of a JS property of the HTML element
    user_message_disabled = user_message_input.get_property("disabled")
    
    # Check if the input element in displayed
    is_displayed = user_message_input.is_displayed()
    
    # Check if the input element is selected
    is_selected = user_message_input.is_selected()
    
    # Check if the input element is enabled
    is_enabled = user_message_input.is_enabled()
    
    # Get text from label
    print(f"Get text from label: {user_message_label.text}")
    print(f"Get input placeholder: {user_message_placeholder}")
    print(f"Get JS property of input: {user_message_disabled}")
    print(f"Is input displayed? {is_displayed}")
    print(f"Is input selected? {is_selected}")
    print(f"Is input enabled? {is_enabled}")
    
    
    
    # Close the browser
    firefox_driver.close()

if __name__ == "__main__":
    main()