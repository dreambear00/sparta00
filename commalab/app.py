from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

import requests
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

# API 역할을 하는 부분
@app.route('/commalab', methods=['POST'])
def buying():
    name_receive = request.form['name_give']
    phone_receive = request.form['phone_give']
    address_receive = request.form['address_give']
    number_receive = request.form['number_give']

    purchase = {
        'name': name_receive,
        'phone': phone_receive,
        'address': address_receive,
        'number': number_receive,
    }

    db.purchases.insert_one(purchase)
    return jsonify({'result': 'success', 'msg': '주문이 완료되었습니다. 즐거운 하루 보내세요!'})

@app.route('/commalab', methods=['GET'])
def read_reviews():
    purchases = list(db.purchases.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'purchases': purchases})

if __name__ == '__main__':
    app.run(port=5000, debug=True)