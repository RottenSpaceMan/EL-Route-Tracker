from flask import Flask, render_template

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    socketio.run(app, debug=True, host='0.0.0.0', port=8080, ssl_context=('cert.pem', 'key.pem'))
