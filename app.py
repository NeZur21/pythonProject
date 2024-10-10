import flask
from http.server import HTTPServer, SimpleHTTPRequestHandler

from flask import render_template

app = flask.Flask(__name__)

@app.route('/')
def contact_list():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True)