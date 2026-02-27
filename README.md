🚀 DevOps Observability Stack — JARVIS War Room








A complete DevOps monitoring and observability platform built using:

🐳 Docker & Docker Compose

📊 Prometheus

📈 Grafana (Professional Dashboards)

🖥 Node Exporter

📦 cAdvisor

🌐 Flask App with Prometheus Metrics

🔔 Telegram Alerting

This project demonstrates real-world monitoring, alerting, and dashboard provisioning for both host systems and Docker containers.

🧠 Architecture Overview
Flask App → Prometheus → Grafana
                ↑
          Node Exporter
                ↑
             cAdvisor
Data Flow

Flask app exposes /metrics

Prometheus scrapes:

App metrics

Host metrics (Node Exporter)

Docker metrics (cAdvisor)

Grafana visualizes everything

Alerts trigger Telegram notifications

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
│   └── other-dashboards.json
│
└── README.md
⚙️ Prerequisites

Docker

Docker Compose

Git

🚀 Setup Instructions
1️⃣ Clone Repository
git clone https://github.com/saifali7243/learndevops.git
cd learndevops
2️⃣ Configure Environment Variables (Secrets Safe)

Create a .env file:

touch .env

Add:

TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here

Add .env to .gitignore:

.env

⚠ Never commit real tokens to GitHub.

3️⃣ Start the Stack
docker compose up --build -d
4️⃣ Verify Services
Service	URL
Flask App	     http://localhost:5000

Prometheus     http://localhost:9090

Grafana	     http://localhost:3000

cAdvisor	     http://localhost:8080

Node Exporter	http://localhost:9100

🔐 Grafana Access
Username: admin
Password: admin

(Change immediately in production.)

📊 Dashboards Included
🖥 Host Monitoring

CPU %

Memory %

Per-core CPU

Disk Usage

Disk I/O

Swap Usage

Load Average

Uptime

Network RX/TX

TCP Connections

File Descriptors

Context Switch Rate

System Temperature

🐳 Docker Monitoring

CPU per container

Memory per container

Container restarts

Running container count

Container health

Container dropdown filter

🌐 Application Monitoring

Total requests

Request rate

Error rate

Total errors

Dashboards auto-provision from:

grafana-dashboards/
🔔 Alerting (Telegram Integration)

Alerts configured for:

Memory > 60% → Warning

Memory > 80% → Critical

Contact points use environment variables:

TELEGRAM_BOT_TOKEN
TELEGRAM_CHAT_ID
📈 Prometheus Targets

Check:

http://localhost:9090/targets

You should see:

app

node_exporter

cadvisor

All must show UP.

🧪 Testing Metrics
App Metrics
http://localhost:5000/metrics
Simulate Traffic
http://localhost:5000/
Simulate Error (if implemented)
http://localhost:5000/error
💾 Data Persistence

Grafana and Prometheus data are stored in Docker volumes.

⚠ Avoid deleting volumes:

docker compose down -v

Use instead:

docker compose down
🛠 Troubleshooting
Grafana Restarting

Check logs:

docker logs grafana --tail 50

Common cause:

Invalid YAML in alert provisioning

Incorrect Telegram contact point name

Prometheus Not Scraping

Check:

docker logs prometheus

Then verify:

http://localhost:9090/targets
Telegram Alerts Not Working

Ensure:

Bot token is valid

Chat ID is correct

Bot has been started with /start

.env is loaded into container

🔍 Useful PromQL Queries
Host CPU
100 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100
Host Memory %
100 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes * 100)
Container CPU %
sum(rate(container_cpu_usage_seconds_total[5m])) by (container) * 100
App Error Rate
rate(app_errors_total[5m])
🛡 Security Practices Implemented

Environment variable secrets

No hardcoded API tokens

Dashboard provisioning via files

Docker volume persistence

Modular provisioning structure

🎯 Future Improvements

Loki log integration

Alertmanager routing

CI/CD deployment pipeline

Kubernetes version

Role-based access control