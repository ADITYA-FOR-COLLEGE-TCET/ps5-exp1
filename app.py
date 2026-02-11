from flask import Flask, render_template, jsonify
from prometheus_client import start_http_server, Counter

app = Flask(__name__)

# Define Prometheus Metric
CLICK_COUNT = Counter('app_button_clicks_total', 'Total number of button clicks')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/click', methods=['POST'])
def click():
    # Increment the Prometheus counter
    CLICK_COUNT.inc()
    return jsonify({"status": "success", "message": "Click recorded!"})

if __name__ == '__main__':
    # Start Prometheus metrics server on port 8000 (accessible by K8s/Prometheus)
    start_http_server(8000)
    # Start Flask Web App on port 5000
    app.run(host='0.0.0.0', port=5000)