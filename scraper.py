import requests
from bs4 import BeautifulSoup
from time import sleep

all_quotes = []
url = "http://quotes.toscrape.com"
page = "/page/1/"

while page:
    res = requests.get(f"{url}{page}")
    print(f"Now Scraping {url}{page}...")
    soup = BeautifulSoup(res.text, "html.parser")
    quotes = soup.find_all(class_="quote")

    for quote in quotes:
        all_quotes.append({
            "text": quote.find(class_="text").get_text(),
            "author": quote.find(class_="author").get_text(),
            "bio-link": quote.find("a")["href"] 
        })
    next_btn = soup.find(class_="next")
    page = next_btn.find("a")["href"] if next_btn else None
    sleep(2)

print(all_quotes)