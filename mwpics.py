import requests
from bs4 import BeautifulSoup
import os

r = requests.get("https://www.fbi.gov/wanted/topten")
data = r.text
soup = BeautifulSoup(data, "lxml")
extra = soup.find(src = "https://www.fbi.gov/++theme++fbi-4-18-2018/images/fbibannerseal.png")
extra.decompose()

i = 0
for link in soup.find_all('img'):
    url = link.get("src")
    response = requests.get(url)
    i += 1
    if response.status_code == 200:
        with open((str(i) + '.jpg'), 'wb') as f:
            f.write(response.content)
