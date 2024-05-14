from flask import current_app, jsonify, request, send_from_directory
from flask_restful import Resource
from db import execute_query
import os, json


class Net(Resource):
    data_json = {
        'code': '',
        'msg': '',
        'data': ''
    }

    def get(self):
        # 获取静态文件所在的目录路径
        static_dir = os.path.join(current_app.root_path, 'static')
        data_dir = os.path.join(static_dir, 'data')
        # 返回静态文件
        return send_from_directory(data_dir, 'data.json')

    def post(self):
        sql = "SELECT * FROM nextlinks ORDER BY RAND() LIMIT 1000"
        links_data = execute_query(sql)
        # 构造节点和边的数据
        nodes_set = set()
        edges = []
        # 获取所有nextlink列的字段名
        nextlink_columns = ['nextlink1', 'nextlink2', 'nextlink3', 'nextlink4', 'nextlink5', 'nextlink6', 'nextlink7']
        for row in links_data:
            linkid = row['linkid']
            # 获取该行所有nextlink的值
            nextlinks = [row[col] for col in nextlink_columns if row[col] is not None]
            # 将 linkid 和 nextlink 添加到集合中
            nodes_set.add(str(linkid))
            nodes_set.update(map(str, nextlinks))
            # 将 linkid 和 nextlink 组合成边
            edges.extend({'source': str(linkid), 'target': str(nextlink)} for nextlink in nextlinks)
        # 将集合中的元素转换为节点列表
        nodes = [{'name': node} for node in nodes_set]
        # 静态目录的路径
        static_dir = os.path.join('App/static', 'data')
        # 文件路径
        filename = os.path.join(static_dir, 'data.json')
        # 返回构造好的数据
        data = {'nodes': nodes, 'edges': edges}
        # 保存数据到文件
        with open(filename, 'w') as f:
            json.dump(data, f)
        return {'success': True}
