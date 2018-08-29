from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

import eventlet
eventlet.monkey_patch(socket=True)

socketio = SocketIO()

DB = SQLAlchemy()


class Project(DB.Model):
    """
    项目
    """
    __tablename__ = "project"

    id = DB.Column(DB.Integer, primary_key=True)
    project_title = DB.Column(DB.String(100), nullable=False)

