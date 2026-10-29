from flask import Flask, request, jsonify
from flask_cors import CORS
from calculator import *

app = Flask(__name__)
CORS(app)

@app.route("/calculate", methods=["POST"])
def calculate():

    data = request.json

    a = float(data["num1"])
    b = float(data["num2"])
    op = data["operation"]

    if op == "add":
        result = add(a, b)
    elif op == "subtract":
        result = subtract(a, b)
    elif op == "multiply":
        result = multiply(a, b)
    elif op == "divide":
        result = divide(a, b)

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(port=5000, debug=True)