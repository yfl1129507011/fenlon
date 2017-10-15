from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .common.config import config

app = Flask(__name__)

# 加载配置
app.config.from_object(config['development'])

# 引入mysql实例
db = SQLAlchemy(app)

# 使用Flask-Login认证用户
lm = LoginManager(app)
lm.session_protection = 'strong'
lm.login_view = 'login'

# 自定义404错误页面
@app.errorhandler(404)
def pageNotFound(e):
    return '404错误'

# 自定义500错误页面
@app.errorhandler(500)
def internalServerError(e):
    return '500错误'

# 引入路由控制模块
from .controller import *