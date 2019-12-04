from flask import Blueprint, jsonify, request, render_template, redirect
import requests
import json

UI_blueprint = Blueprint('interface', __name__, template_folder='./templates')


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
