from flask import Flask, request, render_template
import pymysql
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()
def get_db_connection():
    conn = pymysql.connect(
        host=os.environ['DB_HOST'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        database=os.environ['DB_NAME'],
        #ssl={'ca': 'C:/Users/shrih/Downloads/DigiCertGlobalRootCA.crt.pem'}  # SSL added here
        ssl_disabled=True  
    )
    return conn

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        return render_template('welcome.html', name=username)
    else:
        return "Invalid credentials. Try again."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

#git status
#git add .
#git commit -m "initial"
#git push origin
#gunicorn app:app --host 0.0.0.0 --port 8000
<<<<<<< HEAD
#gunicorn --bind=0.0.0.0 --timeout 600 login_app.app:app
#gunicorn --chdir login_app app:app
=======
>>>>>>> 74f17e46a9c8dfb54f97f2afd18383d1b672ac2b
