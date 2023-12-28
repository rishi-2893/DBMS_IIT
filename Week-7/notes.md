1. Do not forget to import sys, os
2. Add semi colon at the end 
    ```python
    cur.execute("SELECT * FROM table;")
    ```
3. psycopg2.connect accepts named arguments
    - database, user, host, port, password
    - Note: **address** is NOT there
4. You can cut past using the tools given in the editor itself