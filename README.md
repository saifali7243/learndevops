🚀 DevOps Observability Stack – JARVIS War Room

A complete DevOps monitoring stack built using:

🐳 Docker & Docker Compose

📊 Prometheus

📈 Grafana

🖥 Node Exporter

📦 cAdvisor

🌐 Flask Application with Prometheus Metrics

This project demonstrates real-world DevOps observability engineering including:

Host system monitoring

Docker container monitoring

Application-level metrics

Error tracking

Professional Grafana dashboards

Clean DevOps command-center UI

🧱 Architecture Overview
Flask App  →  Prometheus  →  Grafana
              ↑
         Node Exporter
              ↑
           cAdvisor
📂 Project Structure
devops-observability-stack/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── prometheus.yml
│
├── grafana-dashboards/
│   ├── jarvis-war-room-professional.json
│   ├── jarvis-war-room-v6.json
│   ├── jarvis-command-center-v4.json
│   └── ...
│
└── README.md

All dashboards are stored inside:

grafana-dashboards/

You can directly import them into Grafana.

⚙️ Features
🖥 HOST SYSTEM

🔥 Hero Memory Gauge

📈 Host Memory Graph (GB)

⚡ Host CPU Gauge

💻 CPU Per Core Graph

⏱ Uptime

💾 Disk Usage %

📊 Disk I/O (Read / Write)

📈 Load Average

🔄 Swap Usage %

🌐 Network RX/TX

🌡 System Temperature

🔌 TCP Connections

⚙ Running Processes

🐳 DOCKER MONITORING

CPU % Per Container

Memory MB Per Container

Running Containers Count

Docker Health

Container Dropdown Filter

🌐 APPLICATION METRICS

Total Requests

Request Rate

Error Rate

Total Errors

/metrics endpoint exposed for Prometheus

🛠 Setup Instructions
1️⃣ Clone Repository
git clone <your-repo-url>
cd devops-observability-stack
2️⃣ Start the Stack
docker compose up --build -d
🌍 Services & URLs
Service	URL
Flask App	http://localhost:5000

Prometheus	http://localhost:9090

Grafana	http://localhost:3000

cAdvisor	http://localhost:8080

Node Exporter	http://localhost:9100
🔐 Grafana Login

Default credentials:

Username: admin
Password: admin123

(If defined inside docker-compose)

📊 Import Dashboards

Open Grafana → Dashboards → Import

Click Upload JSON file

Select a dashboard from:

grafana-dashboards/

Choose Prometheus as data source

Click Import

📈 Application Metrics

The Flask app exposes metrics at:

http://localhost:5000/metrics

Available metrics:

app_requests_total

app_errors_total

To simulate an error:

http://localhost:5000/error

This increments the error counter.

🧠 Prometheus Targets

Visit:

http://localhost:9090/targets

Ensure all are UP:

app

node_exporter

cadvisor

💾 Data Persistence

Docker volumes are configured for:

Grafana

Prometheus

PostgreSQL (if used)

⚠ Do NOT run:

docker compose down -v

This deletes volumes and dashboards.

Use instead:

docker compose down
🔍 Example PromQL Queries
Host CPU
100 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100
Container CPU
sum(rate(container_cpu_usage_seconds_total[5m])) by (container) * 100
Error Rate
rate(app_errors_total[5m])
🎯 Learning Outcomes

This project demonstrates:

Real DevOps monitoring stack

Prometheus metrics instrumentation

PromQL usage

Docker observability

Host-level monitoring

Professional Grafana dashboards

Practical DevOps engineering

🚀 Future Improvements

Alertmanager integration

Slack / Email alerts

Loki log aggregation

Kubernetes deployment

CI/CD integration

Terraform infrastructure provisioning

🏁 Conclusion

This repository simulates a production-style DevOps observability environment and provides a professional monitoring dashboard for:

Host metrics

Container metrics

Application metrics

Built as a hands-on DevOps learning project.