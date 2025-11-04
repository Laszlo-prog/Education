import requests
import selectorlib

url = 'http://www.pph.hu/'
def scrape(url):
    "'Scrape the page source from the given URL and extract data using selectorlib.'"
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    source = res.text
    return source


if __name__ == "__main__":
    data = scrape(url)
    print(data)
