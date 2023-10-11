import psycopg2

db_config = {
    'dbname': 'learn_psycopg2',
    'user': 'postgres',
    'password': 'password',
    'host': '127.0.0.1',
    'port': '5432'
}

def selectAll():
    conn = None

    try:
        # Connect to the PostgreSQL DB
        conn = psycopg2.connect(**db_config)

        cur = conn.cursor() # Create a new cursor

        # Execute the SELECT statement
        cur.execute("SELECT emp_num, emp_name, department FROM EMPLOYEE")
        rows = cur.fetchall() # Fetches all rows of the query result set

        for row in rows:
            print (("Employee ID = ", row[0], ", NAME = ", row[1], ", DEPARTMENT = ", row[2]))

        cur.close() # Close the cursor

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        conn.close() # Close the connection

selectAll()