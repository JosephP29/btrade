from time import gmtime, strftime
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

def insert_coin_price_hist(table_name, coin_type, price, volume, mktcap, change24hour):
    print("Inserting", coin_type, "into", table_name)
    sql = """INSERT INTO """ + table_name + """(time, coin_type, price, volume, mktcap, change24hour)
                VALUES(%s, %s, %s, %s, %s, %s)"""
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
        cur.execute(sql, (timestmp, coin_type, price, volume, mktcap, change24hour))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def update_current_prices(table_name, coin_type, price, volume, mktcap, change24hour):
    print("Updating", coin_type, "in", table_name)
    sql = """ UPDATE """ + table_name + """
                SET time= %s, coin_type= %s, price= %s, volume= %s, mktcap= %s, change24hour= %s
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
        cur.execute(sql, (timestmp, coin_type, price, volume, mktcap, change24hour, coin_type))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def truncate_current_table(table_name):
    print("Truncating", table_name)
    sql = """ TRUNCATE """ + table_name
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
        cur.execute(sql)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
