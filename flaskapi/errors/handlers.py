"""
This module to handle the custom errors
"""
from flask import Blueprint, jsonify

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(400)
@errors.app_errorhandler(404)
def error_handler(error):
    return jsonify({'error': {
        'code': error.description['code'],
        'message': error.description['message']
    }}), error.code
