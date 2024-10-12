import pyodbc

connection = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server; TrustServerCertificate=No; DATABASE=Contacts; WSID=DESKTOP-FONUECB; Trusted_Connection=Yes; SERVER=localhost')
cursor = connection.cursor()
cursor.execute('SELECT id, Name, Phone, Email FROM Contact ')
rows = cursor.fetchall()