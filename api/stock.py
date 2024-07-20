import json, jwt
from flask import Blueprint, request, jsonify, current_app, Response, g
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
from auth_middleware import token_required

from model.users import User, StockUser

stock_api = Blueprint('stock_api', __name__,
                   url_prefix='/stock')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(stock_api)

class StockAPI:
    class _Test(Resource):
        def post(self):
            body = request.get_json()
            uid = body.get('uid')
            u = User.add_stockuser(self,uid)
            print(str(u))
    api.add_resource(_Test, '/id')
