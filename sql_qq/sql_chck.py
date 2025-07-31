import mysql.connector

def check_user(email):
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'roottoor',
        database = 'chi_cse'
    )
    mycur = mydb.cursor()
    mycur.execute('select count(id) from user where email=%s',(email,))
    row = mycur.fetchall()
    if row[0][0] >= 1:
        print(row, "Record exists")
    else:
        print("Record doesn't exist")

    mycur.close()
    mydb.close()
   
email = input("Enter the email: ")
check_user(email)