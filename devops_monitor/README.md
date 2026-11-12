# DevOps Monitor v1

Collects CPU, memory and disk usage on a Linux machine, stores it in PostgreSQL, and loads it incrementally so re-running never duplicates rows.

## How it works
1. **Collect:** `collect_metrics.sh` prints one CSV line (`timestamp,cpu,memory,disk`). Cron runs it every 5 minutes and appends to `data/metrics.csv`. CPU comes from `mpstat` (package `sysstat`).
2. **Load:** `ingest_metrics.py` reads the CSV and inserts only rows newer than the latest `metric_time` already in the `system_metrics` table (an incremental, watermark-style load). It needs a PostgreSQL database called `log_monitor` and the `psycopg2` package.
3. **Analyse:** `queries.sql` has example queries: latest rows, min/max/average, a threshold filter and hourly buckets with `date_trunc`.

## Table used
`system_metrics(metric_time, cpu_usage, memory_usage, disk_usage)`

## Cron entry
```
*/5 * * * * /path/to/devops_monitor/collect_metrics.sh >> /path/to/devops_monitor/data/metrics.csv
```

## Still to do
Screenshots of the results, a committed `schema.sql`, and multi-host support (roadmap step 9).
