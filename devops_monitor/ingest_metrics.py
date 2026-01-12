import psycopg2
from datetime import datetime

CSV_FILE = "/home/moosechild/projects/learning-journey/devops_monitor/data/metrics.csv"

conn = psycopg2.connect(
    dbname="log_monitor",
    user="moosechild"
)

cur = conn.cursor()

# Get last processed timestamp
cur.execute("SELECT COALESCE(MAX(metric_time), '1970-01-01') FROM system_metrics;")
last_timestamp = cur.fetchone()[0]

inserted = 0

with open(CSV_FILE, "r") as f:
    for line in f:
        ts, cpu, mem, disk = line.strip().split(",")

        metric_time = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")

        if metric_time <= last_timestamp:
            continue

        cur.execute(
            """
            INSERT INTO system_metrics (metric_time, cpu_usage, memory_usage, disk_usage)
            VALUES (%s, %s, %s, %s)
            """,
            (metric_time, cpu, mem, disk)
        )
        inserted += 1

conn.commit()
cur.close()
conn.close()

print(f"Inserted {inserted} new rows")
