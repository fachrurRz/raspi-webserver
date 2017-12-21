"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import *
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def index():
    """Return a friendly HTTP greeting."""
    # getData()
    data = {'merk': 'Panasonic', 'temperature': '29', 'humidity': '50'}
    return render_template('index.html', data=data)

@app.route('/on/')
def turnOnAc():
    """Turn on"""
    # turnOn()
    data = {'merk': 'Panasonic', 'temperature': '29', 'humidity': '50'}
    return render_template('index.html', data=data)

@app.route('/off/')
def turnOffAc():
    """Turn Off"""
    # turnOff()
    data = {'merk': 'Panasonic', 'temperature': '29', 'humidity': '50'}
    return render_template('index.html', data=data)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500

if __name__ == '__main__':
    app.run(debug = True, port=5000)
