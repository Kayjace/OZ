from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello oz"

@app.route("/hello")
def hello():
	  return "Hello Student"