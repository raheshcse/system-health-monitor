from flask import Flask, render_template, jsonify
import pandas as pd
from sklearn.ensemble import IsolationForest

app = Flask(__name__)

# 🟢 MAIN DASHBOARD
@app.route('/')
def dashboard():
    data = pd.read_csv("data/system_metrics.csv")

    # Safety fix (prevents crash)
    if 'disk' not in data.columns:
        data['disk'] = 0

    # Latest values
    latest = data.iloc[-1]

    return render_template(
        'index.html',
        cpu=latest['cpu'],
        memory=latest['memory'],
        disk=latest['disk']
    )

# 🔵 NEW API FOR LIVE DATA (ADD THIS)
@app.route('/data')
def get_data():
    data = pd.read_csv("data/system_metrics.csv")

    if 'disk' not in data.columns:
        data['disk'] = 0

    data = data.tail(20)

    return jsonify({
        "timestamps": data['timestamp'].tolist(),
        "cpu": data['cpu'].tolist(),
        "memory": data['memory'].tolist(),
        "disk": data['disk'].tolist()
    })

# 🚀 RUN APP
if __name__ == '__main__':
    app.run(debug=True)