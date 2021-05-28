from flask import Flask,request,render_template
from flaskext.mysql import MySQL

mysql= MySQL()
app = Flask(__name__)
app.config['MYSQL DATABASE_USER'] = 'root'
app.config['MYSQL DATABASE_PASSWORD'] = 'root'
app.config['MYSQL DATABASE_DB'] = 'test'
app.config['MYSQL DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def my_from():
    return render_template('from_ex.html')

@app.route('/', methods=['POST'])
def Authenticate():
    username = request.form['u']
    password = request.form['p']
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from User where username='"+username+"'and password='"+password +"'")
    data = cursor.fetchone()
    if data is None:
        return "Username or Password is wrong"
    else:
        return "Logged in successfully"

if __name__ == "__main__":
    app.debug = True
    app.run(port=5001)

