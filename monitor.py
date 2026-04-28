import psutil
import time
import csv
from datetime import datetime
import os
import logging

# Create folders
os.makedirs("data", exist_ok=True)
os.makedirs("logs", exist_ok=True)

# Logging setup
logging.basicConfig(
    filename='logs/system.log',
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
)

file_path = "data/system_metrics.csv"

# ✅ FIX: Always ensure correct header
if not os.path.exists(file_path):
    with open(file_path, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "cpu", "memory", "disk"])
else:
    # 🔥 NEW: Check if 'disk' column exists
    with open(file_path, 'r') as f:
        header = f.readline().strip()

    if "disk" not in header:
        print("⚠️ Old CSV detected. Recreating with correct format...")

        # Backup old file (optional)
        os.rename(file_path, file_path + ".old")

        # Create new correct file
        with open(file_path, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "cpu", "memory", "disk"])

print("🚀 System Monitor Started... (Press Ctrl + C to stop)")
logging.info("System Monitor Started")

try:
    while True:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_message = f"CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%"

        # Console output
        print(f"{timestamp} | {log_message}")

        # Log file
        logging.info(log_message)

        # Save to CSV
        with open(file_path, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, cpu, memory, disk])

        time.sleep(2)

except KeyboardInterrupt:
    print("\n🛑 Monitoring stopped by user.")
    logging.info("System Monitor Stopped")