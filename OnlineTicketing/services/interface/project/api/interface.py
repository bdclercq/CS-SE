from flask import Blueprint, jsonify, request, render_template, redirect, g
import requests
import json
import time
from datetime import datetime

UI_blueprint = Blueprint('interface', __name__, template_folder='./templates')


@UI_blueprint.before_request
def before_request():
    g.request_start_time = time.time()
    g.request_time = lambda: "%.5fs" % (time.time() - g.request_start_time)

################################################################


@UI_blueprint.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

################################################################


@UI_blueprint.route('/Users', methods=['GET'])
def user_management():
    # usrs = requests.get("http://users:5001/get_users")
    return render_template("users.html")#, users=usrs.json()['data']['users'])


@UI_blueprint.route('/add_user', methods=['POST'])
def add_user():
    result = request.form
    # mail = result['email']
    # pwd = result['pwd']
    # data = json.dumps({'email': mail, 'password': pwd}), 200
    status = requests.post("http://users:5001/add_user", data=result)
    result = status.json()
    # print(result)
    if result['status'] == "fail":
        return render_template('users.html', message=result['message'])#,users=requests.get("http://users:5001/get_users").json()['data']['users'])
    else:
        return render_template('index.html', message=result['message'])#,users=requests.get("http://users:5001/get_users").json()['data']['users'])

################################################################


@UI_blueprint.route('/Tickets', methods=['GET'])
def ticket_management():
    tickets = requests.get("http://tickets:5004/get_tickets")
    return render_template("tickets.html", tickets=tickets.json()['data']['tickets'])


@UI_blueprint.route('/Tickets/buy/<dfrom>/<dto>', methods=['POST', 'GET'])
def buy_tickets(dfrom, dto):
    from_stamp = datetime.strptime(dfrom, '%a, %d %b %Y %H:%M:%S %Z')
    to_stamp = datetime.strptime(dto, '%a, %d %b %Y %H:%M:%S %Z')
    print(from_stamp, to_stamp)
    return render_template("buy_tickets.html", period=(from_stamp.date(), to_stamp.date()))


@UI_blueprint.route('/place_order', methods=['POST'])
def place_order():
    result = request.form
    mail = result['email']
    pwd = result['password']
    amount = result['amount']
    total = result['total']
    dfrom = result['dfrom']
    dto = result['dto']
    print(mail, pwd, amount, total, dfrom, dto)
    tickets = requests.get("http://tickets:5004/get_tickets")
    auth = requests.get("http://users:5001/authenticate/{0},{1}".format(mail, pwd)).json()
    if auth['status'] == 'success':
        status = requests.get("http://tickets:5004/check_available/{0}/{1}/{2}".format(amount, dfrom, dto)).json()
        if status['status'] == 'success':
            creditcard = requests.get("http://users:5001/get_creditcard/{0},{1}".format(mail, pwd)).json()['data']['creditcard']
            bank_status = requests.get("http://banking:5002/pay_tickets/{0}/{1}/{2}".format(amount, creditcard, mail)).json()
            if bank_status['status'] == 'success':
                tickets = requests.get("http://tickets:5004/get_tickets")
            else:
                release = requests.get("http://tickets:5004/release_tickets/{0}/{1}/{2}".format(amount, dfrom, dto)).json()
                if not release['status'] == 'success':
                    return render_template("tickets.html", tickets=tickets.json()['data']['tickets'],
                                           message='Something went wrong releasing tickets')
        return render_template("tickets.html", tickets=tickets.json()['data']['tickets'], message=status['data'])
    else:
        return render_template("tickets.html", tickets=tickets.json()['data']['tickets'], message='Authentication failed')
