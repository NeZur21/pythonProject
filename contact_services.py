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
        cursor.execute('SELECT id, Name, Phone, Email FROM Contact ')
        rows = cursor.fetchall()

        for i in rows:
            contacts.append(Contact(i.id, i.Name, i.Phone, i.Email))
        connection.close()
        return contacts

    def get_all_contacts(self):
        return self.contacts

    def get_contact_by_id(self, contact_id):
        return next((c for c in self.contacts if c.id == contact_id), None)

    def add_contact(self, name, phone, email):
        id = len(self.contacts) + 1
        new_contact = Contact(id, name, phone, email)
        self.contacts.append(new_contact)
        self.add_to_db(new_contact)

    def update_contact_in_db(self, contact):
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
                    UPDATE
                      dbo.Contact
                    SET
                      Name=?, Phone=?, Email=?
                    WHERE
                      id = ?
                    """
        cursor.execute(query, (contact.name, contact.phone, contact.email, contact.id,))
        print(*cursor.execute('SELECT id, Name, Phone, Email FROM Contact '))
        connection.commit()
        connection.close()

    def update_contact(self, contact_id, name, phone, email):
        contact = self.get_contact_by_id(contact_id)
        contact.name = name
        contact.phone = phone
        contact.email = email
        self.update_contact_in_db(contact)

    def add_to_db(self, contact):
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
                    INSERT INTO
                        dbo.Contact
                    VALUES
                        (?, ?, ?, ?)
                    """
        cursor.execute(query, (contact.id, contact.name, contact.phone, contact.email))
        print(*cursor.execute('SELECT id, Name, Phone, Email FROM Contact '))
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
                    FROM dbo.Contact WHERE id=?
                    """
        cursor.execute(query, (contact_id,))
        print(*cursor.execute('SELECT id, Name, Phone, Email FROM Contact '))
        connection.commit()
        connection.close()

