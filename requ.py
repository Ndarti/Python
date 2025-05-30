import requests
import http.client
BASEKUCOIN="https://api.kucoin.com/"
BASE = 'https://api.binance.com'
def printdeb(bool,str):
    if bool==True:
        print(str)
def tradingDay(symbol=None, symbols=None):
    separator = '/' if '/' in symbol else ''
    if separator:
        base, quote = symbol.split(separator)
    else:
        if symbol.startswith('BTC') and symbol.endswith('USDT'):
            base, quote = symbol[:3], symbol[3:]
    if symbol and symbols:
        raise Exception("err")
    url = BASE + "/api/v3/ticker/price"
    if symbol:
        params = {'symbol': base+quote}
    if symbols:
        params = {'symbols':  base+quote}
    resp = requests.get(url, params=params)
    if resp.status_code == 200:
        return resp.json()
    else:
        return False
def tradingDayKoin(symbol=None, symbols=None):
    separator = '/' if '/' in symbol else ''
    if separator:
        base, quote = symbol.split(separator)
        normalized = f"{base}-{quote}"
        symbol=normalized
    if symbol and symbols:
        raise Exception("err")
    url = BASEKUCOIN + "/api/v1/market/allTickers"
    if symbol:
        params = {'symbol': symbol}
    if symbols:
        params = {'symbols': symbols}
    resp = requests.get(url,params=params)
    #int(resp.json()['code']) == 200000  почему то код 200 000 ко всем значинием и найденым и нет поэтому немного др проверка
    if resp.json()['data']['ticker']!=[]:
        return resp.json()['data']['ticker'][0]['buy']
    #baseCurrency rootSymbol
    else:
        return False
def find_better_prise(A,B):
    A=float(A)
    B=float(B)
    printdeb(type,'find_better_prise')
    if A<B:
        printdeb(type,A)
        return A
    elif B<=A:
        printdeb(type,B)
        return B
    return Exception('dosen*t price')
def change(str):
    separator = '/' if '/' in str else ''
    if separator:
        base, quote = str.split(separator)
        a=quote
        quote=base
        base=a
    return tradingDay(a+'/'+base)
def changekoin(str):
    separator = '/' if '/' in str else ''
    if separator:
        base, quote = str.split(separator)
        a=quote
        quote=base
        base=a
    return tradingDayKoin(a+'/'+base)
def findcours(str):
    separator = '/' if '/' in str else ''
    if separator:
        base, quote = str.split(separator)
        printdeb(type,'findcours')
        price1=float(tradingDay(base+'/'+'USDT')['price'])
        price2=float(tradingDay('USDT'+'/' +quote)['price'])
        print(price1/price2)
def findcoursKucoin(str):
    separator = '/' if '/' in str else ''
    print(str)
    if separator:
        base, quote = str.split(separator)
        printdeb(type, 'findcours')
        if(tradingDayKoin(base + '/' + 'USDT')) and tradingDayKoin('USDT' + '/' + quote):
            price1 = float(tradingDayKoin(base + '/' + 'USDT'))
            price2 = float(tradingDayKoin('USDT' + '/' + quote))
            print(price1 / price2)
            return True
        return False
    return None


type=True#это отладка не ор внимания
AB_1="STX/DAI"
AB_2="SPOT/USD4T"
prise_1=-1
prise_2=-1
if tradingDay(AB_1)==False and change(AB_1)==True:
    BA=(change(AB_1)['price'])
    prise_1=1/float(BA)
elif tradingDay(AB_1):
    prise_1=tradingDay(AB_1)['price']

if tradingDayKoin(AB_2) == False and changekoin(AB_2) == True:
    BA = (changekoin(AB_2))
    prise_2 = 1 / float(BA)
elif tradingDayKoin(AB_2):
    prise_2 = tradingDayKoin(AB_2)
else:
    Exception("er")

printdeb(type,find_better_prise(prise_1,prise_2))
if find_better_prise(prise_1,prise_2)<=0.0:
    findcoursKucoin(AB_2)
    findcours(AB_1)
else:
    print(type,find_better_prise(prise_1,prise_2))
# "XBTUSDTM"