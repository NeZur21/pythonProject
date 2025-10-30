import db

from contact import Contact
from db import get_db_connection


class ContactServices:
    def __init__(self):
        self.contacts = self.load_contacts_from_db()

    def load_contacts_from_db(self):
        contacts = []
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT,
            Phone TEXT,
            Email TEXT,
            Organization TEXT,
            Birthday DATE
        )
        ''')
        connection.commit()
        cursor.execute("SELECT id, Name, Phone, Email, Organization, Birthday FROM users")
        rows = cursor.fetchall()

        for i in rows:
            contacts.append(Contact(i[0], i[1], i[2], i[3], i[4], i[5]))
        connection.close()
        return contacts

    def get_all_contacts(self):
        return self.contacts

    def get_contact_by_id(self, contact_id):
        return next((c for c in self.contacts if c.id == contact_id), None)

    def add_contact(self, name, phone, email, org, date):
        new_contact = Contact(None, name, phone, email, org, date)
        self.add_to_db(new_contact)
        self.contacts.append(new_contact)

    def update_contact_in_db(self, contact):
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
                UPDATE users
                SET Name=?, Phone=?, Email=?, Organization=?, Birthday=?
                WHERE id=?
            """
        cursor.execute(query, (contact.name, contact.phone, contact.email, contact.org, contact.date, contact.id,))
        print(*cursor.execute('SELECT id, Name, Phone, Email, Organization, Birthday FROM users '))
        connection.commit()
        connection.close()

    def update_contact(self, contact_id, name, phone, email, org, date):
        contact = self.get_contact_by_id(contact_id)
        contact.name = name
        contact.phone = phone
        contact.email = email
        contact.org = org
        contact.date = date
        self.update_contact_in_db(contact)

    def add_to_db(self, contact):
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
                    INSERT INTO users (Name, Phone, Email, Organization, Birthday)
        VALUES (?, ?, ?, ?, ?)
                    """
        cursor.execute(query, (contact.name, contact.phone, contact.email, contact.org, contact.date))
        print(*cursor.execute('SELECT id, Name, Phone, Email, Organization, Birthday FROM users '))
        contact.id = cursor.lastrowid
        connection.commit()
        connection.close()

    def delete_contact(self, contact_id):
        self.contacts = [c for c in self.contacts if c.id != contact_id]
        self.delete_contact_from_db(contact_id)

    def delete_contact_from_db(self, contact_id):
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
                    DELETE
                    FROM users WHERE id=?
                    """
        cursor.execute(query, (contact_id,))
        print(*cursor.execute('SELECT id, Name, Phone, Email, Organization, Birthday FROM users '))
        connection.commit()
        connection.close()

