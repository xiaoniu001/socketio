from flask import Flask


from websock.config import Config
from websock.DB import DB, socketio
from websock.project.views import project


def create_app():
    """
    创建flask实例app
    :return: app
    """
    app = Flask(__name__)

    app.register_blueprint(project)

    app.config.from_object(Config)
    DB.init_app(app)
    socketio.init_app(app, async_mode='eventlet', logger=True, engineio_logger=True)
    return app


