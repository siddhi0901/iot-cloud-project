import requests
import random
import time

# 🔹 Replace with Render URL after deployment
API_URL = "http://127.0.0.1:5000/data"

print("Sensor Simulator Started...")

while True:
    data = {
        "device_id": f"sensor_{random.randint(1,3)}",
        "temperature": round(random.uniform(20, 35), 2),
        "humidity": round(random.uniform(40, 80), 2)
    }

    try:
        response = requests.post(API_URL, json=data)
        print("Sent:", data, "| Status:", response.status_code)

    except Exception as e:
        print("Error:", e)

    time.sleep(5)