
from flask import Flask
from flask_mysqldb import MySQL
from flask import request
from flask import render_template
mysql = MySQL()
app = Flask(__name__)
# My SQL Instance configurations 
# Change the HOST IP and Password to match your instance configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ILoveGoogle'
app.config['MYSQL_DB'] = 'studentbook'
app.config['MYSQL_HOST'] = '35.195.18.23'
mysql.init_app(app)

@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/contact-me')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000') #Run the flask app at port 5000
