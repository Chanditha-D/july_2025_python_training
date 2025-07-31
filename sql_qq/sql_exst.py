import mysql.connector
mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'roottoor',
        database = 'chi_cse'
    )
cur = mydb.cursor()
def email_exst(email):
    cur.execute("select COUNT(*) from user where email=%s",(email,))
    row = cur.fetchall()
    if row[0][0]>=1:
        return 1
    else:
        return 0

def email_inrt(id,name,email,password):
    cur.execute('insert into user(id,name,email,password) values(%s,%s,%s,%s)',(id,name,email,password))
    mydb.commit()
    cur.close()
    mydb.close()
    print("Record inserted.")

id = int(input("Enter id: "))
name = input("Enter name: ")
email = input("Enter the email: ")
password = input("Enter the password: ")
if not email_exst(email):
    email_inrt(id,name,email,password)
else:
    print("Record already exists.")