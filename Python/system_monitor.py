import psutil
import time
import csv

# CSV file setup
csv_file = "system_usage_log.csv"
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Time", "CPU Usage (%)", "Memory Usage (%)", "Disk Usage (%)"])

def log_system_usage():
    """Fetch and log system resource usage in real-time."""
    while True:
        # Get system stats
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        # Print system stats
        print(f"[{timestamp}] CPU: {cpu_usage}% | Memory: {memory_usage}% | Disk: {disk_usage}%")

        # Write to CSV log
        with open(csv_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, cpu_usage, memory_usage, disk_usage])

        time.sleep(2)  # Update every 2 seconds

if __name__ == "__main__":
    log_system_usage()
