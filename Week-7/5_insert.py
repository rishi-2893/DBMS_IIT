import psycopg2

db_config = {
    'dbname': 'learn_psycopg2',
    'user': 'postgres',
    'password': 'password',
    'host': '127.0.0.1',
    'port': '5432'
}


def insertRecord(num, name, dept):
    conn = None

    try:
        # Connect to the PostgreSQL DB
        conn = psycopg2.connect(**db_config)

        cur = conn.cursor() # Create a new cursor

        # Execute the INSERT statement
        cur.execute("INSERT INTO EMPLOYEE (emp_num, emp_name, department) \
        VALUES (%s, %s, %s);", (num, name, dept))

        conn.commit() # Commit the changes to the DB
        print ("Total number of rows inserted :", cur.rowcount)
        cur.close() # close the cursor

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

insertRecord(110, 'Bhaskar', 'HR')
insertRecord(109, 'Bhaskar', 'IT')
insertRecord(111, 'Ananya', 'HR')
insertRecord(102, 'Elon', 'Eng')