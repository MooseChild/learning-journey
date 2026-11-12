import os
import json
import psycopg2

REPORT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "report.json")

# Connect using the Unix socket as the current user (moosechild)
conn = psycopg2.connect(
    dbname="log_monitor",
    user="moosechild"
)

cur = conn.cursor()

with open(REPORT_FILE, "r") as f:
    data = json.load(f)

cur.execute(
    """
    INSERT INTO log_summary (total_lines, info_count, error_count)
    VALUES (%s, %s, %s)
    """,
    (data["total_lines"], data["info_count"], data["error_count"])
)

conn.commit()
cur.close()
conn.close()

print("Report inserted into database successfully!")
