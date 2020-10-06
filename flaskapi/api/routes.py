from flask import Blueprint, request, abort, jsonify
from flaskapi.models import User
from flaskapi import db
from datetime import datetime


api = Blueprint('api', __name__)


@api.route('/users', methods=['GET'])
def list_users():
    """
    To get users list
    :return: users list
    """
    # To get query parameter
    q_limit = request.args.get('limit', default=-1, type=int)
    q_offset = request.args.get('offset', default=0, type=int)

    if q_limit == -1:
        users = User.query.all()
    else:
        users = User.query.offset(q_offset).limit(q_limit)

    return jsonify({'users': [user.to_dict() for user in users]})


@api.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id=None):
    """
    To get user information
    :return: user information
    """
    user = User.query.filter_by(id=user_id).first()
    if not user:
        abort(404, {'code': 'Not found', 'message': 'User not found'})

    return jsonify(user.to_dict())


@api.route('/users', methods=['POST'])
def post_user():
    """
    Post the user info to the db
    :return: return posted user
    """

    data = request.json
    name = data.get('name')
    email = data.get('email')

    user = User(name, email)
    db.session.add(user)
    db.session.commit()

    response = jsonify(user.to_dict())
    response.headers['Location'] = '/users/%d' % user.id
    return response


@api.route('/users/<user_id>', methods=['PUT'])
def put_user(user_id):
    """
    To update the user info
    :param user_id: user id
    :return: Updated user info
    """
    user = User.query.filter_by(id=user_id).first()
    if not user:
        abort(404, {'code': 'Not found', 'message': 'User not found'})

    data = request.json
    user.name = data.get('name')
    user.email = data.get('email')
    user.update_time = datetime.utcnow()
    db.session.commit()
    return jsonify(user.to_dict())


@api.route('/users/<user_id>', methods=['DELETE'])
def del_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        abort(404, {'code': 'Not found', 'message': 'User not found'})
    db.session.delete(user)
    db.session.commit()

    return jsonify(None), 204
