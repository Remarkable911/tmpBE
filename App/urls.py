from .exts import api
from App.app.login import Login
from App.app.user import User
from App.app.statistics import Statistics
from App.app.home import Home
from App.app.net import Net
from App.app.forecast import Forecast1, Forecast2
from App.app.query import OrderQuery, WeatherQuery, LinkQuery, CrossQuery
from App.app.Import import OrderImport, WeatherImport, LinkImport, CrossImport
from App.app.abnormal import AbnormalOrder, AbnormalLink, AbnormalCross
from App.app.merge import Merge, Merge2
from App.app.record import Record

api.add_resource(Login, '/login')
api.add_resource(User, '/user')
api.add_resource(Statistics, '/statistics')
api.add_resource(Home, '/home')
api.add_resource(Net, '/net')
api.add_resource(Forecast1, '/forecast/1')
api.add_resource(Forecast2, '/forecast/2')
api.add_resource(OrderImport, '/import/order')
api.add_resource(WeatherImport, '/import/weather')
api.add_resource(LinkImport, '/import/link')
api.add_resource(CrossImport, '/import/cross')
api.add_resource(AbnormalOrder, '/abnormal/order')
api.add_resource(AbnormalLink, '/abnormal/link')
api.add_resource(AbnormalCross, '/abnormal/cross')
api.add_resource(OrderQuery, '/order/query')
api.add_resource(WeatherQuery, '/weather/query')
api.add_resource(LinkQuery, '/link/query')
api.add_resource(CrossQuery, '/cross/query')
api.add_resource(Merge, '/merge')
api.add_resource(Merge2, '/merge2')
api.add_resource(Record, '/record')
