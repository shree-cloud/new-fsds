# 2.  Write a program to update a record via api
# 3 . Write a program to delete a record via api
# 4 . Write a program to fetch a record via api
# 5 . All the above questions you have to answer for mongo db as well .

from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)


client = pymongo.MongoClient("mongodb+srv://shree:haonabhai@cluster0.i1peq.mongodb.net/?retryWrites=true&w=majority")
database = client['taskdb']
collection = database['taskcollection']


# 1 . Write a program to insert a record in sql table via api database
@app.route("/insert/mongo", methods= ['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({name: number})
        return jsonify(str("succesfully inserted"))

if __name__ == '__main__':
    app.run()