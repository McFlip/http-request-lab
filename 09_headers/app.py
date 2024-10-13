from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Publicly accessible"

@app.route("/secret")
def secret():
    if "Authorization" not in request.headers or request.headers["Authorization"] != "Bearer SecretSquirrel":
        return "Ah Ah Uh... You did't say the magic word!", 403
    else:
        return "The answer to life is 42"
