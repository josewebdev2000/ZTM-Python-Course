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
    
    # Grab all elements of class .titleline bc those are links to news
    storylinks = my_bs.select(".titleline")
    
    # Grab all elements with score class to check upvotes
    scores = my_bs.select(".score")
    
    # Grab ID value of the first score
    first_score_id = scores[0].get("id")
    
    print(storylinks[0])
    print(scores[0])
    print(first_score_id)
    
if __name__ == "__main__":
    main()