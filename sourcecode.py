import requests
from bs4 import BeautifulSoup
url= "https://w3schools.com/python/demopage.htm"
page=requests.get(url)
soup=BeautifulSoup(page.content, "html.parser")
print(soup.prettify())
