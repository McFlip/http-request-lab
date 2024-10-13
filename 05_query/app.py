from flask import Flask, request

app = Flask(__name__)

@app.route("/search")
def search():
    name = request.args.get('name')
    food = request.args.get('food')
    return f"Hello, {name}, I also like {food}! Here is a recipe..."
