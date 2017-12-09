import sys
import urllib.request
import json
from databasefunctions import *

def main():
    file = open('coinlist.txt', "r")
    coinlist = ''
    for line in sorted(file):
    	coinlist = coinlist + line.rstrip() + ','
    coinlist = coinlist.rstrip(',')
    file.close()
    print("Successfully read coinlist: ", coinlist, end="\n\n")
    url = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms='+ coinlist +'&tsyms=USD'
    req = urllib.request.Request(url)
    decoder = json.JSONDecoder()
    r = urllib.request.urlopen(req).read()
    parsed = json.loads(r.decode('utf-8'))
    ## Commment out the line below to disable JSON pretty-printing
    #print(json.dumps(parsed, indent=3, sort_keys=False))
    insert_table = 'stocks_history'
    update_table = 'stocks_current_price_table'
    if (len(sys.argv) == 2):
        if sys.argv[1] == 'updatetables':
            truncate_current_table(update_table)

    for coin in sorted(parsed['RAW']):
        price = parsed['RAW'][coin]['USD']['PRICE']
        volume = parsed['RAW'][coin]['USD']['VOLUME24HOURTO']
        mktcap = parsed['RAW'][coin]['USD']['MKTCAP']
        change24hour = parsed['RAW'][coin]['USD']['CHANGE24HOUR']
        high24hour = parsed['RAW'][coin]['USD']['HIGH24HOUR']
        low24hour = parsed['RAW'][coin]['USD']['LOW24HOUR']
        supply = parsed['RAW'][coin]['USD']['SUPPLY']
        ## More fields are available from parsed, however these are the
        ## only values that should be necessary for us

        print(coin, "\tPRICE: ", price)
        print("\tVOLUME: ", volume)
        print("\tMKTCAP: ", mktcap)
        print("\tCHANGE24HOUR: ", change24hour)
        print("\tHIGH24HOUR: ", high24hour)
        print("\tLOW24HOUR: ", low24hour)
        print("\tSUPPLY: ", supply)

        if (len(sys.argv) != 2):
            insert_coin_price_hist(insert_table, coin, price, volume, mktcap)
            update_current_prices(update_table, coin, price, volume, mktcap)
        if (len(sys.argv) == 2):
            if sys.argv[1] == 'updatetables':
                print("INSERTING INTO FRESH TABLE")
                insert_coin_price_hist(update_table, coin, price, volume, mktcap)


        ## More fields are available from parsed, however these are the
        ## only values that should be necessary for us
        print()

# call main and execute
if __name__ == "__main__":main()
