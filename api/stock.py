import json, jwt
from flask import Blueprint, request, jsonify, current_app, Response, g
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
from auth_middleware import token_required

from model.users import User, StockUser,Transactions,Stocks

stock_api = Blueprint('stock_api', __name__,
                   url_prefix='/stock')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(stock_api)

class StockAPI:
    class _initilize_user(Resource):
        def post(self):
            body = request.get_json()
            uid = body.get('uid')
            u = User.add_stockuser(self,uid)
            print(str(u))
    class _transaction_buy(Resource):
        def post(self):
            body = request.get_json()
            try:
                quantity = body.get("quantity")
                current_stock_price = Stocks.get_price(self,body)
                print(str(current_stock_price))
                value = quantity * current_stock_price
                print(str(value))
                u=Transactions.createlog_buy(self,body)
                print(str(u))
            except Exception as e:
                return {"error": "no quantity in payload"},500
            

    class _transaction_sell(Resource):
        def post(self):
            body = request.get_json()
    api.add_resource(_initilize_user, '/initilize')
    api.add_resource(_transaction_buy, '/buy')
    api.add_resource(_transaction_sell, '/sell')

