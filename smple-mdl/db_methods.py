from db_lib import getdb
class dbmethods_lst:
    def insrt(values):
        mydb,cur = getdb()
        cur.execute("INSERT INTO hobbies(id,user_id,description) VALUES (%s,%s,%s)",(values))
        mydb.commit()
        print("1 Record inserted.")
        cur.close()
        mydb.close()
    def update(id,name):
        mydb,cur = getdb()
        cur.execute("update hobbies set description=%s where id=%s",(name,id))
        mydb.commit()
        print("Updated!")
        cur.close()
        mydb.close()
    def select():
        mydb,cur = getdb()
        cur.execute(f"SELECT * FROM hobbies")
        row = cur.fetchall()
        # for x in row:
        #     print(x)
        cur.close()
        mydb.close()
        print(row)
    def delete(id):
        mydb,cur = getdb()
        cur.execute("DELETE FROM hobbies WHERE id=%s",(id,))
        mydb.commit()
        print("Deleted!")
        cur.close()
        mydb.close()