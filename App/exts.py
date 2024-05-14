from flask_restful import Api

api = Api()


def init_exts(app):
    api.init_app(app=app)
