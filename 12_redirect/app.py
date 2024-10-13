from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/login")
def login():
    return "Please enter credentials"
