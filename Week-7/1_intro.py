"""
Connecting to PostgresSQL using psycopg2
"""

import psycopg2


def connectDb(dbname, usrname, pwd, address, portnum):
    # storing connection object in this
    conn = None
    try:
        # Connect to the PostgreSQL DB
        conn = psycopg2.connect(
            database=dbname, user=usrname, password=pwd, host=address, port=portnum
        )
        print("Database connected successfully")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        # Close the connection
        conn.close()


connectDb("flis", "postgres", "password", "127.0.0.1", "5432")
