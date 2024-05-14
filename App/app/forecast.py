import pickle
import networkx as nx
from flask import jsonify, request, send_from_directory, current_app
from flask_restful import Resource
from db import execute_query
import os
import time


class Forecast1(Resource):  # 路段估值
    data_json = {
        'code': 200,
        'msg': '',
        'data': ''
    }

    def post(self):
        request_json = request.json
        startLink = request_json.get('startLink', None)
        endLink = request_json.get('endLink', None)
        if startLink is not None and endLink is not None:
            self.data_json['code'] = 200
            self.data_json['msg'] = "路段估值成功"
            # 定义图数据文件路径
            file_path = os.path.join("App/static", "data", "graph_data.pickle")
            # 加载图数据
            with open(file_path, 'rb') as f:
                G = pickle.load(f)
            shortest_path = nx.shortest_path(G, source=startLink, target=endLink, weight='weight')
            shortest_distance = nx.shortest_path_length(G, source=startLink, target=endLink, weight='weight')
            distance = shortest_distance
            if distance == float('inf'):
                distance = 'Infinity'
            response_data = {
                'startLink': startLink,
                'endLink': endLink,
                'linkTime': distance,
                'path': shortest_path,
            }
            self.data_json['data'] = response_data
        else:
            self.data_json['code'] = 404
            self.data_json['msg'] = '未提交数据'
            self.data_json['data'] = ''
        return jsonify(self.data_json)


class Forecast2(Resource):  # 总体估值
    data_json = {
        'code': 200,
        'msg': '',
        'data': ''
    }

    def post(self):
        request_json = request.json
        startLink = request_json.get('startLink', None)
        endLink = request_json.get('endLink', None)
        sliceNum = int(request_json.get('slice'))
        timeStr = request_json.get('time')
        if startLink is not None and endLink is not None and sliceNum is not None and timeStr is not None:
            timeObj = time.strptime(timeStr, "%H:%M")
            minutes = (timeObj.tm_hour - 8) * 60 + timeObj.tm_min
            min_slice = minutes / 5
            max_slice = min_slice + sliceNum / 5
            self.data_json['code'] = 200
            sql = "SELECT startlink AS startLink,endlink AS endLink,AVG(ata) AS average_ata FROM `order` WHERE startlink = %s AND endlink = %s AND sliceid BETWEEN %s AND %s;"
            res = execute_query(sql, [startLink, endLink, min_slice, max_slice], True)
            self.data_json['msg'] = '总体估值'
            self.data_json['data'] = res
        else:
            self.data_json['code'] = 404
            self.data_json['msg'] = '未提交数据'
            self.data_json['data'] = ''
        return jsonify(self.data_json)
