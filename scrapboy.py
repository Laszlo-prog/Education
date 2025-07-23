

import requests
from bs4 import BeautifulSoup
import selectorlib


url = ("https://www.amazon.com")

def scrap(url):
    response = requests.get(url, 'h1')
    source = response.text
    return source

if __name__ == "__main__":
    print(scrap(url))
