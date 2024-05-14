from flask import jsonify, request
from flask_restful import Resource
from db import execute_query
from datetime import datetime


class Merge(Resource):
    data_json = {
        'code': 200,
        'msg': '',
        'data': {
            'order': [],
            'link': []
        }
    }

    def get(self):
        sql = "SELECT * FROM `order` LIMIT 10"
        res = execute_query(sql)
        self.data_json['data']['order'] = res
        return jsonify(self.data_json)

    def post(self):
        orderid = request.json.get('orderid')
        sql = "SELECT * FROM `link` WHERE orderid = %s"
        res = execute_query(sql, orderid)
        self.data_json['data']['link'] = res
        return jsonify(self.data_json)


class Merge2(Resource):
    data_json = {
        'code': 200,
        'msg': '',
        'data': {
            'order': [],
            'link': []
        }
    }

    def post(self):
        date = request.json.get('formattedDate')
        driverid = request.json.get('driveid')
        print(date, type(date), driverid, type(driverid))
        if date is not None and (driverid is not None and driverid != ""):
            sql = "SELECT * FROM `order` where date = %s and driverid = %s LIMIT 10"
            res = execute_query(sql, [date, driverid])
            self.data_json['data']['order'] = res
            return jsonify(self.data_json)
        elif date is None and (driverid is not None and driverid != ""):
            sql = "SELECT * FROM `order` where driverid = %s LIMIT 10"
            res = execute_query(sql, driverid)
            self.data_json['data']['order'] = res
            return jsonify(self.data_json)
        elif date is not None and driverid is None:
            sql = "SELECT * FROM `order` where date = %s LIMIT 10"
            res = execute_query(sql, date)
            self.data_json['data']['order'] = res
            return jsonify(self.data_json)
        else:
            sql = "SELECT * FROM `order` LIMIT 10"
            res = execute_query(sql)
            self.data_json['data']['order'] = res
            return jsonify(self.data_json)
