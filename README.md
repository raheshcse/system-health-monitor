🚀 System Health Monitor with AI Anomaly Detection

A real-time system monitoring dashboard that tracks CPU, memory, and disk usage, and applies machine learning to detect anomalies in system behavior. The project includes a live web dashboard built with Flask and dynamic visualizations using Chart.js.

---

📌 Overview

This project simulates a lightweight **observability and monitoring system**, similar to tools like Grafana. It continuously collects system metrics and provides real-time insights through a web-based dashboard, enhanced with AI-driven anomaly detection.

---

⚙️ Features

- 📊 Real-time CPU, Memory, and Disk monitoring
- 🤖 AI-based anomaly detection using Isolation Forest
- 🌐 Flask web dashboard
- 📈 Live updating charts (Chart.js)
- 📝 Logging system for system activity
- ⚡ REST API for dynamic data updates
- 🎨 Modern responsive UI with color-coded indicators

---

🧠 AI Component

The project uses the **Isolation Forest algorithm** from Scikit-learn to identify unusual system behavior.

- Trained on historical system metrics
- Detects outliers (unexpected spikes or drops)
- Can be extended for real-time alerting systems

---

🏗️ Architecture

[ System Metrics ]
↓
monitor.py (Data Collection)
↓
CSV Storage / Live API
↓
Flask Backend (app.py)
↓
REST API (/data)
↓
Frontend Dashboard (HTML + Chart.js)

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Data Processing:** Pandas
- **Machine Learning:** Scikit-learn (Isolation Forest)
- **System Monitoring:** psutil
- **Frontend:** HTML, CSS, Chart.js
- **Logging:** Python logging module

---

## 📂 Project Structure

System Health Monitor/
│
├── app.py # Flask backend
├── monitor.py # System metrics collector
├── anomaly.py # ML anomaly detection
├── requirements.txt # Dependencies
│
├── templates/
│ └── index.html # Dashboard UI
│
├── data/
│ └── system_metrics.csv
│
├── logs/
│ └── system.log


