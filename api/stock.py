import json, jwt
from flask import Blueprint, request, jsonify, current_app, Response, g
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
from auth_middleware import token_required

from model.users import User, StockUser,Transactions,Stocks, User_Transaction_Stocks

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
            
            quantity = body.get("quantity")
            symbol = body.get("symbol")
            uid = body.get("uid")
            current_stock_price = Stocks.get_price(self,body)
            value = quantity * current_stock_price
            bal = StockUser.get_balance(self,body)
            userid = StockUser.get_userid(self,uid)
            stockid = Stocks.get_stockid(self,symbol)
            u=Transactions.createlog_buy(self,body)
            z= User_Transaction_Stocks.multilog_buy(self,body = body,value = value,transactionid=u)
            print(str(z))
            print("this is transactionid" + str(u))
            print("this is user id" + str(userid))
            print("this is stockid" + str(stockid))
            
            

    class _transaction_sell(Resource):
        def post(self):
            body = request.get_json()
    api.add_resource(_initilize_user, '/initilize')
    api.add_resource(_transaction_buy, '/buy')
    api.add_resource(_transaction_sell, '/sell')

