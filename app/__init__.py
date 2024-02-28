import logging
from flask import Flask
from flask_pymongo import PyMongo
from app.config import FLASK_ENV, MONGO_URI, LOG_FILE

logger = logging.getLogger(__name__)

# Create a global PyMongo instance
mongo = PyMongo()


def configure_logging():
    logging.basicConfig(level=logging.INFO)


def create_app():
    app = Flask(__name__)
    configure_logging()

    logger.info(f'FLASK_ENV: {FLASK_ENV}')

    # Initialize PyMongo with the Flask app
    app.config['MONGO_URI'] = MONGO_URI
    mongo.init_app(app)

    # Set up logging to write messages to a file
    if not app.debug:
        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    # Import and register blueprints
    from .routes.user_routes import app_blueprint as user_routes
    from .routes.item_routes import app_blueprint as item_routes
    app.register_blueprint(user_routes)
    app.register_blueprint(item_routes)

    return app
