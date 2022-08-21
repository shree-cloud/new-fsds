from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/abc',methods=['GET','POST'])
def test1():
    if(request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a + b
        return jsonify((str(result)))


@app.route('/abc1/shree', methods=['GET', 'POST'])
def test2():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a * b
        return jsonify((str(result)))

@app.route('/abc1/shree/test3', methods=['GET', 'POST'])
def test3():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a / b
        return jsonify((str(result)))

@app.route('/abc1/shree/test4', methods=['GET', 'POST'])
def test4():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = b**2
        return jsonify((str(result)))

if __name__=='__main__':
    app.run()


# 1 . Write a program to insert a record in sql table via api database
# 2.  Write a program to update a record via api
# 3 . Write a program to delete a record via api
# 4 . Write a program to fetch a record via api
# 5 . All the above questions you have to answer for mongo db as well .