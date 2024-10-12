import flask
from http.server import HTTPServer, SimpleHTTPRequestHandler

from flask import render_template

app = flask.Flask(__name__)

class Contact:
    def __init__(self, id, name, phone, email):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email


contacts = [
    Contact(1, "Alice", "123456789", "alice@example.com"),
    Contact(2, "Bob", "987654321", "bob@example.com")
]

@app.route('/')
def contact_list():
    return render_template('base.html')

@app.route('/all_contacts')
def all_contacts():
    return render_template('contacts.html', contacts=contacts)


if __name__ == '__main__':
    app.run(debug=True)