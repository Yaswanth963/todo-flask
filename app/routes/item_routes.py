from flask import Blueprint, request, jsonify, render_template

from app import mongo
from app.models.item import Item
from app.middleware.auth_middleware import token_required
import logging
from bson import ObjectId

# Get the logger for the current module
logger = logging.getLogger(__name__)

app_blueprint = Blueprint('item_routes', __name__)


@app_blueprint.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app_blueprint.route('/todos', methods=['POST'])
@token_required
def create_todo(current_user):
    try:
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        if not name:
            logger.warning('Name is required')
            return jsonify({'message': 'Name is required'}), 400

        todo = Item(name, description)
        mongo.db.todos.insert_one(todo.__dict__)  # converting object to dict
        logger.info('Item created successfully')
        return jsonify({'message': 'Item created successfully!'}), 201
    except Exception as e:
        logger.error(f'Error creating todo: {str(e)}')
        return jsonify({'message': 'An error occurred while creating todo'}), 500


@app_blueprint.route('/todos', methods=['GET'])
@token_required
def get_all_todos(current_user):
    try:
        todos = mongo.db.todos.find({})
        output = []
        for todo in todos:
            output.append({'id': str(todo['_id']), 'name': todo['name'], 'description': todo['description'],
                           'created_at': todo['created_at']})
        logger.info('All todos retrieved successfully')
        return jsonify({'todos': output}), 200
    except Exception as e:
        logger.error(f'Error retrieving todos: {str(e)}')
        return jsonify({'message': 'An error occurred while retrieving todos'}), 500


@app_blueprint.route('/todos/<todo_id>', methods=['GET'])
@token_required
def get_todo(current_user, todo_id):
    try:
        todo = mongo.db.todos.find_one({'_id': ObjectId(todo_id)})
        if not todo:
            logger.warning(f'Item with id {todo_id} not found')
            return jsonify({'message': 'Item not found!'}), 404
        logger.info(f'Item with id {todo_id} retrieved successfully')
        return jsonify({'id': str(todo['_id']), 'name': todo['name'], 'description': todo['description'],
                        'created_at': todo['created_at']}), 200
    except Exception as e:
        logger.error(f'Error retrieving todo: {str(e)}')
        return jsonify({'message': 'An error occurred while retrieving todo'}), 500


@app_blueprint.route('/todos/<todo_id>', methods=['PUT'])
@token_required
def update_todo(current_user, todo_id):
    try:
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        todo = mongo.db.todos.find_one({'_id': ObjectId(todo_id)})
        if not todo:
            logger.warning(f'Item with id {todo_id} not found')
            return jsonify({'message': 'Item not found!'}), 404
        mongo.db.todos.update_one({'_id': ObjectId(todo_id)},
                                  {'$set': {'name': name, 'description': description}})
        logger.info(f'Item with id {todo_id} updated successfully')
        return jsonify({'message': 'Item updated successfully!'}), 200
    except Exception as e:
        logger.error(f'Error updating todo: {str(e)}')
        return jsonify({'message': 'An error occurred while updating todo'}), 500


@app_blueprint.route('/todos/<todo_id>', methods=['DELETE'])
@token_required
def delete_todo(current_user, todo_id):
    try:
        todo = mongo.db.todos.find_one({'_id': ObjectId(todo_id)})
        if not todo:
            logger.warning(f'Item with id {todo_id} not found')
            return jsonify({'message': 'Item not found!'}), 404
        mongo.db.todos.delete_one({'_id': ObjectId(todo_id)})
        logger.info(f'Item with id {todo_id} deleted successfully')
        return jsonify({'message': 'Item deleted successfully!'}), 200
    except Exception as e:
        logger.error(f'Error deleting todo: {str(e)}')
        return jsonify({'message': 'An error occurred while deleting todo'}), 500
