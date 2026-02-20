import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content,'html.parser')
news_headlines = soup.find_all(['h1','h2','h3'])

with open("news_headlines.txt", "w") as f:
    for headline in news_headlines:
        f.write(headline.text.strip() + "\n")
        print(headline.text.strip())
