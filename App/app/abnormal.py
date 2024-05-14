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

    def put(self):
        request_json = request.json
        if request_json:
            orderid = request_json.get('orderid', None)
            ata = request_json.get('ata', None)
            distance = request_json.get('distance', None)
            simpleeta = request_json.get('simpleeta', None)
            driverid = request_json.get('driverid', None)
            sliceid = request_json.get('sliceid', None)
            date = request_json.get('date', None)
            startlink = request_json.get('startlink', None)
            endlink = request_json.get('endlink', None)
            sql = "UPDATE `order` SET ata =%s, distance =%s,simpleeta =%s,driverid=%s,sliceid=%s, startlink =%s, endlink =%s,date= %s where orderid =%s"
            execute_query(sql, [ata, distance, simpleeta, driverid, sliceid, startlink, endlink, date, orderid])
            self.data_json['code'] = 200
            self.data_json['msg'] = "编辑成功"
        else:
            self.data_json['code'] = 404
            self.data_json['msg'] = '未提交数据'
        return jsonify(self.data_json)

    def delete(self):
        request_json = request.json
        print(request_json)
        orderid = request_json.get('orderid')

        sql = "DELETE FROM `order` where orderid = %s"
        execute_query(sql, [orderid])
        self.data_json['code'] = 200
        self.data_json['msg'] = "删除成功"
        return jsonify(self.data_json)


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

    def put(self):
        request_json = request.json
        if request_json:
            orderid = request_json.get('orderid', None)
            sequence = request_json.get('sequence', None)
            linkid = request_json.get('linkid', None)
            linktime = request_json.get('linktime', None)
            linkratio = request_json.get('linkratio', None)
            linkcurrentstatus = request_json.get('linkcurrentstatus', None)
            linkarrivalstatus = request_json.get('linkarrivalstatus', None)
            sql = "UPDATE `link` SET linktime =%s,linkratio= %s,linkcurrentstatus = %s,linkcurrentstatus = %s WHERE orderid = %s AND sequence = %s AND linkid =%s"
            execute_query(sql, [linktime, linkratio, linkcurrentstatus, linkarrivalstatus, orderid, sequence, linkid])
            self.data_json['code'] = 200
            self.data_json['msg'] = "编辑成功"
        else:
            self.data_json['code'] = 404
            self.data_json['msg'] = '未提交数据'
        return jsonify(self.data_json)

    def delete(self):
        request_json = request.json
        orderid = request_json.get('orderid', None)
        sequence = request_json.get('sequence', None)
        linkid = request_json.get('linkid', None)
        sql = "DELETE FROM `link` WHERE orderid = %s AND sequence = %s AND linkid =%s"
        execute_query(sql, [orderid, sequence, linkid])
        self.data_json['code'] = 200
        self.data_json['msg'] = "删除成功"
        return jsonify(self.data_json)


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

    def put(self):
        request_json = request.json
        if request_json:
            crossid = request_json.get('crossid', None)
            entranceid = request_json.get('entranceid', None)
            exitid = request_json.get('exitid', None)
            crosstime = request_json.get('crosstime', None)
            orderid = request_json.get('orderid', None)
            sql = "UPDATE `intersection` SET crosstime = %s, entranceid = %s, exitid = %s WHERE orderid = %s AND crossid = %s"
            execute_query(sql, [crosstime, entranceid, exitid, orderid, crossid])
            self.data_json['code'] = 200
            self.data_json['msg'] = "编辑成功"
        else:
            self.data_json['code'] = 404
            self.data_json['msg'] = '未提交数据'
        return jsonify(self.data_json)

    def delete(self):
        request_json = request.json
        crossid = request_json.get('crossid', None)
        orderid = request_json.get('orderid', None)
        sql = "DELETE FROM `intersection` WHERE orderid =%s AND crossid =%s"
        execute_query(sql, [orderid, crossid])
        self.data_json['code'] = 200
        self.data_json['msg'] = "删除成功"
        return jsonify(self.data_json)
