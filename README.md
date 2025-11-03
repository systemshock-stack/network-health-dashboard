# Network Health Dashboard

**Live Demo**: [https://network-health-dashboard.onrender.com](https://network-health-dashboard.onrender.com)

A **real-time network scanner** that pings all devices on a local network and displays status in a clean web dashboard.

## Features
- Scans any `/24` network (configurable via `NETWORK_PREFIX`)
- Shows **IP, Hostname, Status, Latency**
- Auto-refreshes every 30s
- Secure: No hard-coded IPs

## Tech Stack
```text
Python │ Flask │ ping3 │ HTML/CSS │ Git │ Render.com
