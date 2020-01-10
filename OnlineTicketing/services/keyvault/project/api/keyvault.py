from flask import Blueprint, jsonify, request, render_template
from sqlalchemy import exc
from project.api.models import Keyvault
from project import db
import http.client
import json

keyvault_blueprint = Blueprint('keyvault', __name__, template_folder='./templates')



