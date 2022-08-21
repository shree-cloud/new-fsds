# 5 . All the above questions you have to answer for mongo db as well .

from flask import Flask, request, jsonify
import mysql.connector as conn

app = Flask(__name__)

mydb = conn.connect(host = "localhost" , user ="root" , passwd = "haonabhai" )
cursor = mydb.cursor()
cursor.execute("create database if not exists shree")
cursor.execute("create table if not exists shree.ineuron(name varchar(30), number int)")



# 1 . Write a program to insert a record in sql table via api database
@app.route('/insert',methods=['POST'])
def insert():
    if(request.method=='POST'):
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into shree.ineuron values(%s, %s)",(name, number))
        mydb.commit()
        return jsonify(str('succesfully inserted'))


# 2.  Write a program to update a record via api
@app.route("/update",methods=['POST'])
def update():
    if request.method=='POST':
        get_name = request.json['get_name']
        cursor.execute("update shree.ineuron set number = number+500 where name = %s", (get_name,))
        mydb.commit()
        return jsonify(str('update successful'))


# 3 . Write a program to delete a record via api
@app.route("/delete",methods=['POST'])
def delete():
    if request.method == 'POST':
        name_del = request.json['name_del']
        cursor.execute("delete from shree.ineuron where name = %s",(name_del,))
        mydb.commit()
        return jsonify(str("delete successful"))


# 4 . Write a program to fetch a record via api
@app.route("/fetch",methods = ['POST','GET'])
def fetch_data():
    cursor.execute("select * from shree.ineuron")
    l = []
    for i in cursor.fetchall():
        l.append(i)
    return jsonify(str(l))

if __name__=='__main__':
    app.run()



