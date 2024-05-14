from flask import jsonify, request
from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage
from App import utils
from App.app.import_csv import import_order, import_link, import_cross, import_weather


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
        import_order(filePath)
        return {"msg": "保存成功"}


class LinkImport(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('linkFile', required=True, type=FileStorage, location="files", help="请提供一个文件")

    data_json = {
        'code': 200,
        'msg': '',
        'data': '',
    }

    def post(self):
        linkFile = self.parser.parse_args().get("linkFile")
        filePath = utils.get_upload_path(linkFile.filename)
        linkFile.save(filePath)
        import_link(filePath)
        return {"msg": "保存成功"}


class CrossImport(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('crossFile', required=True, type=FileStorage, location="files", help="请提供一个文件")

    data_json = {
        'code': 200,
        'msg': '',
        'data': '',
    }

    def post(self):
        crossFile = self.parser.parse_args().get("crossFile")
        filePath = utils.get_upload_path(crossFile.filename)
        crossFile.save(filePath)
        import_cross(filePath)
        return {"msg": "保存成功"}


class WeatherImport(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('weatherFile', required=True, type=FileStorage, location="files",
                                 help="请提供一个文件")

    data_json = {
        'code': 200,
        'msg': '',
        'data': '',
    }

    def post(self):
        weatherFile = self.parser.parse_args().get("weatherFile")
        filePath = utils.get_upload_path(weatherFile.filename)
        weatherFile.save(filePath)
        import_weather(filePath)
        return {"msg": "保存成功"}
