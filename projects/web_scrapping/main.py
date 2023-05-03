# Scrape HTML Data from Hacker News Website

# Remember to use the HTML class .titleline instead of .storylink

import requests
from bs4 import BeautifulSoup as BS
from constants import HACKERNEWS_URL, HTML_PARSER

# MODIFICATION: ALLOW THE USER TO ADD THEIR OWN URL AND CHECK IF IT BELONGS TO HACKERNEWS

def main() -> None:

    # Get HTML data from Hackernews
    res = requests.get(HACKERNEWS_URL)

    # Create web scrapping object
    my_bs = BS(res.text, HTML_PARSER)

    # Grab all elements of class .titleline bc those are links to news
    storylinks = my_bs.select(".titleline")

    # Grab all elements with score class to check upvotes
    subtexts = my_bs.select(".subtext")
    
    links = create_custom_hn(storylinks, subtexts)

    for each_dict in links:
        
        print("\n")
        for key, value in each_dict.items():
            
            print(f"{key.capitalize()}: {value}")
            
        print("\n")
            
    

def sort_stories_by_votes(hnlist):
    
    return sorted(hnlist, key = lambda k : k["votes"], reverse = True)

def create_custom_hn(links, scoresContainer):

    hn = []

    for i, item in enumerate(links):
        
        # Get a tag of this span link
        a_tag = links[i].find("a")
        
        # Get title of each link
        title = links[i].getText()
        
        # Get score of each link
        score = scoresContainer[i].select(".score")
        
        if score:
            
            points = int(score[0].getText().replace(" points", ""))
            # Get the actual link
            href = a_tag.get("href")
            
            if points >= 100:

                hn.append({"title": title, "link": href, "votes": points})

    return sort_stories_by_votes(hn)


if __name__ == "__main__":
    main()
