import requests
from bs4 import BeautifulSoup as bs
url= "https://w3schools.com/python/demopage.htm"
page=requests.get(url)
soup=bs(page.content, "html.parser")
print(soup.prettify())
