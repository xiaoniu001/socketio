from websock import socketio

from flask_socketio import join_room, emit, rooms
from flask import current_app, Blueprint, render_template
from websock.DB import Project


project = Blueprint("project", __name__,  url_prefix='/project')

thread = []


@project.route('/')
def index():
    return render_template('websocket.html', async_mode=socketio.async_mode)


@socketio.on("cold", namespace='/test')
def show_project(message):

    print("receive message", message)
    global thread
    join_room(message['project'])
    if message['project'] in thread:
        emit('my_response', {'data': 'Connected'}, room=message["project"])
    else:
        socketio.start_background_task(project_query, (message, current_app._get_current_object()))
        thread.append(message['project'])



def project_query(message):
    print(message)
    while True:

        socketio.sleep(5)
        with message[1].app_context():
            projects = Project.query.filter_by(id=int(message[0]["project"])).first()
        print("projects", projects)
        socketio.emit('my_response', {"data": "come here", "id": projects.id}, room=message[0]["project"],
                      namespace='/test')


@socketio.on('connect', namespace='/test')
def connect():
    print("client connect")




