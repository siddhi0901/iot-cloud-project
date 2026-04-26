from flask import Flask, request, jsonify
from flask_cors import CORS
from db import insert_data, get_all_data
import os

app = Flask(__name__)
CORS(app)

# 🔹 POST API
@app.route('/data', methods=['POST'])
def receive_data():
    try:
        content = request.get_json()

        if content is None:
            return jsonify({"error": "No data received"}), 400

        if "temperature" not in content or "humidity" not in content:
            return jsonify({"error": "Missing fields"}), 400

        insert_data(content)

        return jsonify({
            "status": "success",
            "message": "Data stored successfully"
        }), 200

    except Exception as e:
        return jsonify({
            "error": "Server error",
            "details": str(e)
        }), 500


# 🔹 GET API
@app.route('/data', methods=['GET'])
def send_data():
    try:
        data = get_all_data()
        return jsonify(data if data else []), 200

    except Exception as e:
        return jsonify({
            "error": "Failed to fetch data",
            "details": str(e)
        }), 500


# 🔹 Health check route (VERY IMPORTANT for Render)
@app.route('/')
def home():
    return jsonify({
        "status": "running",
        "message": "IoT Backend is live 🚀"
    })


# 🔹 Run server (Render + Local compatible)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


