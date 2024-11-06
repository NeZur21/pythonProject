import pyodbc

def get_db_connection():
    return pyodbc.connect(
        'DRIVER=ODBC Driver 17 for SQL Server; TrustServerCertificate=No; DATABASE=Contacts; '
        'WSID=DESKTOP-FONUECB; Trusted_Connection=Yes; SERVER=localhost'
    )