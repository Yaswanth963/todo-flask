import logging
from flask import Blueprint, request, jsonify
from datetime import datetime, timedelta
import bcrypt
import jwt
from app import mongo
from app.models.user import User
from app.config import SECRET_KEY

# Create a logger
logger = logging.getLogger(__name__)

app_blueprint = Blueprint('user_routes', __name__)


# JWT token generation
def generate_token(username):
    try:
        payload = {
            'username': username,
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        logger.info(f"JWT token generated for user '{username}'.")
        return token
    except Exception as e:
        logger.error(f"Failed to generate JWT token for user '{username}': {e}")
        raise


# Routes for user registration and login
@app_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = bcrypt.hashpw(data.get('password').encode('utf-8'), bcrypt.gensalt())
    existing_user = mongo.db.users.find_one({'username': username})

    if existing_user:
        logger.info(f"User registration failed: User '{username}' already exists.")
        return jsonify({'message': 'User already exists!'}), 400

    user = User(username, password)
    mongo.db.users.insert_one(user.__dict__)
    logger.info(f"User '{username}' registered successfully.")
    return jsonify({'message': 'User registered successfully!'}), 201


@app_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = mongo.db.users.find_one({'username': username})

    if not user or not bcrypt.checkpw(password.encode('utf-8'), user['password']):
        logger.info(f"Login failed: Invalid username or password for user '{username}'.")
        return jsonify({'message': 'Invalid username or password!'}), 401

    token = generate_token(username)
    logger.info(f"User '{username}' logged in successfully.")
    return jsonify({'token': token}), 200
