import requests
from bs4 import BeautifulSoup

all_quotes = []
res = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(res.text, "html.parser")
quotes = soup.find_all(class_="quote")

for quote in quotes:
    all_quotes.append({
        "text": quote.find(class_="text").get_text(),
        "author": quote.find(class_="author").get_text(),
        "bio-link": quote.find("a")["href"] 
    })

print(all_quotes)