import requests
import selectorlib

url = 'http://www.pph.hu/'
def scrape(url):
    "'Scrape the page source from the given URL and extract data using selectorlib.'"
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    source = res.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file('selectors.yml')
    value = extractor.extract(source)
    return value

if __name__ == "__main__":
    data = scrape(url)
    extracted = extract(data)
    print(extracted)
