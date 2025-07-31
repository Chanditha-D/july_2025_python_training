import mysql.connector
mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'roottoor',
        database = 'chi_cse'
    )
cur = mydb.cursor()
cur.execute("SELECT * FROM user")
row = cur.fetchall()
for x in row:
    print(x)