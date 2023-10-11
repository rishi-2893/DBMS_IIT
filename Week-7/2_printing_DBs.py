import psycopg2


db_config = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'password',
    'host': '127.0.0.1',
    'port': '5432'
}


# Establish a connection to the PostgreSQL server
connection = psycopg2.connect(**db_config)

# Create a cursor object
cursor = connection.cursor()

# Execute the SQL command to list all databases
list_databases_command = "SELECT datname FROM pg_database"

cursor.execute(list_databases_command)

# Fetch and print the database names
database_names = cursor.fetchall()

for db_name in database_names:
    print(db_name[0])

# Close the connection
connection.close()