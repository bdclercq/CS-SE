from flask import Blueprint, jsonify, request, render_template
from sqlalchemy import exc
from project.api.models import Ticket
from project import db

tickets_blueprint = Blueprint('tickets', __name__, template_folder='./templates')


@tickets_blueprint.route('/get_tickets', methods=['GET'])
def get_users():
    """Get all users"""
    response_object = {
        'status': 'success',
        'data': {
            'tickets': [ticket.to_json() for ticket in Ticket.query.all()]
        }
    }
    return jsonify(response_object), 200

