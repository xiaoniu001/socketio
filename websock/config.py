class Config(object):
    """
    配置文件参数
    """
    DEBUG = True
    ENV = "development"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:wlm19941118@localhost:3306/socketio?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    REDIS_URL = "redis://127.0.0.1:6379/0"

