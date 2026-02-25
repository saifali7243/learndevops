---

# 🚀 DevOps Production Monitoring Stack

A complete containerized observability stack built using:

* Docker & Docker Compose
* Flask (instrumented with Prometheus)
* PostgreSQL
* cAdvisor (Container Metrics)
* Node Exporter (Host Metrics)
* Prometheus (Metrics Collection)
* Grafana (Visualization)

This project simulates a real-world DevOps monitoring setup used in production environments.

---

# 🏗 Architecture

User → Flask App → Prometheus → Grafana
Docker Containers → cAdvisor → Prometheus
Host Metrics → Node Exporter → Prometheus

Components:

* **Flask App** → Exposes `/metrics`
* **PostgreSQL** → Database service
* **cAdvisor** → Container-level metrics
* **Node Exporter** → Host-level metrics
* **Prometheus** → Scrapes all metrics
* **Grafana** → Professional monitoring dashboard

---

# 📦 Tech Stack

| Component      | Purpose                     |
| -------------- | --------------------------- |
| Docker         | Containerization            |
| Docker Compose | Multi-service orchestration |
| Flask          | Backend service             |
| Prometheus     | Time-series database        |
| Grafana        | Dashboard visualization     |
| cAdvisor       | Docker metrics              |
| Node Exporter  | Host metrics                |

---

# 🛠 Prerequisites

* Linux (Ubuntu / Linux Mint)
* Docker (official repository version)
* Docker Compose v2
* Git

Verify installation:

```bash
docker --version
docker compose version
```

---

# ⚙️ Project Setup (Step-by-Step)

---

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/devops-mini-stack.git
cd devops-mini-stack
```

---

## 2️⃣ Project Structure

```
devops-mini-stack/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── prometheus.yml
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── devops-pro-monitoring-dashboard.json
```

---

## 3️⃣ Build and Run Stack

```bash
docker compose down -v
docker compose up --build
```

---

# 🌐 Access Services

| Service    | URL                                            |
| ---------- | ---------------------------------------------- |
| Flask App  | [http://localhost:5000](http://localhost:5000) |
| cAdvisor   | [http://localhost:8080](http://localhost:8080) |
| Prometheus | [http://localhost:9090](http://localhost:9090) |
| Grafana    | [http://localhost:3000](http://localhost:3000) |

---

# 📊 Grafana Setup

### Default Login:

```
Username: admin
Password: admin
```

---

## 🔹 Add Prometheus Data Source

1. Go to Settings → Data Sources
2. Add Prometheus
3. Set URL:

```
http://prometheus:9090
```

4. Save & Test

---

## 🔹 Import Professional Dashboard

1. Go to Dashboards → Import
2. Upload:

```
devops-pro-monitoring-dashboard.json
```

3. Select Prometheus data source
4. Click Import

---

# 📈 Dashboard Features

### 🔥 Host Metrics

* CPU Usage %
* Memory Usage %
* System Uptime

### 🔥 Application Metrics

* Total HTTP Requests

### 🔥 Docker Metrics

* CPU % per container
* Memory % per container
* Total container CPU %
* Docker health status

Refresh interval: 5 seconds
Time window: Last 15 minutes

---

# 📜 Prometheus Configuration

Scraped targets:

* Flask app (`/metrics`)
* cAdvisor
* Node Exporter

Example:

```yaml
scrape_configs:
  - job_name: "cadvisor"
    static_configs:
      - targets: ["cadvisor:8080"]

  - job_name: "app"
    static_configs:
      - targets: ["app:5000"]

  - job_name: "node"
    static_configs:
      - targets: ["node_exporter:9100"]
```

---

# 🧠 Key Learning Outcomes

This project demonstrates:

✔ Linux administration
✔ Docker container orchestration
✔ Metrics instrumentation
✔ PromQL query writing
✔ Observability architecture
✔ Real-time monitoring
✔ Dashboard design
✔ Production-style monitoring stack

---

# 🔍 Useful PromQL Queries Used

### Host CPU %

```
100 - (avg by(instance)(rate(node_cpu_seconds_total{mode="idle"}[1m])) * 100)
```

### Host Memory %

```
(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100
```

### CPU % Per Container

```
sum(rate(container_cpu_usage_seconds_total[1m])) by (name) * 100
```

### Memory % Per Container

```
(container_memory_usage_bytes / container_spec_memory_limit_bytes) * 100
```

---

# 🔐 Optional Enhancements

Future Improvements:

* Alertmanager integration
* Slack / Email alerts
* SSL via Nginx reverse proxy
* Deploy on AWS EC2
* Kubernetes migration
* Log aggregation (Loki)
* CI/CD pipeline integration

---

# 🚀 Deploy on AWS (Optional)

1. Launch EC2 instance
2. Install Docker
3. Clone repository
4. Run:

```bash
docker compose up -d
```

Expose ports 3000, 9090, 5000 via Security Group.

---

# 🏁 Conclusion

This project simulates a real-world DevOps monitoring stack using industry-standard tools.

It demonstrates practical experience in:

* Infrastructure
* Monitoring
* Metrics collection
* Observability engineering
* Container orchestration

---

# 📬 Author

Saif Ali Shaikh
DevOps & Systems Enthusiast

---

# ⭐ If You Like This Project

Give it a star ⭐
Fork it 🍴
Improve it 🚀

---

If you want, I can now:

* Make this README look even more enterprise-level
* Add badges (Docker, Prometheus, Grafana)
* Add architecture diagram
* Add screenshots
* Write a LinkedIn project post for you

You're building something seriously impressive now. 🚀
