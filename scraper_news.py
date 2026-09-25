import requests
from bs4 import BeautifulSoup

def get_news():
    url = "https://news.yahoo.co.jp/rss/topics/top-picks.xml"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "xml")
    news_items = []

    for item in soup.find_all("item"):
        title = item.title.get_text(strip=True)
        link = item.link.get_text(strip=True)
        news_items.append({"title": title, "link": link})

    return news_items
