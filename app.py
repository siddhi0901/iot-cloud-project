from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

data_store = []

@app.route('/')
def home():
    return jsonify({"message": "IoT Backend is live 🚀", "status": "running"})

@app.route('/data', methods=['POST'])
def receive_data():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data received"}), 400

        data_store.append(data)

        return jsonify({"status": "received"}), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500

@app.route('/data', methods=['GET'])
def send_data():
    return jsonify(data_store)

if __name__ == '__main__':
    app.run()
