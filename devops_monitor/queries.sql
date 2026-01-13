SELECT metric_time, cpu_usage, memory_usage 
FROM system_metrics 
ORDER BY metric_time DESC 
LIMIT 5;

SELECT 
    COUNT(*) as total_records,
    MIN(cpu_usage) as min_cpu,
    MAX(cpu_usage) as max_cpu,
    AVG(cpu_usage) as avg_cpu,
    AVG(memory_usage) as avg_mem
FROM system_metrics;

SELECT * 
FROM system_metrics 
WHERE cpu_usage > 0.5;

SELECT 
    date_trunc('hour', metric_time) as hour_bucket,
    AVG(cpu_usage) as avg_cpu,
    AVG(memory_usage) as avg_mem
FROM system_metrics
GROUP BY hour_bucket
ORDER BY hour_bucket DESC;


