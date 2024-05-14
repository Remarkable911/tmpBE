from flask import Flask
from .exts import init_exts
from .urls import *
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)  # 添加 CORS 头部，允许所有域名的跨域请求
    app.config.from_object('App.config.settings')
    init_exts(app=app)
    return app
