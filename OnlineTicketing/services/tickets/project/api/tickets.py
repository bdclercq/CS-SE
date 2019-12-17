from flask import Blueprint, jsonify, request, render_template
from sqlalchemy import exc
from project.api.models import Ticket
from project import db
from datetime import datetime, date, time

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


@tickets_blueprint.route('/check_available/<amount>/<dfrom>/<dto>', methods=['POST', 'GET'])
def check_available(amount, dfrom, dto):
    response_object = {
        'status': 'success',
        'data': 'Success!'
    }
    ticket_time = time()
    from_date = date.fromisoformat(dfrom)
    to_date = date.fromisoformat(dto)
    from_stamp = datetime.combine(from_date, ticket_time)
    to_stamp = datetime.combine(to_date, ticket_time)
    print(from_stamp, to_stamp)
    exists = db.session.query(Ticket.period_from, Ticket.period_to).filter_by(period_from=from_stamp, period_to=to_stamp).scalar() is not None
    print(exists)
    if exists:
        print('Record exists')
        record = Ticket.query.filter_by(period_from=from_stamp, period_to=to_stamp).first()
        val = record.amount
        amount = int(amount)
        if val >= amount:
            val = val - amount
            record.amount = val
            db.session.commit()
            return jsonify(response_object), 200
        else:
            response_object['status'] = 'fail'
            response_object['data'] = 'Not enough tickets left.'
            return jsonify(response_object), 400
    else:
        response_object['status'] = 'fail'
        response_object['data'] = 'Cannot find tickets for specified period {0} - {1}'.format(datetime(dfrom), datetime(dto))
        return jsonify(response_object), 400


@tickets_blueprint.route('/release_tickets/<amount>/<dfrom>/<dto>', methods=['POST', 'GET'])
def release_tickets(amount, dfrom, dto):
    response_object = {
        'status': 'success',
        'data': 'Success!'
    }
    ticket_time = time()
    from_date = date.fromisoformat(dfrom)
    to_date = date.fromisoformat(dto)
    from_stamp = datetime.combine(from_date, ticket_time)
    to_stamp = datetime.combine(to_date, ticket_time)
    exists = db.session.query(Ticket.period_from, Ticket.period_to).filter_by(period_from=from_stamp, period_to=to_stamp).scalar() is not None
    if exists:
        print('Record exists')
        record = Ticket.query.filter_by(period_from=from_stamp, period_to=to_stamp).first()
        val = record.amount
        amount = int(amount)
        val = val + amount
        record.amount = val
        db.session.commit()
        return jsonify(response_object), 200
    else:
        response_object['status'] = 'fail'
        response_object['data'] = 'Cannot find tickets for specified period {0} - {1}'.format(datetime(dfrom), datetime(dto))
        return jsonify(response_object), 400
