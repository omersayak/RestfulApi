from functools import wraps
from flask import g, request, jsonify
import jwt
from api.app.utils.database import db
from api.app.models.user import User

def check_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(' ')[1]
        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        try:
            data = jwt.decode(token, 'SECRET_KEY')
            user = User.query.filter_by(id=data['id']).first()
            g.user = user
        except:
            return jsonify({'message': 'Token is invalid'}), 401
        return func(*args, **kwargs)
    return wrapper