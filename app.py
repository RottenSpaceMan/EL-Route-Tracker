from flask import Flask, render_template, request
import json

app = Flask(__name__)
app.static_url_path = '/static'
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/home')
def home():
    return render_template('front.html')

@app.route('/demo-bus')
def demobus():
    return render_template('demo-bus.html')

@app.route('/process_location', methods=['POST'])
def process_location():
    # Get latitude and longitude from the form
    latitude = request.form['latitude']
    longitude = request.form['longitude']

    # Create a dictionary to store the data
    data = {
        'latitude': latitude,
        'longitude': longitude
    }

    # Write the data to a JavaScript file in the static folder
    with open('static/location.js', 'w') as js_file:
        js_file.write('var locationData = {};'.format(json.dumps(data)))

    return 'Data saved successfully.'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080, ssl_context=('cert.pem', 'key.pem'))
