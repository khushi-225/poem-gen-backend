from app import app, socketio

if __name__ == '__main__':
    socketio.run(app, port=9000, debug=True)