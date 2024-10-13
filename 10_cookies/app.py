from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def cookies():
    pref = dict()
    pref["theme"] = request.cookies.get("theme")
    pref["language"] = request.cookies.get("language")
    return pref
