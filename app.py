from flask import Flask, render_template

app = Flask(__name__)
app.static_url_path = '/static'
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080, ssl_context=('cert.pem', 'key.pem'))
