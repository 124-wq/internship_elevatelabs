import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content,'html.parser')
news_headlines = soup.find_all(['h1','h2','h3'])

for headline in news_headlines:
    print(headline.text.strip())
