import re
import requests
#url="https://data-api.binance.vision/api/v3/exchangeInfo?symbol=BTCUSDT"
#response=requests.get(url)
#print(response.text)
def tradingDayAPI(BASE, symbol=None,symbols=None):
    if symbol and symbols:
        raise Exception("Валютная пара не найдена")
    url = BASE + "/api/v3/ticker/tradingDay"
    if symbol:
        params = {'symbol':symbol}
    if symbols:
        params = {'symbols':symbols}
    resp = requests.get(url,params=params)
    if resp.status_code==400:
        print(resp.status_code)
        exit(404)
    return resp.json()['lastPrice']
def Coupls(Valute):
    A=float(tradingDayAPI(  'https://api.binance.com/',Valute))
    B=float(tradingDayAPI(  'https://api2.binance.com/',Valute))
    if A<B:
        return str(f'{B} {A}+')
    else: return str(f'{A} {B}+')
print("введите валютную пару")
valute=str(input())
print(Coupls("XRPUSDT"))
#все валюты взять тикеры 2з
just_repeat2
2 фуекиии обр в метод
функция которая зап метод с такими методоми
кукоит метод

пары если не найдено
3) доп биржи ...2 конст