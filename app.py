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

contacts = [
    Contact(1, "Alice", "123456789", "alice@example.com"),
    Contact(2, "Bob", "987654321", "bob@example.com")
]

@app.route('/')
def main():
    return render_template('base.html')

@app.route('/contact')
def all_contacts():
    return render_template('contacts.html', contacts=contacts)

@app.route('/contact/edit/<int:contact_id>', methods=['GET', 'POST'])
def edit_contact(contact_id):
    contact = next((c for c in contacts if c.id == contact_id), None)
    if request.method == 'POST':
        contact.name = request.form['name']
        contact.phone = request.form['phone']
        contact.email = request.form['email']
        return redirect(flask.url_for('all_contacts'))
    return render_template('edit_contact.html', contact=contact)

@app.route('/contact/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        new_contact = Contact(len(contacts) + 1, request.form['name'], request.form['phone'], request.form['email'])
        contacts.append(new_contact)
        return redirect(flask.url_for('all_contacts'))
    return render_template('add_contact.html')

@app.route('/contact/delete/<int:contact_id>')
def delete_contact(contact_id):
    global contacts
    contacts = [c for c in contacts if c.id != contact_id]
    return redirect(flask.url_for('all_contacts'))

if __name__ == '__main__':
    app.run(debug=True)