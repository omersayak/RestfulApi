from flask import Flask, jsonify, request
from models import User, user_schema, users_schema
from api.app import db

app = Flask(__name__)


class UserController:
    @app.route('/users', methods=['GET'])
    def get_all_users():
        users = User.query.all()
        return jsonify(users_schema.dump(users))

    @app.route('/users/<int:user_id>', methods=['GET'])
    def get_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return jsonify({'message': 'User not found'})
        return jsonify(user_schema.dump(user))

    @app.route('/users', methods=['POST'])
    def add_user():
        username = request.json.get('username')
        email = request.json.get('email')
        password = request.json.get('password')
        if not username or not email or not password:
            return jsonify({'message': 'Please provide username, email and password'}), 400
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify(user_schema.dump(user))

    @app.route('/users/<int:user_id>', methods=['PUT'])
    def update_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return jsonify({'message': 'User not found'})
        username = request.json.get('username')
        email = request.json.get('email')
        password = request.json.get('password')
        if not username and not email and not password:
            return jsonify({'message': 'Please provide username, email or password to update'}), 400
        if username:
            user.username = username
        if email:
            user.email = email
        if password:
            user.password = password
        db.session.commit()
        return jsonify(user_schema.dump(user))

    @app.route('/users/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return jsonify({'message': 'User not found'})
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'})