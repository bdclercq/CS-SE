from flask import Blueprint, jsonify, request, render_template
from sqlalchemy import exc
import requests

banking_blueprint = Blueprint('ratings', __name__, template_folder='./templates')


@banking_blueprint.route('/banking', methods=['GET'])
def get_all():
    response_object = {
        'status': 'success',
        'data': {
            'message': 'Hello from the bank'
        }
    }
    return jsonify(response_object), 200

