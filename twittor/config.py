#这里定义class级别的变量 第一个变量就是用来存储本地sql表单的位置的
#SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///" + os.path.join(config_path, '
#"DATABASE_URL" 是一个空的环境变量 如果存在的化使用它 否则使用后者

import os

config_path = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///" + os.path.join(config_path, 'twittor.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'abc123')
    TWEET_PER_PAGE = os.environ.get('TWEET_PER_PAGE', 20)

    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', 'noreply@twittor.com')
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = os.environ.get('MAIL_PORT', 587)
    
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', True)
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'twittorservice123@gmail.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'twittoradmin123')
    MAIL_SUBJECT_RESET_PASSWORD = '[Twittor] Please Reset Your Password'
    MAIN_SUBJECT_USER_ACTIVATE = '[Twittor] Please Activate Your Accout'