from flask import Flask, request

app = Flask(__name__)

fav_list = []
id = 0


@app.route("/colors/favorites", methods=["POST"])
def create_favorite():
    new_fav = request.json
    if new_fav is None:
        return {"error": "empty request"}, 400
    global id
    id += 1
    new_fav["id"] = id
    fav_list.append(new_fav)
    print("*UPDATED FAVORITES LIST*")
    print(fav_list)
    return {"id": id}


@app.route("/colors/favorites/<int:id>", methods=["GET", "PUT", "DELETE"])
def favorite(id):
    if request.method == "GET":
        print("*FAVORITES LIST*")
        print(fav_list)
        try:
            return fav_list[id - 1]
        except IndexError:
            return {"error": "id not found"}, 404
    elif request.method == "PUT":
        new_fav = request.json
        if new_fav is None:
            return {"error": "empty request"}, 400
        new_fav["id"] = id
        fav_list[id - 1] = new_fav
        print("*UPDATED FAVORITES LIST*")
        print(fav_list)
        return {"message": "Successfully updated favorite"}
    else:
        del fav_list[id - 1]
        print("*UPDATED FAVORITES LIST*")
        print(fav_list)
        return {"message": "Successfully deleted favorite"}
