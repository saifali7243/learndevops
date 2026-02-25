import psutil
from flask import Flask, render_template, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter('app_requests_total', 'Total App HTTP Requests')
ERROR_COUNT = Counter('app_errors_total', 'Total App Errors')

@app.route("/")
def dashboard():
    REQUEST_COUNT.inc()
    return render_template("index.html")

@app.route("/stats")
def stats():
    data = {
        "cpu": psutil.cpu_percent(),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent
    }
    return jsonify(data)

@app.route("/error")
def error():
    ERROR_COUNT.inc()
    return "Error simulated", 500

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
