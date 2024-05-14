from flask import jsonify, request
from flask_restful import Resource
from db import execute_query


class Home(Resource):
    data_json = {
        'code': 200,
        'msg': '',
        'data': {
            'orderNum': 0,
            'todayNum': 0,
            'linkFlow': '',
            'link': {},
            'linkList': {}
        },
    }

    def get(self):
        sql = "SELECT COUNT(orderid) AS orderNum FROM `order`"
        res = execute_query(sql, [], True)
        self.data_json['data']['orderNum'] = res['orderNum']

        sql = "SELECT COUNT(*) AS todayNum FROM `order` WHERE create_at >= DATE_SUB(CURDATE(), INTERVAL 1 DAY)"
        res = execute_query(sql, [], True)
        self.data_json['data']['todayNum'] = res['todayNum']
        sql = "SELECT linkid, COUNT(linkid) AS link_count FROM `link` GROUP BY linkid ORDER BY link_count desc LIMIT 5"
        res = execute_query(sql)
        self.data_json['data']['linkFlow'] = res
        return jsonify(self.data_json)

    def post(self):
        linkId = request.json.get('linkid', 2)
        sql = "select * from linkavg where linkid = %s"
        res = execute_query(sql, [linkId], True)
        self.data_json['data']['link'] = res
        print(self.data_json)
        return jsonify(self.data_json)
