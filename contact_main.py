# contact_main.py
from flask import Flask, render_template, request, redirect, url_for
from contact_services import ContactServices

contact_main = Flask(__name__)
contact_service = ContactServices()

@contact_main.route('/')
def main():
    return render_template('base.html')

@contact_main.route('/contact')
def all_contacts():
    contacts = contact_service.get_all_contacts()
    return render_template('contacts.html', contacts=contacts)

@contact_main.route('/contact/edit/<int:contact_id>', methods=['GET', 'POST'])
def edit_contact(contact_id):
    contact = contact_service.get_contact_by_id(contact_id)
    if request.method == 'POST':
        contact_service.update_contact(
            contact_id,
            request.form['name'],
            request.form['phone'],
            request.form['email']
        )
        return redirect(url_for('all_contacts'))  # Здесь правильный вызов
    return render_template('edit_contact.html', contact=contact)

@contact_main.route('/contact/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        contact_service.add_contact(
            request.form['name'],
            request.form['phone'],
            request.form['email']
        )
        return redirect(url_for('all_contacts'))  # Здесь правильный вызов
    return render_template('add_contact.html')

@contact_main.route('/contact/delete/<int:contact_id>')
def delete_contact(contact_id):
    contact_service.delete_contact(contact_id)
    return redirect(url_for('all_contacts'))  # Здесь правильный вызов

if __name__ == '__main__':
    contact_main.run(debug=True)  # Запускаем приложение