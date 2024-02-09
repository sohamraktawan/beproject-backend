from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import ObjectId
import bcrypt
import jwt
import time
import os
from dotenv import load_dotenv
import certifi

load_dotenv()

app = Flask(__name__)
app.config['MONGO_URI'] = os.getenv('db_connect')
mongo = PyMongo(app, tlsCAFile=certifi.where())

task_collection = mongo.db.tasks
user_collection = mongo.db.users

expireTime = 86400

def create_token(id):
    return jwt.encode({'id': str(id)}, 'soham post application secret', algorithm='HS256')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    postsLiked = []
    postsDisliked = []
    
    try:
        user = {
            'username': username,
            'email': email,
            'password': hashed_password,
            'postsLiked': postsLiked,
            'postsDisliked': postsDisliked
        }
        user_id = user_collection.insert_one(user).inserted_id
        token = create_token(user_id)
        return jsonify({'token': token}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']
    
    user = user_collection.find_one({'email': email})
    
    if user:
        if bcrypt.checkpw(password.encode('utf-8'), user['password']):
            token = create_token(user['_id'])
            return jsonify({'token': token}), 200
        else:
            return jsonify({'error': 'Incorrect password'}), 400
    else:
        return jsonify({'error': 'Incorrect email'}), 400

@app.route('/auth', methods=['POST'])
def auth():
    token = request.json['token']
    
    try:
        decoded_token = jwt.decode(token, 'soham post application secret', algorithms=['HS256'])
        user = user_collection.find_one({'_id': ObjectId(decoded_token['id'])})
        if user:
            return jsonify({'user': str(user['_id'])}), 200
        else:
            return jsonify({'error': 'User not found'}), 400
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token expired'}), 400
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 400

@app.route('/create', methods=['POST'])
def create_task():
    timeDue = request.json['timeDue']
    username = request.json['username']
    title = request.json['title']
    desc = request.json['desc']
    priority = request.json['priority']
    status = 'assigned'
    
    new_task = {
        'timeDue': timeDue,
        'username': username,
        'title': title,
        'desc': desc,
        'priority': priority,
        'status': status
    }
    
    try:
        task_id = task_collection.insert_one(new_task).inserted_id
        return jsonify({'message': 'Task created successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = task_collection.find()
    result = []
    
    for task in tasks:
        task['_id'] = str(task['_id'])
        result.append(task)
    
    return jsonify(result), 200

@app.route('/complete', methods=['POST'])
def complete_task():
    task_id = request.json['id']
    
    task = task_collection.find_one({'_id': ObjectId(task_id)})
    
    if task:
        if task['timeDue'] - time.time() > 0:
            task_collection.update_one({'_id': ObjectId(task_id)}, {'$set': {'status': 'completed'}})
        else:
            task_collection.update_one({'_id': ObjectId(task_id)}, {'$set': {'status': 'completed-late'}})
        
        return jsonify({'message': 'Task marked as complete'}), 200
    else:
        return jsonify({'error': 'Task not found'}), 400

@app.route('/delete', methods=['POST'])
def delete_task():
    task_id = request.json['id']
    
    task = task_collection.find_one({'_id': ObjectId(task_id)})
    
    if task:
        task_collection.delete_one({'_id': ObjectId(task_id)})
        return jsonify({'message': 'Task deleted successfully'}), 200
    else:
        return jsonify({'error': 'Task not found'}), 400

if __name__ == '__main__':
    app.run(port=int(os.getenv('PORT', 3001)))
