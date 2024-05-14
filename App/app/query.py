from flask import jsonify, request
from flask_restful import Resource
from db import execute_query


class OrderQuery(Resource):
    data_json = {
        'code': 200,
        'msg': '',
        'data': '',
    }

    def get(self):
        sql = "SELECT * FROM `order` LIMIT 10"
        res = execute_query(sql)
        self.data_json['data'] = res
        return jsonify(self.data_json)

    def post(self):
        response_date = request.json.get('formattedDate')
        print(response_date)
        sql = "SELECT * FROM `order` WHERE date = %s LIMIT 10"
        res = execute_query(sql, [response_date])
        self.data_json['data'] = res
        return jsonify(self.data_json)


class WeatherQuery(Resource):
    data_json = {
        'code': 200,
        'msg': '',
        'data': '',
    }

    def get(self):
        sql = "SELECT * FROM `weather` LIMIT 10"
        res = execute_query(sql)
        self.data_json['data'] = res
        return jsonify(self.data_json)

    def post(self):
        response_date = request.json.get('formattedDate')
        sql = "SELECT * FROM `weather` WHERE date = %s LIMIT 10"
        res = execute_query(sql, [response_date])
        self.data_json['data'] = res
        return jsonify(self.data_json)


class LinkQuery(Resource):
    data_json = {
        'code': 200,
        'msg': '',
        'data': '',
    }

    def get(self):
        sql = "SELECT * FROM `link` LIMIT 10"
        res = execute_query(sql)
        self.data_json['data'] = res
        return jsonify(self.data_json)

    def post(self):
        response_date = request.json.get('formattedDate')
        print(response_date)
        sql = "SELECT * FROM `link` WHERE orderid = %s LIMIT 10"
        res = execute_query(sql, [response_date])
        self.data_json['data'] = res
        return jsonify(self.data_json)


class CrossQuery(Resource):
    data_json = {
        'code': 200,
        'msg': '',
        'data': '',
    }

    def get(self):
        sql = "SELECT * FROM `intersection` LIMIT 10"
        res = execute_query(sql)
        self.data_json['data'] = res
        return jsonify(self.data_json)

    def post(self):
        response_date = request.json.get('formattedDate')
        print(response_date)
        sql = "SELECT * FROM `intersection` WHERE orderid = %s LIMIT 10"
        res = execute_query(sql, [response_date])
        self.data_json['data'] = res
        return jsonify(self.data_json)
