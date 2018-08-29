# coding=utf-8

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from websock.DB import socketio, DB
from websock import create_app


if __name__ == '__main__':
    app = create_app()
    # app.app_context().push()
    migrate = Migrate(app, DB)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    manager.add_command('runserver', socketio.run(app=app, host='0.0.0.0', port=5010))
    manager.run()
