import mysql.connector
mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'roottoor',
        database = 'chi_cse'
    )
cur = mydb.cursor()
def upqq(id,name):
    cur.execute("update user set name=%s where id=%s",(name,id))
    mydb.commit()
    cur.close()
    mydb.close()

id = int(input("Enter the id: "))
name = input("Enter the name: ")
upqq(id,name)