from flask import jsonify, request
from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage
from App import utils
from db import execute_query


class OrderImport(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('orderFile', required=True, type=FileStorage, location="files", help="请提供一个文件")

    data_json = {
        'code': 200,
        'msg': '',
        'data': '',
    }

    def post(self):
        orderFile = self.parser.parse_args().get("orderFile")
        filePath = utils.get_upload_path(orderFile.filename)
        orderFile.save(filePath)
        return {"msg": "保存成功"}


class LinkImport(Resource):
    data_json = {
        'code': 200,
        'msg': '',
        'data': '',
    }


class CrossImport(Resource):
    data_json = {
        'code': 200,
        'msg': '',
        'data': '',
    }


class WeatherImport(Resource):
    data_json = {
        'code': 200,
        'msg': '',
        'data': '',
    }
