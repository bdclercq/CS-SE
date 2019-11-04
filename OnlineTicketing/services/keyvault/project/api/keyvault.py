from flask import Blueprint, jsonify, request, render_template
from sqlalchemy import exc
from project.api.models import Keyvault
from project import db
import http.client
import json

keyvault_blueprint = Blueprint('keyvault', __name__, template_folder='./templates')


@keyvault_blueprint.route('/keyvault/encrypt', methods=['GET'])
def encrypt():
    response_object = {
        'status': 'success',
        'data': {
            'encrypted': ""
        }
    }
    return jsonify(response_object), 200


@keyvault_blueprint.route('/keyvault/decrypt', methods=['GET'])
def decrypt():
    response_object = {
        'status': 'success',
        'data': {
            'decrypted': ""
        }
    }
    return jsonify(response_object), 200

