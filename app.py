import flask
import db

from flask import render_template

app = flask.Flask(__name__)

class Contact:
    def __init__(self, id, name, phone, email):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email

contacts = []

for i in db.rows:
    contacts.append(Contact(i.id, i.Name, i.Phone, i.Email))

@app.route('/')
def contact_list():
    return render_template('base.html')

@app.route('/all_contacts')
def all_contacts():
    return render_template('contacts.html', contacts=contacts)


if __name__ == '__main__':
    app.run(debug=True)