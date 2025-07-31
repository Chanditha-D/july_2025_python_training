from flask import Flask, jsonify,request,render_template # type: ignore
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'roottoor'
app.config['MYSQL_DB'] = 'chi_cse'

mysql = MySQL(app)

@app.route('/')
def hello_world():
    return "homee"


@app.route('/register', methods=["GET","POST"])
def regst_sv():
    if request.method=="GET":
        return render_template("home.html")
    else:
        name = request.form.get("name")
        email = request.form.get("email")
        passw = request.form.get("passw")
        cur=mysql.connection.cursor()
        val = [name,email,passw]
        cur.execute("INSERT INTO ruser VALUES (%s,%s,%s)",val)
        mysql.connection.commit()
        cur.close()
        return "Record inserted"

@app.route('/getData')
def getData():
    id = request.args.get("id")
    cur = mysql.connection.cursor()
    if id is None:
        cur.execute("SELECT * FROM user")
    else:
        cur.execute("SELECT * FROM user WHERE id=%s",(id,))
    row = cur.fetchall()
    cur.close()
    return render_template("userlist.html",userlist=row)

if __name__=='__main__':
    app.run()

# @app.route('/<nnnn>')
# def hommyy(nnnn):
#     return jsonify(("how","are","you",nnnn))


# @app.route('/myhtml')
# def myhh():
#     return render_template("home.html")

# @app.route('/mydetails',methods=["get","post"])
# def mydet():
#     name = request.args.get("na")
#     college = request.args.get("cc")
#     addrr = request.args.get("aa")
#     return jsonify(f"name={name}   college={college}   address={addrr}")

