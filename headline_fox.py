import requests, re
from bs4 import BeautifulSoup, SoupStrainer

url = 'http://www.foxnews.com/'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")

# Latest News
def getLatestNews():
    for section in soup.find_all('section', id='latest'):
        for list_ in section.find_all('li'):
            for a in list_.find_all('a'):
                print (a.text)

getLatestNews()
