import requests

def get_rate():
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=YOUR_KEY"
    res = requests.get(url)
    data = res.json()
    rate = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    return float(rate)