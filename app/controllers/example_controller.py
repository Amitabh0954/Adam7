from flask import Blueprint, jsonify

example_bp = Blueprint('example', __name__)

@example_bp.route('/example', methods=['GET'])
def get_example():
    response = {'message': 'This is an example endpoint'}
    return jsonify(response)