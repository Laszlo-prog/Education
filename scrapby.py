import requests
from bs4 import BeautifulSoup

#url = "https://www.evomag.ro/?gad_source=1&gad_campaignid=18516780677&gbraid=0AAAAAD-e_AhJpOZEleGSwo5ohYwAXMNyf&gclid=CjwKCAjw6ZTCBhBOEiwAqfwJd1-eK7owCTlDC6GTLRGHmGqDNKduOu2xBLa8d45HXfPw75LdhRhVmBoCaV4QAvD_BwE"
url = " https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=b5c5df0f-1f84-4c35-bfe6-9361919ef19b"
request = requests.get(url)
print(request)

soup = BeautifulSoup(request.text, "html.parser")
print(soup)

#Source inspiration code: https://www.youtube.com/watch?v=704hLk559c8&list=PLc20sA5NNOvrsn3a78ewy2VTCXVV47NB4&index=19







