from flask import Flask, Response
from random import randint

app = Flask(__name__)

# animal generator route here
@app.route('/animal', methods=['GET'])
def animal():
    animals = ["pig","cow","horse"]
    animal = animals[randint(0,len(animals)-1)]
    return animal

# animal noise generator route here
@app.route('/noise/<string:key>', methods=['POST'])
def noise(key):
    noise = {"pig":"oink","cow":"moo","horse":"neigh"}
    if key not in noise:
        return Response(key +" currently not defined")
    else:
        return Response("The "+ key + " goes "+f'{noise[key]}')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)