# 🌐 Cloud-Based IoT Data Processing System

## 📌 Description
This project simulates IoT sensors sending temperature and humidity data to a Flask API.  
The data is stored in MongoDB Atlas and can be accessed via REST API.

---

## ⚙️ Technologies Used
- Python
- Flask
- MongoDB Atlas
- PyMongo
- HTML (optional frontend)
- Render (Deployment)

---

## 🏗️ Architecture
Sensor → Flask API → MongoDB → Dashboard/API

---

## 🚀 How to Run

### 1. Install dependencies
pip install -r requirements.txt

### 2. Run backend
python app.py

### 3. Run simulator
python sensor_simulator.py

---

## ☁️ API Endpoints

GET /data → Fetch sensor data  
POST /data → Send sensor data  

---

## 🗄️ Database
MongoDB Atlas Cloud Database

---

## 👨‍💻 Author
IoT Cloud Project (Student Project)