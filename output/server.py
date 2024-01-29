from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database_name']
collection = db['users']

@app.route('/users', methods=['GET'])
def get_users():
    users = collection.find()
    return jsonify(list(users))

@app.route('/users', methods=['POST'])
def create_user():
    user = {
        'name': request.json['name'],
        'dept': request.json['dept']
    }
    result = collection.insert_one(user)
    return jsonify({'message': 'User created successfully', 'user': user}), 201

if __name__ == '__main__':
    app.run(port=3000)