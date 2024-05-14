from flask import jsonify, request
from flask_restful import Resource
from db import execute_query


class Login(Resource):
    menuUser = [
        {
            'path': "/home",
            'name': "home",
            'label': "首页",
            'icon': "s-home",
            'url': "Home.vue",
        },
        {
            'path': "/predict",
            'name': "predict",
            'label': "时间预测",
            'icon': "guide",
            'url': "Predict.vue",
        },
        {
            'path': "/record",
            'name': "record",
            'label': "行程记录",
            'icon': "time",
            'url': "Record.vue",
        },
        {
            'path': "/situation",
            'name': "situation",
            'label': "路段状况",
            'icon': "data-analysis",
            'url': "Situation.vue",
        }
    ]
    menuData = [{
        'path': "/clear",
        'label': "数据清洗",
        'icon': "folder",
        'children': [
            {
                'path': "/abnormal",
                'name': "abnormal",
                'label': "异常数据清理",
                'icon': "sunny",
                'url': "DataClear/Abnormal.vue",
            },
            {
                'path': "/merge",
                'name': "merge",
                'label': "道路合并",
                'icon': "truck",
                'url': "DataClear/Merge.vue",
            }]
    },
        {
            'path': "/statistics",
            'name': "statistics",
            'label': "数据统计",
            'icon': "coordinate",
            'url': "Statistics.vue",
        }, ]
    menuAdmin = [{
        'path': "/user",
        'name': "user",
        'label': "用户管理",
        'icon': "user-solid",
        'url': "User.vue",
    },
        {
            'path': "/import",
            'label': "数据导入",
            'icon': "s-data",
            'children': [
                {
                    'path': "/order",
                    'name': "order-in",
                    'label': "订单导入",
                    'icon': "truck",
                    'url': "DataImport/OrderIn.vue",
                },
                {
                    'path': "/weather",
                    'name': "weather-in",
                    'label': "天气导入",
                    'icon': "sunny",
                    'url': "DataImport/WeatherIn.vue",
                },
                {
                    'path': "/link",
                    'name': "link-in",
                    'label': "路段导入",
                    'icon': "link",
                    'url': "DataImport/LinkIn.vue",
                },
                {
                    'path': "/cross",
                    'name': "cross-in",
                    'label': "路口导入",
                    'icon': "news",
                    'url': "DataImport/CrossIn.vue",
                },
            ],
        }, ]
    data_json = {
        'code': 200,
        'msg': '',
        'data': {
            'username': '',
            'password': '',
            'rule': '',
            'token': '',
            'menu': ''
        }
    }

    def get(self):
        return 'ok'

    def post(self):
        request_json = request.json
        # print(request_json)
        if request_json:
            username = request_json.get('username', None)
            password = request_json.get('password', None)
            # print('username: %s, password: %s' % (username, password))
            sql = "SELECT * FROM `member` WHERE username=%s AND password=%s"
            res = execute_query(sql, [username, password], True)
            if res:
                self.data_json['code'] = 200
                self.data_json['data']['username'] = res['username']
                self.data_json['data']['password'] = res['password']
                self.data_json['data']['rule'] = res['rule']
                self.data_json['data']['status'] = res['status']
                self.data_json['data']['token'] = res['id'] + res['password']
                if res['rule'] == 3:
                    self.data_json['data']['menu'] = self.menuAdmin
                elif res['rule'] == 2:
                    self.data_json['data']['menu'] = self.menuData
                else:
                    self.data_json['data']['menu'] = self.menuUser
            else:
                self.data_json['code'] = 404
                self.data_json['data']['username'] = ''
                self.data_json['data']['password'] = ''
                self.data_json['data']['rule'] = ''
                self.data_json['data']['token'] = ''
                self.data_json['data']['menu'] = ''
                self.data_json['data']['status'] = ''
                self.data_json['msg'] = '用户名或密码错误'
        else:
            self.data_json['code'] = 404
            self.data_json['data']['username'] = ''
            self.data_json['data']['password'] = ''
            self.data_json['data']['rule'] = ''
            self.data_json['data']['token'] = ''
            self.data_json['data']['menu'] = ''
            self.data_json['data']['status'] = ''
            self.data_json['msg'] = '未提交数据'
        return jsonify(self.data_json)
