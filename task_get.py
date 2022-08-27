import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", passwd="haonabhai" )
cursor = mydb.cursor()
cursor.execute("create database if not exists shree")
cursor.execute("create table if not exists shree.ineuron(name varchar(30), number int)")

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/fetch-data")
def test():
    db_name = request.args.get("db_name")
    table_name = request.args.get("table_name")
    cursor.execute("select * from {}.{}".format(db_name, table_name))
    data = cursor.fetchall()
    mydb.commit()
    return jsonify(data)


# @app.route("/testfun")
# def test():
#     get_name = request.args.get("get_name")
#     mobile_number = request.args.get("mobile")
#     mail_id = request.args.get("mail_id")
#     return "this is a first GET function {} {} {}".format(get_name, mobile_number, mail_id)

if __name__ == '__main__':
    app.run(port=5002)