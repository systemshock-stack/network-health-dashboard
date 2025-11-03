import ping3
from concurrent.futures import ThreadPoolExecutor
import socket

def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0].split('.')[0]
    except:
        return "Unknown"

def ping_host(ip):
    try:
        delay = ping3.ping(ip, timeout=1)
        if delay is not False and delay is not None:
            return {
                "ip": ip,
                "status": "up",
                "delay": f"{delay * 1000:.0f}ms",
                "hostname": get_hostname(ip)
            }
        else:
            return {"ip": ip, "status": "down", "delay": "N/A", "hostname": "Unknown"}
    except:
        return {"ip": ip, "status": "error", "delay": "N/A", "hostname": "Unknown"}

def scan_network(network="192.168.1"):
    ips = [f"{network}.{i}" for i in range(1, 255)]
    results = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        for result in executor.map(ping_host, ips):
            if result["status"] == "up":
                results.append(result)
    return sorted(results, key=lambda x: int(x["ip"].split(".")[-1]))