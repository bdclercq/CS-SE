from flask import Blueprint, jsonify, request, render_template
from sqlalchemy import exc
import requests
import random, time

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


@banking_blueprint.route('/pay_tickets/<amount>/<credit_card>', methods=['GET'])
def pay_tickets(amount, credit_card):
    response_object = {
        'status': 'success',
        'data': 'Transaction succeeded'
    }
    transactiontime = random.randint(1, 5)/100.0
    time.sleep(transactiontime)
    rand = random.randint(0, 100)
    if rand%5:
        return jsonify(response_object), 200
    else:
        response_object['status'] = 'fail'
        response_object['data'] = 'Not enough funds left.'
        return jsonify(response_object), 400
