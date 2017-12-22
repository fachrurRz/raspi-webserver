"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import *
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

global_data = {'humidity': '10', 'temperature': '60'}

@app.route('/')
def index():
    """Return a friendly HTTP greeting."""
    # getData()
    data = {'merk': 'Panasonic', 'temperature': global_data['temperature'], 'humidity': global_data['humidity']}
    return render_template('index.html', data=data)

@app.route('/on/')
def turnOnAc():
    """Turn on"""
    # turnOn()
    data = {'merk': 'Panasonic', 'temperature': global_data['temperature'], 'humidity': global_data['humidity']}
    return render_template('index.html', data=data)

@app.route('/off/')
def turnOffAc():
    """Turn Off"""
    # turnOff()
    data = {'merk': 'Panasonic', 'temperature': global_data['temperature'], 'humidity': global_data['humidity']}
    return render_template('index.html', data=data)


@app.route('/update', methods=['POST'])
def update():
    humidity = request.form['humidity']
    temperature = request.form['temperature']

    global_data['humidity'] = humidity
    global_data['temperature'] = temperature

    return jsonify({'data': global_data}), 201


@app.route('/get-current', methods=['GET'])
def get_current():
    return jsonify({'data': global_data}), 200


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug = True, port=5000)
