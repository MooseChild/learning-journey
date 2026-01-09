#!/usr/bin/env bash

TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

# CPU usage (percentage) using mpstat idle%
CPU_USAGE=$(mpstat 1 1 | awk '/Average/ && $NF ~ /^[0-9.]+$/ {printf "%.2f", 100 - $NF}')

# Memory usage (percentage)
MEMORY_USAGE=$(free | awk '/Mem/ {printf "%.2f", $3/$2 * 100}')

# Disk usage (root filesystem)
DISK_USAGE=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')

# Output as CSV (easy for Python)
echo "$TIMESTAMP,$CPU_USAGE,$MEMORY_USAGE,$DISK_USAGE"
