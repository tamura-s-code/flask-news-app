from flask import Flask, render_template
from scraper_news import get_news
from scraper_weather import get_weather
from API_rate import get_rate

app = Flask(__name__)

@app.route("/")
def index():
    news_list = get_news()
    weather_list = get_weather()
    rate = get_rate()
    return render_template("index.html", news=news_list,weather=weather_list,rate=rate)

if __name__ == "__main__":
    app.run(debug=True)
