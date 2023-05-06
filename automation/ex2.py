# Diverse ways to grab HTML elements

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
    
    # Find HTML element by id
    element_by_id = firefox_driver.find_element(By.ID, "user-message")
    
    # Find HTML element by name attribute
    element_by_name = firefox_driver.find_element(By.NAME, "sum1")
    
    # Find HTML element by class
    element_by_class = firefox_driver.find_element(By.CLASS_NAME, "btn-primary")
    
    # Find HTML element by CSS Selector
    element_by_css = firefox_driver.find_element(By.CSS_SELECTOR, "div.form-group")
    
    # Find HTML element by XPath
    element_by_xpath = firefox_driver.find_element(By.XPATH, "//input")
    
    print(f"Element By ID: {element_by_id}")
    print(f"Element By Name: {element_by_name}")
    print(f"Element By Class: {element_by_class}")
    print(f"Element By CSS Selector: {element_by_css}")
    print(f"Element By XML Path: {element_by_xpath}")
    
    # Close the browser
    firefox_driver.close()

if __name__ == "__main__":
    main()