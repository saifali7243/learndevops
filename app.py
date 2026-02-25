import psutil
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h2>Server Health Dashboard</h2>
    CPU Usage: {psutil.cpu_percent()}% <br>
    RAM Usage: {psutil.virtual_memory().percent}% <br>
    Disk Usage: {psutil.disk_usage('/').percent}% <br>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
