from flask import Flask, render_template
from dotenv import load_dotenv
import scanner
import os

# Load .env file (only for local testing)
load_dotenv()

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Get network from .env or use safe default
    network = os.getenv("NETWORK_PREFIX", "192.168.1")
    devices = scanner.scan_network(network)
    return render_template('index.html', devices=devices, network=network)

# Local development
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
# Production (Render.com)
else:
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)