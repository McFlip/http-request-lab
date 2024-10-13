from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "example.com"}})

@app.route("/api/cors", methods=["OPTIONS", "GET"])
def cors():
  return "You should not be able to reach me by clicking the button."

