import flask
import db

from flask import render_template, request, redirect

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
def main():
    return render_template('base.html')

@app.route('/all_contacts')
def all_contacts():
    return render_template('contacts.html', contacts=contacts)

@app.route('/edit_contact/<int:contact_id>', methods=['GET', 'POST'])
def edit_contact(contact_id):
    contact = next((c for c in contacts if c.id == contact_id), None)
    if request.method == 'POST':
        contact.name = request.form['name']
        contact.phone = request.form['phone']
        contact.email = request.form['email']
        return redirect(flask.url_for('all_contacts'))
    return render_template('edit_contact.html', contact=contact)



if __name__ == '__main__':
    app.run(debug=True)