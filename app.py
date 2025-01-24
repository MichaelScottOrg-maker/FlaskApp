from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import pyodbc
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

def get_db_connection():
    conn = pyodbc.connect(
        'Driver={ODBC Driver 18 for SQL Server};Server=tcp:test.database.windows.net,1433;Database=proddbsharpcoding;Uid=test;Pwd=test;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
    )
    return conn

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Here you can add logic to check the username and password
    if username == 'admin' and password == 'password':  # Example check
        return redirect(url_for('success'))
    else:
        return redirect(url_for('index'))


@app.route('/users')
def user_list():
    search_query = request.args.get('search', '')
    conn = get_db_connection()
    cursor = conn.cursor()
    if search_query:
        query = "SELECT name, surname FROM Myusers WHERE name = '" +    search_query + "'"
        cursor.execute(query)
    else:
        cursor.execute("SELECT name, surname FROM Myusers")
    rows = cursor.fetchall()
    conn.close()
    users = [{'name': row.name, 'surname': row.surname} for row in rows]

    return render_template('user_list.html', users=users)

@app.route('/upload', methods=['POST'])
def upload_file():
    # Azure Storage account connection string
    connect_str = "DefaultEndpointsProtocol=https;AccountName=test;AccountKey=test==;EndpointSuffix=core.windows.net"
    container_name = "sharpcodingcontainer"

    eicar_file_content = (
        "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
    )
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob="eicar_test_file.txt")

    # Upload the file
    blob_client.upload_blob(eicar_file_content, overwrite=True)

    return redirect(url_for('upload_success'))


@app.route('/upload_success')
def upload_success():
    return render_template('upload_success.html')
    
@app.route('/success')
def success():
    return render_template('login_success.html')

if __name__ == '__main__':
    app.run(debug=True)
