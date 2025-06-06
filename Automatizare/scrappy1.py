import request
import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the web page
url = 'https://redtube.com/redtube/lesbian'
response = requests.get(url)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract data (for example, all the links)
for link in soup.find_all('a'):
    print(link.get('href'))