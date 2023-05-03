# Scrape HTML Data from Hacker News Website

# Remember to use the HTML class .titleline instead of .storylink

import requests
from bs4 import BeautifulSoup as BS
from constants import HACKERNEWS_URL, HTML_PARSER

def main() -> None:
    
    # Get HTML data from Hackernews
    res = requests.get(HACKERNEWS_URL)
    
    # Create web scrapping object
    my_bs = BS(res.text, HTML_PARSER)
    
    # Get page title
    hacker_title = my_bs.title
    
    # Find all <div> present
    all_divs = my_bs.find_all("div")
    
    # Find all <a> links present
    all_links = my_bs.find_all("a")
    
    print(f"Page Title: {hacker_title}\n")
    print(f"All div tags: \n{all_divs}\n")
    print(f"All link tags: \n{all_links}\n")  

if __name__ == "__main__":
    main()