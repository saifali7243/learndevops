🚀 DevOps Observability Stack — JARVIS War Room








A production-style DevOps observability platform built with Docker, Prometheus, and Grafana.

This project demonstrates real-world monitoring of:

🖥 Host system metrics

🐳 Docker container metrics

🌐 Application-level metrics

🔔 Automated alerting via Telegram

Designed as a complete Infrastructure-as-Code monitoring stack.

🧠 Architecture
Flask App  ───────────►  Prometheus  ───────────►  Grafana
     │                        ▲
     │                        │
     ▼                        │
  /metrics                Node Exporter
                               ▲
                               │
                           cAdvisor
Data Flow

Flask app exposes /metrics

Prometheus scrapes:

Application metrics

Host metrics (Node Exporter)

Container metrics (cAdvisor)

Grafana visualizes metrics

Alert rules trigger Telegram notifications

📁 Project Structure
learndevops/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── prometheus.yml
│
├── grafana/
│   └── provisioning/
│       ├── datasources/
│       │   └── prometheus.yml
│       ├── dashboards/
│       │   └── dashboards.yml
│       └── alerting/
│           ├── alert-rules.yml
│           ├── contact-points.yml
│           └── notification-policies.yml
│
├── grafana-dashboards/
│   ├── jarvis-war-room.json
│   └── additional-dashboards.json
│
└── README.md
⚙️ Prerequisites

Docker

Docker Compose

Git

🚀 Setup
1. Clone the Repository
git clone https://github.com/saifali7243/learndevops.git
cd learndevops
2. Configure Secrets (Secure Method)

Create a .env file in the project root:

touch .env

Add:

TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here

Add .env to .gitignore:

.env

⚠ Never commit API tokens to GitHub.

3. Start the Stack
docker compose up --build -d
🌐 Access the Services
Service	URL
Flask App	http://localhost:5000

Prometheus	http://localhost:9090

Grafana	http://localhost:3000

cAdvisor	http://localhost:8080

Node Exporter	http://localhost:9100
🔐 Grafana Login
Username: admin
Password: admin

(Change credentials in production.)

📊 Monitoring Coverage
🖥 Host System

CPU Usage %

Per-core CPU

Memory Usage %

Swap Usage %

Disk Usage %

Disk I/O

Load Average

Uptime

Network RX/TX

TCP Connections

File Descriptors

Context Switch Rate

System Temperature

🐳 Docker Monitoring

CPU % per container

Memory usage per container

Running containers count

Container restarts

Container health status

Container dropdown filtering

🌐 Application Monitoring

Total requests

Request rate

Error rate

Total errors

Application metrics endpoint:

http://localhost:5000/metrics
🔔 Alerting

Telegram integration configured via environment variables.

Alerts include:

Memory > 60% → Warning

Memory > 80% → Critical

Alert provisioning is managed under:

grafana/provisioning/alerting/
📈 Prometheus Targets

Verify scraping status:

http://localhost:9090/targets

Expected targets:

app

node_exporter

cadvisor

All should show UP.

🧪 Testing the Application

Generate traffic:

http://localhost:5000/

If error route exists:

http://localhost:5000/error
🔎 Useful PromQL Queries
Host CPU %
100 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100
Host Memory %
100 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes * 100)
Container CPU %
sum(rate(container_cpu_usage_seconds_total[5m])) by (container) * 100
Application Error Rate
rate(app_errors_total[5m])
💾 Persistence

Grafana and Prometheus use Docker volumes.

Avoid deleting volumes:

docker compose down -v

Use instead:

docker compose down
🛠 Troubleshooting
Grafana Restarting

Check logs:

docker logs grafana --tail 50

Common causes:

Invalid YAML provisioning

Incorrect alert contact point

Misconfigured datasource UID

Prometheus Not Scraping
docker logs prometheus

Then verify:

http://localhost:9090/targets
Telegram Alerts Not Sending

Ensure:

Bot token is valid

Chat ID is correct

Bot has been started via /start

.env file is loaded

🔒 Security Practices

Environment-based secrets

No hardcoded credentials

Docker volume persistence

File-based provisioning

Modular infrastructure layout

🚀 Future Enhancements

Loki log aggregation

Alertmanager integration

CI/CD pipeline

Kubernetes deployment

RBAC configuration

📜 License

MIT License

🎯 Summary

This project demonstrates:

Production-style monitoring stack

Infrastructure as Code provisioning

Secure secret management

Container and host observability

Professional dashboard design

Real-world DevOps practices