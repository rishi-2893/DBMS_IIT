import psycopg2

db_config = {
    'dbname': 'learn_psycopg2',
    'user': 'postgres',
    'password': 'password',
    'host': '127.0.0.1',
    'port': '5432'
}

def deleteRecord(num):
    conn = None

    try:
        # Connect to the PostgreSQL DB
        conn = psycopg2.connect(**db_config)
    
        cur = conn.cursor() # Create a new cursor

        # Execute the DELETE statement
        cur.execute("DELETE FROM EMPLOYEE WHERE emp_num = %s", (num,))
    
        conn.commit() # Commit the changes to the DB
    
        print ("Total number of rows deleted :", cur.rowcount)
        cur.close() # Close the cursor

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        conn.close() # Close the connection

deleteRecord(110)