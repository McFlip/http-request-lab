from flask import Flask, request, send_from_directory 
import base64
import os

app = Flask(__name__)

my_profile = dict()

@app.route("/profile", methods=["POST"])
def profile():
    my_profile["name"] = request.form["name"]
    my_profile["email"] = request.form["email"]
    request.files["avatar"].save("uploads/avatar.jpg")
    my_profile["avatar"] = base64.b64encode(open("uploads/avatar.jpg", "rb").read()).decode("utf-8")
    return my_profile

@app.route("/profile/avatar")
def avatar():
    full_path = os.path.join(app.root_path, 'uploads')
    return send_from_directory(full_path, 'avatar.jpg')
