from flask import jsonify, request
from flask_restful import Resource
from db import execute_query


class Statistics(Resource):
    data_json = {
        'code': 200,
        'msg': '',
        'data': {
            'crossTimeTable': {
                'asc': {},
                'desc': {}
            },
            'linkTimeTable': {
                'asc': {},
                'desc': {}
            },
            'disOrderTable': {
                'asc': {},
                'desc': {}
            },
            'linkFlowTable': {
                'asc': {},
                'desc': {}
            },
            'driverRunTable': {
                'asc': {},
                'desc': {}
            }
        }
    }

    def get(self):
        # crossTime
        # sql = "SELECT * FROM `intersection` ORDER BY crosstime  LIMIT 10"
        # res = execute_query(sql)
        # self.data_json['data']['crossTimeTable']['asc'] = res
        sql = "SELECT * FROM `intersection` where crosstime <1000000 ORDER BY crosstime DESC LIMIT 10"
        res = execute_query(sql)
        self.data_json['data']['crossTimeTable']['desc'] = res
        # linkTime
        # sql = "SELECT * FROM `linkavg` WHERE linkavgtime != 0 ORDER BY linkavgtime  LIMIT 10"
        # res = execute_query(sql)
        # self.data_json['data']['linkTimeTable']['asc'] = res
        sql = "SELECT * FROM `linkavg` where linkavgtime<1000000 ORDER BY linkavgtime DESC LIMIT 10"
        res = execute_query(sql)
        self.data_json['data']['linkTimeTable']['desc'] = res
        # disOrder
        # sql = "SELECT * FROM `order` ORDER BY distance  LIMIT 10"
        # res = execute_query(sql)
        # self.data_json['data']['disOrderTable']['asc'] = res
        sql = "SELECT * FROM `order` where distance<1000000 ORDER BY distance DESC LIMIT 10"
        res = execute_query(sql)
        self.data_json['data']['disOrderTable']['desc'] = res
        # linkFlow
        # sql = "SELECT linkid, COUNT(linkid) AS link_count FROM `trajectorylink` GROUP BY linkid ORDER BY link_count LIMIT 10"
        # res = execute_query(sql)
        # self.data_json['data']['linkFlowTable']['asc'] = res
        sql = "SELECT linkid, COUNT(linkid) AS link_count FROM `link` GROUP BY linkid ORDER BY link_count DESC LIMIT 10"
        res = execute_query(sql)
        self.data_json['data']['linkFlowTable']['desc'] = res
        # driveRun
        # sql = "SELECT driverid, COUNT(driverid) AS drive_count FROM `order` GROUP BY driverid ORDER BY drive_count LIMIT 10"
        # res = execute_query(sql)
        # self.data_json['data']['driverRunTable']['asc'] = res
        sql = "SELECT driverid, COUNT(driverid) AS drive_count FROM `order` GROUP BY driverid ORDER BY drive_count DESC LIMIT 10"
        res = execute_query(sql)
        self.data_json['data']['driverRunTable']['desc'] = res
        return jsonify(self.data_json)
