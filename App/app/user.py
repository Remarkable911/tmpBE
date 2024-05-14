from flask import jsonify, request
from flask_restful import Resource
from db import execute_query


class User(Resource):
    data_json = {
        'code': 200,
        'msg': '',
        'data': {
            'userTable': {}
        },
    }

    def get(self):
        sql = "SELECT * FROM member"
        res = execute_query(sql)
        self.data_json['data']['userTable'] = res
        return jsonify(self.data_json)

    def post(self):
        request_json = request.json

        if request_json:
            username = request_json.get('username', None)
            id = request_json.get('id', None)
            if request_json.get('gender') == '男':
                gender = 1
            elif request_json.get('gender') == '女':
                gender = 2
            phone = request_json.get('phone', None)
            email = request_json.get('email', None)
            rule = int(request_json.get('rule', None))
            if request_json.get('status') == '正常':
                status = 1
            else:
                status = 2
            try:
                sql = "INSERT INTO member (username, id, gender, phone, email, rule, status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                execute_query(sql, [username, id, gender, phone, email, rule, status])
                self.data_json['code'] = 200
                self.data_json['msg'] = "添加成功"
            except Exception as e:
                print("添加失败")
                self.data_json['code'] = 404
                self.data_json['msg'] = "用户重复或输入不合法"
        else:
            self.data_json['code'] = 404
            self.data_json['msg'] = '未提交数据'
        return jsonify(self.data_json)

    def put(self):
        request_json = request.json
        if request_json:
            username = request_json.get('username', None)
            id = request_json.get('id', None)
            if request_json.get('gender') == '男':
                gender = 1
            elif request_json.get('gender') == '女':
                gender = 2
            phone = request_json.get('phone', None)
            email = request_json.get('email', None)
            if request_json.get('rule') == '用户':
                rule = 1
            elif request_json.get('rule') == '权限管理员':
                rule = 2
            elif request_json.get('rule') == '系统管理员':
                rule = 3
            if request_json.get('status') == '正常':
                status = 1
            else:
                status = 2
            print(username, gender, phone, email, rule, status, id)
            sql = "UPDATE `member` SET username = %s,gender =%s,phone = %s,email = %s,rule =%s,status =%s WHERE id =%s"
            execute_query(sql, [username, gender, phone, email, rule, status, id])
            self.data_json['code'] = 200
            self.data_json['msg'] = "编辑成功"
        else:
            self.data_json['code'] = 404
            self.data_json['msg'] = '未提交数据'
        return jsonify(self.data_json)

    def delete(self):
        id = request.json
        id = id.get('id', None)
        print(id)
        if id:
            sql = "DELETE FROM `member` WHERE id = %s"
            execute_query(sql, [id])
            self.data_json['code'] = 200
            self.data_json['msg'] = "删除成功"
        else:
            self.data_json['code'] = 404
            self.data_json['msg'] = "删除失败"
        return jsonify(self.data_json)
