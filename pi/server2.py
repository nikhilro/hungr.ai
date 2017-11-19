from flask import Flask, render_template
from flask_socketio import SocketIO
from camera import Camera

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)


@socketio.on('connected')
def handle_json(json):
    print('received message: ' + str(json))
    Camera().get_frame(socketio)


if __name__ == '__main__':
    socketio.run(app)
