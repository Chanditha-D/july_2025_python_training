import mysql.connector # type: ignore
def getdb():
    mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'roottoor',
            database = 'chi_cse'
        )
    cur = mydb.cursor()
    return mydb,cur