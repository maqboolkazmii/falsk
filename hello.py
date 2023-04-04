from flask import Flask
from 
app = Flask(__name__)

api = A

@app.route('/')
def hello_world():
   return 'Hello World .'

@app.route('/new/<name>')
def user_name(name):
   return 'Hello World '+name

@app.route('/squre/<int:num>')
def number_squre(num):
   return 'Squre of Number is : '+ str(num**2)

if __name__ == '__main__':
   app.run(debug=True)