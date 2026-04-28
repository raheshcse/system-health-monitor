import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Load data
data = pd.read_csv("data/system_metrics.csv")

# Convert timestamp
data['timestamp'] = pd.to_datetime(data['timestamp'])

# Train model (same logic)
X = data[['cpu', 'memory', 'disk']]
model = IsolationForest(contamination=0.05, random_state=42)
data['anomaly'] = model.fit_predict(X)

# Separate anomalies
anomalies = data[data['anomaly'] == -1]

# Plot normal data
plt.plot(data['timestamp'], data['cpu'], label='CPU')
plt.plot(data['timestamp'], data['memory'], label='Memory')
plt.plot(data['timestamp'], data['disk'], label='Disk')

# 🔥 Highlight anomalies
plt.scatter(anomalies['timestamp'], anomalies['cpu'], marker='x', label='Anomaly')

plt.xlabel("Time")
plt.ylabel("Usage (%)")
plt.title("System Health Monitoring with Anomaly Detection")
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()