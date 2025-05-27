import requests
BASEKUCOIN="https://api-futures.kucoin.com"
BASE = 'https://api.binance.com'
def tradingDay(symbol=None, symbols=None):
    separator = '/' if '/' in symbol else ''
    if separator:
        base, quote = symbol.split(separator)
    else:
        if symbol.startswith('BTC') and symbol.endswith('USDT'):
            base, quote = symbol[:3], symbol[3:]
    if symbol and symbols:
        raise Exception("err")
    url = BASE + "/api/v3/ticker/tradingDay"
    if symbol:
        params = {'symbol': base+quote}
    if symbols:
        params = {'symbols':  base+quote}
    resp = requests.get(url, params=params)
    if resp.status_code == 200:
        return resp.json()
    else:
        return False
        print(resp.status_code)
def tradingDayKoin(symbol=None, symbols=None):
    separator = '/' if '/' in symbol else ''
    if separator:
        base, quote = symbol.split(separator)
        base = f"X{base}" if base == 'BTC' else base
        if quote == 'USDT': quote = 'USDTM'
        normalized = f"{base[:-1]}{quote}"
        symbol=normalized
    if symbol and symbols:
        raise Exception("err")
    url = BASEKUCOIN + "/api/v1/contracts/"
    if symbol:
        params = {'symbol': symbol}
    if symbols:
        params = {'symbols': symbols}
    resp = requests.get(url+params['symbol'])
    if int(resp.json()['code']) == 200000:
        return resp.json()['data']
    #baseCurrency rootSymbol
    else:
        print(resp.status_code)
def find_better_prise(A,B):
    A=float(A)
    B=float(B)
    if A<B:
        return A
    elif B<=A:
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
AB_1="BTC/USDT"
AB_2="BTC/USDT"
prise_1=-1
prise_2=-1
if tradingDay(AB_1)==False and change(AB_1)==True:
    BA=(change(AB_1)['lastPrice'])
    prise_1=1/float(BA)
elif tradingDay(AB_1):
    prise_1=tradingDay(AB_1)['lastPrice']
if tradingDayKoin(AB_2) == False and change(AB_2) == True:
    BA = (changekoin(AB_2)['markPrice'])
    prise_2 = 1 / float(BA)
elif tradingDay(AB_2):
    prise_2 = tradingDayKoin(AB_2)['markPrice']
else: Exception("er")
print(find_better_prise(prise_1,prise_2))
#"XBTUSDTM"