# Open a browser window and get its title

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

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
    
    # Get the page title
    page_title = firefox_driver.title
    
    print(page_title)
    
    # Close the browser
    firefox_driver.close()

if __name__ == "__main__":
    main()