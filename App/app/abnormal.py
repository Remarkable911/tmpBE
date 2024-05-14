from flask import jsonify, request
from flask_restful import Resource
from db import execute_query


class AbnormalOrder(Resource):
    data_json = {
        'code': 200,
        'msg': '',
        'data': {
            'ata': {
                'info': '真实行程总时间',
                'table': []
            },
            'distance': {
                'info': '路线距离',
                'table': []
            },
            'simpleeta': {
                'info': '平均通行时间',
                'table': []
            },
            'date': {
                'info': '日期',
                'table': []
            }
        }
    }

    def get(self):
        sql = "SELECT * FROM `order` WHERE ata is null OR ata <= 0 OR ata >= 1000000"
        res = execute_query(sql)
        self.data_json['data']['ata']['table'] = res
        sql = "SELECT * FROM `order` WHERE distance is null OR distance <= 0 OR distance >= 1000000"
        res = execute_query(sql)
        self.data_json['data']['distance']['table'] = res
        sql = "SELECT * FROM `order` WHERE simpleeta is null OR simpleeta <= 0 OR simpleeta >= 1000000"
        res = execute_query(sql)
        self.data_json['data']['simpleeta']['table'] = res
        sql = "SELECT * FROM `order` WHERE date is null "
        res = execute_query(sql)
        self.data_json['data']['date']['table'] = res
        return jsonify(self.data_json)

    def post(self):
        orderid = request.json.get('orderid')
        sql = "DELETE FROM `order` WHERE orderid = %s"
        res = execute_query(sql, orderid)
        if res:
            msg = '删除成功'
        else:
            msg = '删除失败'
        return jsonify(msg)


class AbnormalLink(Resource):
    data_json = {
        'code': 200,
        'msg': '',
        'data': {
            'linktime': {
                'info': '路段通行时间',
                'table': {}
            },
            'ratio': {
                'info': '道路覆盖率',
                'table': {}
            },
            'status': {
                'info': '道路状况',
                'table': {}
            }
        }
    }

    def get(self):
        sql = "SELECT * FROM `link` WHERE linktime < 0 or linktime is null or linktime >=100000 LIMIT 20"
        res = execute_query(sql)
        self.data_json['data']['linktime']['table'] = res
        sql = "SELECT * FROM `link` WHERE linkratio <1 LIMIT  20"
        res = execute_query(sql)
        self.data_json['data']['ratio']['table'] = res
        sql = "SELECT * FROM `link` WHERE linkarrivalstatus > 3 OR linkcurrentstatus >3 LIMIT 20"
        res = execute_query(sql)
        self.data_json['data']['status']['table'] = res
        return jsonify(self.data_json)

    def post(self):
        linkid = request.json.get('linkid')
        sql = "DELETE FROM `link` WHERE linkid = %s"
        res = execute_query(sql, linkid)
        if res:
            msg = '删除成功'
        else:
            msg = '删除失败'
        return jsonify(msg)


class AbnormalCross(Resource):
    data_json = {
        'code': 200,
        'msg': '',
        'data': {
            'info': '路口通行时间',
            'table': {}
        }
    }

    def get(self):
        sql = "SELECT * FROM `intersection` WHERE crosstime is NULL OR crosstime <= 0 OR crosstime >= 1000000"
        res = execute_query(sql)
        self.data_json['data']['table'] = res
        return jsonify(self.data_json)

    def post(self):
        crossid = request.json.get('crossid')
        sql = "DELETE FROM `intersection` WHERE crossid = %s"
        res = execute_query(sql, crossid)
        if res:
            msg = "删除成功"
        else:
            msg = "删除失败"
        return jsonify(msg)
