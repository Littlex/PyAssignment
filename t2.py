import MySQLdb
from intercom.client import Client

intercom = Client(personal_access_token='my_personal_access_token')
db = MySQLdb.connect(host="localhost",  # your host 
                     user="root",       # username
                     passwd="root",     # password
                     db="pythonspot")   # name of the database
            
# Create a Cursor object to execute queries.
cur = db.cursor()
# Select data from table using SQL query.
cur.execute("SELECT * FROM table")

# suppose the table is like this:
"""
+----+---------------------------------+
| id | name   | email                  |
+----+--------+------------------------+
|  1 | David  | David@getmonument.com  |
|  2 | Tom    | Tom@getmonument.com    |
|  3 | Lily   | Lily@getmonument.com   |
+----+---------------------------------+
"""

for row in cur.fetchall() :
    # create users
    intercom.users.create(user_id=row[0], name=row[1], email=row[2])
db.close()

