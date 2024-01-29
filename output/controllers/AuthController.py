from flask import request, jsonify, make_response
from models import UserModel
import jwt
import bcrypt

count = 0
errors = None

def handle_errors(err):
    errors = {"email": "", "password": "", "username": ""}
    
    if hasattr(err, "code") and err.code == 11000:
        field = list(err.details['keyPattern'].keys())[0]
        if field == 'username':
            errors["username"] = "This username is already in use"
        elif field == 'email':
            errors["email"] = "This email is already registered"
    else:
        if "username" in err.errors:
            errors["username"] = err.errors["username"]
        if "email" in err.errors:
            errors["email"] = err.errors["email"]
        if "password" in err.errors:
            errors["password"] = err.errors["password"]
    
    return errors

def handle_errors1(err):
    errors = {"email": "", "password": ""}
    if str(err) == "incorrect email":
        errors["email"] = "Incorrect email"
    elif str(err) == "incorrect password":
        errors["password"] = "Incorrect password"
    
    return errors

def create_token(id):
    secret_key = 'soham post application secret'
    token_data = {"id": id}
    token = jwt.encode(token_data, secret_key, algorithm='HS256').decode('utf-8')
    return token

def signup_get():
    pass

def signup_post():
    global errors
    data = request.json
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    try:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        posts_liked = []
        posts_disliked = []
        user = UserModel(username=username, email=email, password=hashed_password, postsLiked=posts_liked, postsDisliked=posts_disliked)
        user.save()
        token = create_token(user.id)
        return make_response(jsonify(token), 201)
    except Exception as err:
        errors = handle_errors(err)
        return make_response(jsonify({"errors": errors}), 201)

def login_get():
    pass

def login_post():
    global errors
    data = request.json
    email = data.get("email")
    password = data.get("password")

    try:
        user = UserModel.login(email, password)
        token = create_token(user.id)
        return make_response(jsonify({"user": str(user.id), "token": token}), 200)
    except Exception as err:
        errors = handle_errors1(err)
        return make_response(jsonify({"errors": errors}), 201)

def auth():
    global errors, count
    token = request.json.get("token")
    count += 1

    try:
        decoded_token = jwt.decode(token, 'soham post application secret', algorithms=['HS256'])
        user = UserModel.objects.get(id=decoded_token["id"])
        return make_response(jsonify({"user": str(user.id)}), 200)
    except jwt.ExpiredSignatureError:
        return make_response(jsonify("false"), 200)
    except jwt.InvalidTokenError:
        return make_response(jsonify("false"), 200)
    except Exception as err:
        print(err)
        return make_response(jsonify("false"), 200)
