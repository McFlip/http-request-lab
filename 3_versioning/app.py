from flask import Flask

app = Flask(__name__) 

@app.route("/v1/info")
def v1():
    return dict({
        "version": 1,
        "msg": "Old and busted"
    })

@app.route("/v2/info")
def v2():
    return dict({
        "version": 2,
        "message": "New Hotness!"
    })
