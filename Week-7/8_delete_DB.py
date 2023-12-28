import psycopg2

db_config = {
    "dbname": "postgres",  # Connect to the 'postgres' database
    "user": "postgres",
    "password": "password",
    "host": "127.0.0.1",
    "port": "5432",
}


def dropDB(DB_name):
    conn = None

    try:
        # Connect to the PostgreSQL DB
        conn = psycopg2.connect(**db_config)
        conn.autocommit = (
            True  # Set autocommit mode to avoid running inside a transaction
        )

        cur = conn.cursor()  # Create a new cursor

        # Build and execute the SQL query to drop the database
        query = "DROP DATABASE IF EXISTS %s;" % DB_name
        cur.execute(query)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()  # Close the connection


dropDB("learn_psycopg2")
