from flask import Flask

app = Flask(__name__)

users = dict({
    1: {"name": "Alice"},
    2: {"name": "Bob"}
})

@app.route("/users/<int:user_id>")
def get_users(user_id):
    return users[user_id]
