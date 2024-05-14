from flask import jsonify, request
from flask_restful import Resource
from db import execute_query


class Record(Resource):
    data_json = {
        'code': 200,
        'msg': '',
        'data': {
            'queryHistory': []
        }
    }

    def get(self):
        driverId = request.args.get('driverId')
        sql = "SELECT * FROM `record` where driverid = %s"
        res = execute_query(sql, driverId)
        self.data_json['data']['queryHistory'] = res
        return jsonify(self.data_json)
