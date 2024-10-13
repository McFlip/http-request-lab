from flask import Flask, request

app = Flask(__name__)

@app.route("/order", methods=["POST"])
def order():
    my_order = dict()
    my_order["crust"] = request.form["crust"]
    my_order["sauce"] = request.form["sauce"]
    my_order["toppings"] = request.form.getlist("topping")
    print(request.form)
    return my_order

