import psycopg2

db_config = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'password',
    'host': '127.0.0.1',
    'port': '5432'
}

# connection establishment
conn = psycopg2.connect(**db_config)

conn.autocommit = True

# Creating a cursor object
cursor = conn.cursor()

# query to create a database 
sql = "CREATE DATABASE learn_psycopg2;"

# executing above query
cursor.execute(sql)

# Closing the connection
conn.close()