from flask import Flask
from config import load_config

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

if __name__ == "__main__":
    app.run(debug=True)



'''
config = load_config(mode)
app = Flask(__name__)
app.config.from_object(config)
'''

'''
#execute in a development env
#debug
#port host
#commands to start flask application
#requirement.txt
#folder structure in flask

'''



'''
flaskr/, a Python package containing your application code and files.

tests/, a directory containing test modules.

venv/, a Python virtual environment where Flask and other dependencies are installed.
'''
