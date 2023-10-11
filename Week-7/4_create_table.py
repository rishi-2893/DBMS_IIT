import psycopg2

db_config = {
    'dbname': 'learn_psycopg2',
    'user': 'postgres',
    'password': 'password',
    'host': '127.0.0.1',
    'port': '5432'
}

def createTable():
    conn = None

    try:
        conn = psycopg2.connect(**db_config)

        cur = conn.cursor() # Create a new cursor
        cur.execute('''
                    CREATE TABLE EMPLOYEE \
                    (emp_num INT PRIMARY KEY NOT NULL, \
                    emp_name VARCHAR(40) NOT NULL, \
                    department VARCHAR(40) NOT NULL)
                    ''')

        conn.commit() # Commit the changes to the DB
        print("Table created successfully")
        
        cur.close() # close the cursor

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
                  
    finally:
        if conn is not None:
            conn.close()

createTable()