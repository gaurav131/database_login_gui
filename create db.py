import sqlite3
conn = sqlite3.connect('user.db')
conn.execute('''CREATE TABLE Authentication
         (USERID INT PRIMARY KEY     NOT NULL,
         PASSWORD       TEXT    NOT NULL,
         NAME           TEXT    NOT NULL);''')
print ("Table created successfully")
conn.close()
