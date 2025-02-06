from flask import Flask, request, jsonify
from flask_cors import CORS  # Allow CORS for external access
from calculator import calculate  # Import function from calculator.py

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/calculate', methods=['POST'])
def calculate_api():
    data = request.json
    try:
        num1 = float(data.get("num1"))
        num2 = float(data.get("num2"))
        operator = data.get("operator")
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input"}), 400

    if operator is None:
        return jsonify({"error": "Missing operator"}), 400

    result = calculate(num1, num2, operator)

    if isinstance(result, dict):  # Handle errors from calculator.py
        return jsonify(result), 400

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
