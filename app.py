from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome, your app has been deployed'
