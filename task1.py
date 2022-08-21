# 1 . Write a program to insert a record in sql table via api database
# 2.  Write a program to update a record via api
# 3 . Write a program to delete a record via api
# 4 . Write a program to fetch a record via api
# 5 . All the above questions you have to answer for mongo db as well .

from flask import Flask, request, jsonify
import mysql.connector as conn

app = Flask(__name__)

mydb = conn.connect(host = "localhost" , user ="root" , passwd = "haonabhai" )
cursor = mydb.cursor()
cursor.execute("create database if not exists shree")
cursor.execute("create table if not exists shree.ineuron(name varchar(30), number int)")



# @app.route('/abc',methods=['GET','POST'])
# def test1():
#     if(request.method=='POST'):
#
#
# if __name__=='__main__':
#     app.run()



