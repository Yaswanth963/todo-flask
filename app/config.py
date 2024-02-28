import os
import uuid

SECRET_KEY = os.environ.get('SECRET_KEY') or 'e1f13411ba2d47b3bd2781ece4db1c'
MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/todo_db'
FLASK_DEBUG = os.getenv('FLASK_DEBUG') or False
FLASK_ENV = os.environ.get('FLASK_ENV') or 'dev'
LOG_FILE = '/var/log/todo/flask_app_todo.log'

# generating secret key for dev testing purpose
# if __name__ == '__main__':
#     secret_key = str(uuid.uuid4().hex)
#     print(secret_key)
