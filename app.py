from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def results():
    return render_template('results.html')

@socketio.on('connect')
def handle_connect():
    print("Client connected to Socket.IO")

@socketio.on('button_click')
def handle_button_click(data):
    print("Button click event received on the server")
    # Check if the trigger message is received
    if 'message' in data and data['message'] == 'Trigger button clicked':
        # Emit a custom event to the client on the results.html page
        socketio.emit('show_popup', {'message': 'Pop-up triggered from index.html'})

if __name__ == "__main__":
    socketio.run(app, debug=True, host='0.0.0.0', port=8080, ssl_context=('cert.pem', 'key.pem'))
