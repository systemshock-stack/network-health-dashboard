from flask import Flask, render_template
from dotenv import load_dotenv
import scanner
import os

load_dotenv()

app = Flask(__name__)

@app.route('/')
def dashboard():
    network = os.getenv("NETWORK_PREFIX", "192.168.1")
    
    try:
        devices = scanner.scan_network(network)
        print(f"[DEBUG] Found {len(devices)} devices")
    except Exception as e:
        print(f"[ERROR] Scan failed: {e}")
        devices = []

    demo_mode = False
    if not devices:
        devices = [
            {"ip": f"{network}.1", "status": "up", "delay": "2ms", "hostname": "Router"},
            {"ip": f"{network}.10", "status": "up", "delay": "5ms", "hostname": "Laptop"},
            {"ip": f"{network}.50", "status": "down", "delay": "N/A", "hostname": "Printer"},
            {"ip": f"{network}.100", "status": "up", "delay": "1ms", "hostname": "Phone"},
        ]
        demo_mode = True

    return render_template(
        'index.html',
        devices=devices,
        network=network,
        demo_mode=demo_mode,
        device_count=len(devices)  # ← PASS LEN HERE
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
else:
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)