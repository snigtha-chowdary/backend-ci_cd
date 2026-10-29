from flask import Flask, request, jsonify
from flask_cors import CORS
from calculator import *
from db import get_connection

app = Flask(__name__)
CORS(app)

@app.route("/calculate", methods=["POST"])
def calculate():

    data = request.json

    num1 = float(data["num1"])
    num2 = float(data["num2"])
    operation = data["operation"]

    if operation == "add":
        result = add(num1, num2)

    elif operation == "subtract":
        result = subtract(num1, num2)

    elif operation == "multiply":
        result = multiply(num1, num2)

    elif operation == "divide":
        result = divide(num1, num2)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO calculations
        (operation, num1, num2, result)
        VALUES (%s, %s, %s, %s)
        """,
        (operation, num1, num2, result)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"result": result})

@app.route("/history", methods=["GET"])
def history():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM calculations
        ORDER BY created_at DESC
        """
    )

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)