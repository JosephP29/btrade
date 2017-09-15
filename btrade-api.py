import time
import urllib.request
import json
import psycopg2
from config import config

def config(filename='database.ini', section='postgresql'):
	# create a parser
	parser = ConfigParser()
	# read config file
	parser.read(filename)

	# get section, default postgresql
	db = {}
	if parser.has_section(section):
		params = parser.items(section)
		for param in params:
			db[param[0]] = param[1]
	else:
		raise Exception('Section {0} not found in the {1} file'.format(section, filename))

	return db

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
				print('Database connectin closed.')


## This function creates a new table in postgres
def create_table():
	""" create table in the PostgreSQL database"""
	## USING F STRINGS, new to Python v3
	day = currentDay
	commands = (
		f"""
		CREATE TABLE prices_{day} (
			id serial primary key,
			time time,
			coin_type text,
			price real,
			volume real,
			mktcap real
		)
		""")


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
	print(coin, "\tMKTCAP: ", parsed['RAW'][coin]['USD']['MKTCAP'])
	print("\tPRICE: ", parsed['RAW'][coin]['USD']['PRICE'])
	print("\tCHANGE24HOUR: ", parsed['RAW'][coin]['USD']['CHANGE24HOUR'])
	print("\tVOLUME24HOUR: ", parsed['RAW'][coin]['USD']['VOLUME24HOURTO'])
	print("\tHIGH24HOUR: ", parsed['RAW'][coin]['USD']['HIGH24HOUR'])
	print("\tLOW24HOUR: ", parsed['RAW'][coin]['USD']['LOW24HOUR'])
	print("\tSUPPLY: ", parsed['RAW'][coin]['USD']['SUPPLY'])
	## More fields are available from parsed, however these are the 
	## only values that should be necessary for us
	print()


