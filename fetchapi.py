import time
from time import gmtime, strftime
import urllib.request
import json
import psycopg2
from config import config

def connect():
	""" Connect to the PostgreSQL database server """
	conn = None
	try:
		# read connection parameters
		params = config()
		# connect to the PostgreSQL server
		print('Connecting to the PostgreSQL database...')
		conn = psycopg2.connect(**params)
		# create a cursor
		cur = conn.cursor()
		# display the PostgreSQL database server version
		db_version = cur.fetchone()
		print(db_version)
		# close the communication with the PostgreSQL
		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
			print('Database connection closed.')

def insert_coin_price_hist(table_name, coin_type, price, volume, mktcap):
    print("Inserting", coin_type, "into", table_name)
    sql = """INSERT INTO """ + table_name + """(time, coin_type, price, volume, mktcap)
                VALUES(%s, %s, %s, %s, %s)"""
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        timestmp = strftime("%Y-%m-%d %H:%M:%S")
        # execute the INSERT statement
        cur.execute(sql, (timestmp, coin_type, price, volume, mktcap))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def update_current_prices(table_name, coin_type, price, volume, mktcap):
    print("Updating", coin_type, "in", table_name)
    sql = """ UPDATE """ + table_name + """
                SET time= %s, coin_type= %s, price= %s, volume= %s, mktcap= %s
                WHERE coin_type = %s"""
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        timestmp = strftime("%Y-%m-%d %H:%M:%S")
        # execute the INSERT statement
        cur.execute(sql, (timestmp, coin_type, price, volume, mktcap, coin_type))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

##url = 'https://poloniex.com/public?command=returnTicker'
##url = 'https://www.cryptocompare.com/api/data/coinlist/'
coinlist = 'BTC,DASH,ETH,LTC,MCO,QTUM,ZEC'
url = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms='+ coinlist +'&tsyms=USD'
req = urllib.request.Request(url)
decoder = json.JSONDecoder()
r = urllib.request.urlopen(req).read()
parsed = json.loads(r.decode('utf-8'))

## Commment out the line below to disable JSON pretty-printing
#print(json.dumps(parsed, indent=3, sort_keys=False))
for coin in parsed['RAW']:
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

	insert_table = 'stocks_history'
	update_table = 'stocks_current_price_table'

	insert_coin_price_hist(insert_table, coin, price, volume, mktcap)
	#insert_coin_price_hist(update_table, coin, price, volume, mktcap)
	update_current_prices(update_table, coin, price, volume, mktcap)

	## More fields are available from parsed, however these are the
	## only values that should be necessary for us
	print()
