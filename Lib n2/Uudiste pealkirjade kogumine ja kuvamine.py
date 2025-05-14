import requests
from bs4 import BeautifulSoup
import pandas

# get url
url = input('Enter a URL (include `http://`): ')

# connect to the url
response = requests.get(url)
soup = BeautifulSoup(response.content,"html.parser")
for i in soup.find_all('h1'):
    print(i.text)