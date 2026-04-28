import pandas as pd
from sklearn.ensemble import IsolationForest
import time

file_path = "data/system_metrics.csv"

print("🤖 Training anomaly detection model...")

# Load existing data
data = pd.read_csv(file_path)

# Use numeric columns
X_train = data[['cpu', 'memory']]

# Train model
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(X_train)

print("✅ Model trained. Starting real-time monitoring...\n")

last_checked_index = len(data)

try:
    while True:
        # Reload data (new rows added by monitor.py)
        data = pd.read_csv(file_path)

        # Check if new data is available
        if len(data) > last_checked_index:
            new_data = data.iloc[last_checked_index:]

            for _, row in new_data.iterrows():
                sample = [[row['cpu'], row['memory']]]
                prediction = model.predict(sample)

                if prediction[0] == -1:
                    print(f"🚨 ALERT at {row['timestamp']} | CPU: {row['cpu']} | Memory: {row['memory']}")
                else:
                    pass  # only show alerts

            last_checked_index = len(data)

        time.sleep(2)

except KeyboardInterrupt:
    print("\n🛑 Anomaly detection stopped.")