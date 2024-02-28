from functools import wraps
from flask import request, jsonify
from app import mongo
import jwt
import logging
from app.config import SECRET_KEY

# Get the logger for the current module
logger = logging.getLogger(__name__)


# Middleware to intercept the desired routes for authentication
def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            logger.warning('Token is missing!')
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            secret_key = SECRET_KEY
            data = jwt.decode(token, secret_key, algorithms=['HS256'])
            current_user = mongo.db.users.find_one({'username': data['username']})
            logger.info(f'Token decoded successfully for user: {data["username"]}')
        except jwt.ExpiredSignatureError:
            logger.error('Token has expired!')
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            logger.error('Invalid token!')
            return jsonify({'message': 'Invalid token!'}), 401
        except Exception as e:
            logger.error(f'Error decoding token: {str(e)}')
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated_function
