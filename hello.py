from flask import Flask, request, jsonify, render_template
import hashlib
app = Flask(__name__)


# home route
@app.route('/') 
def welcome():
   return render_template('index.html')

@app.route('/new/<name>')
def user_name(name):
   return 'Hello World '+name

@app.route('/squre/<int:num>')
def number_squre(num):
   return 'Squre of Number is : '+ str(num**2)


#Image link route
@app.route("/submit", methods=["POST",'GET'])
def img_hash():
   if request.method == 'POST':

      im_path = request.form['path']
      #return (im_path) retun the link
      with open(im_path, "rb") as f:
         im_bytes = f.read()
      im_hash = str(hashlib.md5(im_bytes).hexdigest())
      return f"Hash Code  {im_hash}."
if __name__ == '__main__':
   app.run(debug=True)