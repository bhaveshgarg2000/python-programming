from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/b")
def bhavesh():
    return "Hello, Bhavesh Krishan Garg!"

app.run(debug=True)