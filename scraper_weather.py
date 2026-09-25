import requests
from bs4 import BeautifulSoup

def get_weather():
    #yahoo天気のURLからデータを取得
    url = "https://weather.yahoo.co.jp/weather/jp/13/4410.html"
    res = requests.get(url)
    soup = BeautifulSoup(res.content,"html.parser")

    weather_items = []

    #天気、最高気温、最低気温を抽出
    weather = soup.select_one('#main > div.forecastCity > table > tr > td > div > p.pict')
    high = soup.select_one('#main > div.forecastCity > table > tr > td > div > ul > li.high > em')
    low = soup.select_one('#main > div.forecastCity > table > tr > td > div > ul > li.low')

    weather_items.append({"weather":weather.text.replace('\n',''),"high":high.text.replace('\n',''),"low":low.text.replace('\n','')})

    return  weather_items