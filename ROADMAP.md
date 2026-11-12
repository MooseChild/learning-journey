# Data Engineering Roadmap (AWS first)

Eleven steps, taken in order. Each is finished when it feels properly practised, with a target of roughly six months for the whole ladder. These are personal learning goals. Last updated 2026-11-12.

## Credentials

| Credential | Status |
|---|---|
| AWS Certified AI Practitioner (AIF-C01) | Held. [Credly badge](https://www.credly.com/go/hZCJ3YVqqUlSSkh230B0fQ). Taken for a promotion, so it is not a roadmap step |
| AWS Certified Cloud Practitioner (CLF-C02) | Not yet held. Exam booked for 2026-11-30 |

## Progress

| Step | Goal | Status |
|---|---|---|
| 1 | AWS Cloud Practitioner (CLF-C02) | Course in progress, exam booked for 2026-11-30 |
| 2 | AWS Data Engineer Associate (DEA-C01) | Not started |
| 3 | Database fundamentals and normalisation (1NF to 3NF) | Partly done: Postgres schema in use by the monitor; ERD and `schema.sql` still to do |
| 4 | Analytics modelling and ETL patterns | Partly done: incremental load script and [SQL cheat sheet](devops_monitor/queries.sql); star schema still to do |
| 5 | DevOps Monitor v1 | Built in January 2026, see [`devops_monitor/`](devops_monitor/). Screenshots and a fuller README still to do |
| 6 | IBM Data Engineering Professional Certificate | Not started |
| 7 | Mock Data Lake (homelab) | Not started |
| 8 | Cloud Data Pipeline (AWS) | Not started |
| 9 | DevOps Monitor v2 and v3 (multi-host, Grafana, alerting) | Not started |
| 10 | Capstone (homelab plus AWS) | Not started |
| 11 | Interview preparation | Not started |

App development has taken priority recently, so the next ladder step is the CLF-C02 exam on 2026-11-30.

## The steps

1. **AWS Cloud Practitioner (CLF-C02).** Core AWS vocabulary: global infrastructure, IAM, EC2/S3/RDS basics, pricing and support plans. *Proof:* certificate or badge; 1 to 2 pages of notes.
2. **AWS Data Engineer Associate (DEA-C01).** S3 as a data lake, Glue, Redshift, Athena, Kinesis, EMR. *Proof:* certificate or badge; a one-page "which service for which data problem" cheat sheet.
3. **Database fundamentals and normalisation.** Normal forms, keys and constraints, bridge tables, how poor design causes data-quality problems. *Proof:* ERD, `schema.sql`, README on design trade-offs.
4. **Analytics modelling and ETL patterns.** Fact and dimension tables, star schema, full vs incremental loads, idempotency, watermarks, late-arriving data, data-quality checks. *Proof:* star schema DDL, a small incremental ETL script, a tool-agnostic write-up.
5. **DevOps Monitor v1.** Bash collector, cron schedule, Python load into Postgres. *Proof:* repo, metrics table with sample data, screenshots.
6. **IBM Data Engineering Professional Certificate (Coursera).** ETL, SQL and NoSQL, warehousing, Spark basics. *Proof:* certificate and notes.
7. **Mock Data Lake.** Raw and clean zones, ingestion, Python ETL into Postgres, dashboards. *Proof:* repo, architecture diagram, dashboards.
8. **Cloud Data Pipeline (AWS).** S3 raw zone, Glue transforms, Redshift, visualisation. *Proof:* repo, runbook, diagram, data flowing end to end.
9. **DevOps Monitor v2 and v3.** Several machines feeding one database, Grafana dashboards, alerts. *Proof:* updated repo, screenshots, an alert firing on a test event.
10. **Capstone.** One hybrid homelab and AWS project to walk through in interviews. *Proof:* repo, diagrams, walkthrough script.
11. **Interview preparation.** SQL practice, explaining data models, pipeline walkthroughs, a story for each project. *Proof:* a 1 to 2 page interview pack.
