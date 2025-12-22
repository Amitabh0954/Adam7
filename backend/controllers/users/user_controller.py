from flask import Blueprint, request, jsonify
from backend.services.users.user_service import UserService

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    try:
        user = UserService.register_user(data['username'], data['email'], data['password'])
        response = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'image_file': user.image_file,
            'created_at': user.created_at.isoformat()
        }
        return jsonify(response), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    try:
        user = UserService.authenticate_user(data['email'], data['password'])
        response = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'image_file': user.image_file,
            'created_at': user.created_at.isoformat()
        }
        return jsonify(response), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 401