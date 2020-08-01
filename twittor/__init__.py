#init是真正的启动文件，相当于一个router，提供不同URL的启动方法
#add_url_rule第一个参数是定义URL 第二个参数是对应的route里的函数，每个函数渲染一个页面
#初始页面只有GET方法 而登陆页面要写入信息 所以需要POST方法  在methods里重新定义

#初始化工作：初始化一个sql数据库 一个migrate 传入flaskapp
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from flask_login import LoginManager
from flask_mail import Mail

from twittor.config import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'login'
mail = Mail()

from twittor.route import index, login, logout, register, user, page_not_found, \
    edit_profile, reset_password_request, password_reset, explore, user_activate


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)
    app.add_url_rule('/index', 'index', methods=['GET', 'POST'])
    app.add_url_rule('/', 'index', index, methods=['GET', 'POST'])
    app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
    app.add_url_rule('/logout', 'logout', logout)
    app.add_url_rule('/register', 'register', register, methods=['GET', 'POST'])
    app.add_url_rule('/<username>', 'profile', user, methods=['GET', 'POST'])
    app.add_url_rule('/edit_profile', 'edit_profile', edit_profile, methods=['GET', 'POST'])
    app.add_url_rule(
        '/reset_password_request',
        'reset_password_request',
        reset_password_request,
        methods=['GET', 'POST']
    )
    app.add_url_rule(
        '/password_reset/<token>',
        'password_reset',
        password_reset,
        methods=['GET', 'POST']
    )
    app.register_error_handler(404, page_not_found)
    app.add_url_rule('/explore', 'explore', explore)
    app.add_url_rule('/activate/<token>', 'user_activate', user_activate)
    return app