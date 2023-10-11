import psycopg2

db_config = {
    'dbname': 'dbms_candidate_app',
    'user': 'postgres',
    'password': 'password',
    'host': '127.0.0.1',
    'port': '5432'
}

# connection object
conn = psycopg2.connect(**db_config)

# cursor
cur = conn.cursor()

# Schema
sql = """
CREATE TABLE candidate
(
cno INT PRIMARY KEY, 
name VARCHAR(30),
email VARCHAR(30)
)
"""

# executing
cur.execute(sql)

# committing
conn.commit()

cur.close()

# closing connection
conn.close()