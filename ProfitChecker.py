import requests
import time

"""
triangular arbitrage trips we are checking for in bid/bid/bid form:
    1. AUD/BTC - BTC/ETH - ETH/AUD
    2. AUD/BTC - BTC/BCH - BCH/AUD
    3. AUD/ETH - ETH/BTC - BTC/AUD
    4. AUD/ETH - ETH/BCH - BCH/AUD
    5. AUD/BCH - BCH/BTC - BTC/AUD
    6. AUD/BCH - BCH/ETH - ETH/AUD
"""

def check_trips():
    Hitbtc_pairs = ['ETHBTC','BCHBTC','BCHETH']
    Acx_pairs = ['btcaud','bchaud','ethaud']

    Acx_ticker = requests.get('https://acx.io:443//api/v2/tickers.json').json()
    Hitbtc_ticker= requests.get('https://api.hitbtc.com/api/2/public/ticker').json()
    Acx = {}
    Hitbtc = {}
    for pair in Acx_pairs:
        bid = float(Acx_ticker[pair]['ticker']['buy'])
        ask = float(Acx_ticker[pair]['ticker']['sell'])
        Acx[pair]={'bid':bid,'ask':ask}
    for pair in Hitbtc_pairs:
        for element in Hitbtc_ticker:
            if element['symbol']==pair:
                bid = float(element['bid'])
                ask = float(element['ask'])
                Hitbtc[pair]={'bid':bid,'ask':ask}
 
    Book = {'Acx':Acx,'Hitbtc':Hitbtc}
    profit_1 = ((1/Book['Acx']['btcaud']['ask'])/Book['Hitbtc']['ETHBTC']['ask'])*Book['Acx']['ethaud']['bid']*0.99-1
    profit_2 = ((1/Book['Acx']['btcaud']['ask'])/Book['Hitbtc']['BCHBTC']['ask'])*Book['Acx']['bchaud']['bid']*0.99-1
    profit_3 = (1/Book['Acx']['ethaud']['ask'])*Book['Hitbtc']['ETHBTC']['bid']*Book['Acx']['btcaud']['bid']*0.99-1
    profit_4 = ((1/Book['Acx']['ethaud']['ask'])/Book['Hitbtc']['BCHETH']['ask'])*Book['Acx']['bchaud']['bid']*0.99-1
    profit_5 = (1/Book['Acx']['bchaud']['ask'])*Book['Hitbtc']['BCHBTC']['bid']*Book['Acx']['btcaud']['bid']*0.99-1
    profit_6 = (1/Book['Acx']['bchaud']['ask'])*Book['Hitbtc']['BCHETH']['bid']*Book['Acx']['ethaud']['bid']*0.99-1

    lst = [(profit_1,'AUD/BTC - BTC/ETH - ETH/AUD'),(profit_2,'AUD/BTC - BTC/BCH - BCH/AUD'),
           (profit_3,'AUD/ETH - ETH/BTC - BTC/AUD'),(profit_4,'AUD/ETH - ETH/BCH - BCH/AUD'),
           (profit_5,'AUD/BCH - BCH/BTC - BTC/AUD'),(profit_6,'AUD/BCH - BCH/ETH - ETH/AUD')]

    for i in lst:
        print(i)

    return lst

def auto(filename='Acx-HitBTC.csv'):
    csv = open(filename,'a')
    while True:
        lst = check_trips()
        for element in lst:
            if element[0] > 0:
                timestamp = time.time()
                fields = [str(timestamp),str(element[0]),str(element[1])]
                csv.seek(0,2)
                csv.writelines("\r")
                csv.writelines( (',').join(fields))