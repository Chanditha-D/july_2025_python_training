import mysql.connector

def insert_d(id,name,email,password):
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'roottoor',
        database = 'chi_cse'
    )
    mycur = mydb.cursor()
    sql = 'insert into user(id,name,email,password) values(%s,%s,%s,%s)'
    val = (id,name,email,password)
    mycur.execute(sql,val)      #mycur.execute("insert into user(id,name,email,password) values(%s,%s,%s,%s)",(id,name,email,password))
    mydb.commit()
    mycur.close()
    mydb.close()
    print(mycur.rowcount,"record inserted.")

id = int(input("Enter id: "))
name = input("Enter name: ")
email = input("Enter the email: ")
password = input("Enter the password: ")

insert_d(id,name,email,password)
