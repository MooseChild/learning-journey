# learning-journey
Data Engineering study notes and scripts

# Data Engineering Learning Journey

This repository tracks my transition into Data Engineering.

## Phase 0: Foundations & DevOps Monitor v1
I have built a local monitoring pipeline that tracks the health of my Proxmox development environment.

### Architecture
- **Collector:** Bash script (`collect_metrics.sh`) gathering CPU, RAM, and Disk stats.
- **Scheduler:** Linux `cron` running every 5 minutes.
- **Storage:** PostgreSQL database (`log_monitor`).
- **ETL:** Python script (`ingest_metrics.py`) using `psycopg2` for incremental data loading.

### Skills Mastered
- **Linux:** User management, SSH, Cron, Bash scripting.
- **SQL:** Schema design, Aggregations (`AVG`, `MAX`), Time-bucketing (`date_trunc`).
- **Python:** File I/O, JSON/CSV parsing, Database connectivity.
- **Git:** Version control, `.gitignore`, remote syncing.
