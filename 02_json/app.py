from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello_world():
    data = request.get_json()
    name = data.get('name')
    return dict({ "msg": f"Hello, {name}"})
