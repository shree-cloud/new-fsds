# 1 . Write a program to insert a record in sql table via api database
# 2.  Write a program to update a record via api
# 3 . Write a program to delete a record via api
# 4 . Write a program to fetch a record via api
# 5 . All the above questions you have to answer for mongo db as well .

import mysql.connector as conn

mydb = conn.connect(host = "localhost" , user ="root" , passwd = "haonabhai" )
cursor = mydb.cursor()

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/abc',methods=['GET','POST'])
def test1():
    if(request.method=='POST'):
        a = request.json['a']
        b = request.json['b']
        c = request.json['c']
        d = request.json['d']
        e = request.json['e']
        cursor.execute("insert into shree.ineuron values(a,b,c,d,e)")
        mydb.commit()
        q2 = cursor.execute("select * from sudhanshu.ineuron1")
        return jsonify((q2))

if __name__=='__main__':
    app.run()



# "a":101,
#     "b":'sudhanshu kumar',
#     "c":'sudhanshu@ineuron.ai',
#     "d": 100,
#     "e":30