from flask import Flask, render_template, request
import psycopg2

db_config = {
    'dbname': 'dbms_candidate_app', 
    'user': 'postgres',
    'password': 'password',
    'host': '127.0.0.1',
    'port': '5432'
}

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/savedetails', methods=['POST'])
def saveDetails():
    cno = request.form["cno"]
    name = request.form["name"]
    email = request.form["email"]
    conn = None


    try:
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor() # Create a new cursor

        cur.execute("INSERT INTO candidate (cno, name, email) VALUES (%s, %s, %s)", (cno, name, email))
        conn.commit() # Commit the changes to the DB
        cur.close() # Close the cursor

    except (Exception, psycopg2.DatabaseError) as error:
        render_template("fail.html")
    finally:

        if conn is not None:
            conn.close() # Close the connection

    return render_template("success.html")


@app.route("/viewall")
def viewAll():
    conn = None

    try:
        # Connect to the PostgreSQL DB
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor() # Create a new cursor

        # Execute the SELECT statement
        cur.execute("SELECT cno, name, email FROM Candidate")
        results = cur.fetchall() # Fetches all rows of the query result set
        cur.close() # Close the cursor
    
    except (Exception, psycopg2.DatabaseError) as error:
        render_template("fail.html")
    finally:
        conn.close() # Close the connection

    return render_template("viewall.html",rows = results)



if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=5000)