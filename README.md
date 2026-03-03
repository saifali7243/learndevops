
````markdown
# 🚀 DevOps Observability Stack — JARVIS War Room

A production-style DevOps observability platform built with **Docker, Prometheus, and Grafana**.

This project demonstrates real-world monitoring of:

- 🖥 Host system metrics  
- 🐳 Docker container metrics  
- 🌐 Application-level metrics  
- 🔔 Automated alerting via Telegram  

Designed as a complete **Infrastructure-as-Code monitoring stack**.

---

# 🧠 Architecture

```mermaid
flowchart LR
    App[Flask App]
    Prom[Prometheus]
    Graf[Grafana]
    Node[Node Exporter]
    Cad[cAdvisor]
    Tele[Telegram Alerts]

    App -->|/metrics| Prom
    Node --> Prom
    Cad --> Prom
    Prom --> Graf
    Graf --> Tele
````

---

# 📊 Metrics Flow

1. Flask app exposes `/metrics`
2. Prometheus scrapes:

   * Application metrics
   * Host metrics (Node Exporter)
   * Container metrics (cAdvisor)
3. Grafana visualizes metrics
4. Alert rules trigger Telegram notifications

---

# 📁 Project Structure

```
learndevops/
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
```

---

# ⚙️ Prerequisites

* Docker
* Docker Compose
* Git

---

# 🚀 Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/saifali7243/learndevops.git
cd learndevops
```

---

## 2️⃣ Configure Secrets (Secure Method)

Create a `.env` file:

```bash
touch .env
```

Add:

```
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

Add `.env` to `.gitignore`:

```
.env
```

⚠ **Never commit API tokens to GitHub.**

---

## 3️⃣ Start the Stack

```bash
docker compose up --build -d
```

---

# 🌐 Access the Services

| Service       | URL                                            |
| ------------- | ---------------------------------------------- |
| Flask App     | [http://localhost:5000](http://localhost:5000) |
| Prometheus    | [http://localhost:9090](http://localhost:9090) |
| Grafana       | [http://localhost:3000](http://localhost:3000) |
| cAdvisor      | [http://localhost:8080](http://localhost:8080) |
| Node Exporter | [http://localhost:9100](http://localhost:9100) |

---

# 🔐 Grafana Login

```
Username: admin
Password: admin
```

(Change credentials in production.)

---

# 📊 Monitoring Coverage

## 🖥 Host System Metrics

* CPU Usage %
* Per-core CPU
* Memory Usage %
* Swap Usage %
* Disk Usage %
* Disk I/O
* Load Average
* Uptime
* Network RX/TX
* TCP Connections
* File Descriptors
* Context Switch Rate
* System Temperature

---

## 🐳 Docker Monitoring

* CPU % per container
* Memory usage per container
* Running container count
* Container restarts
* Container health status
* Container-level filtering

---

## 🌐 Application Monitoring

* Total requests
* Request rate
* Error rate
* Total errors

Metrics endpoint:

```
http://localhost:5000/metrics
```

---

# 🔔 Alerting

Telegram integration configured via environment variables.

Configured alerts:

* Memory > 60% → Warning
* Memory > 80% → Critical

Provisioned via:

```
grafana/provisioning/alerting/
```

---

# 📈 Prometheus Targets

Verify scraping status:

```
http://localhost:9090/targets
```

Expected targets:

* app
* node_exporter
* cadvisor

All should show **UP**.

---

# 🧪 Testing

Generate traffic:

```
http://localhost:5000/
```

Test error metrics (if implemented):

```
http://localhost:5000/error
```

---

# 🔎 Useful PromQL Queries

### Host CPU %

```promql
100 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100
```

### Host Memory %

```promql
100 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes * 100)
```

### Container CPU %

```promql
sum(rate(container_cpu_usage_seconds_total[5m])) by (container) * 100
```

### Application Error Rate

```promql
rate(app_errors_total[5m])
```

---

# 💾 Persistence

Grafana and Prometheus use Docker volumes.

Avoid deleting volumes:

```bash
docker compose down -v
```

Use instead:

```bash
docker compose down
```

---

# 🛠 Troubleshooting

## Grafana Restarting

```bash
docker logs grafana --tail 50
```

Common causes:

* Invalid YAML provisioning
* Incorrect alert contact point
* Misconfigured datasource UID

---

## Prometheus Not Scraping

```bash
docker logs prometheus
```

Then verify:

```
http://localhost:9090/targets
```

---

## Telegram Alerts Not Sending

Ensure:

* Bot token is valid
* Chat ID is correct
* Bot has been started via `/start`
* `.env` file is loaded correctly

---

# 🔒 Security Practices

* Environment-based secrets
* No hardcoded credentials
* Docker volume persistence
* File-based provisioning
* Modular infrastructure layout

---

# 🚀 Future Enhancements

* Loki log aggregation
* Alertmanager integration
* CI/CD pipeline
* Kubernetes deployment
* RBAC configuration


---

