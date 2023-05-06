# Submit data through Selenium, click buttons, and check responses

# Open a browser window and get its title

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

import time
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
    
    # Enter a message through the "user-message" input
    user_message_input = firefox_driver.find_element(By.ID, "user-message")
    
    # Type information into the HTML input element
    user_message_input.send_keys("I am learning how to automate web testing with Selenium")
    
    # Grab the button to submit such information
    user_message_btn = firefox_driver.find_element(By.CSS_SELECTOR, "form#get-input > button.btn.btn-primary")
    
    # Click that button
    user_message_btn.click()
    
    # Display the result of such action
    your_message = firefox_driver.find_element(By.ID, "display")
    
    print(your_message.text)
    
    
    # Wait 3 seconds before closing the browser
    time.sleep(3)
    
    # Close the browser
    firefox_driver.close()

if __name__ == "__main__":
    main()