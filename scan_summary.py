def is_private_ip(ip):
    if ip.startswith("192.168") or ip.startswith("10."):
        return True
    else:
        return False
def is_port_risky(port):
    risky_ports = {23, 21, 3389}
    return port in risky_ports
def scan_summary(hosts):
    for host in hosts:
        ip_status = is_private_ip(host["ip"])
        try:
            port_status = is_port_risky(host["port"])
        except KeyError:
            print(f"skipping host {host["ip"]} - missing port data")
            continue
        if ip_status:
            ip_label = "Private"
        else:
            ip_label = "Public"

        if port_status:
            port_label = "Risky"
        else:
            port_label = "Safe"

        print(f"{host["ip"]} ({ip_label}) - Port {host["port"]} ({port_label})")

hosts = [
        {"ip" : "192.168.0.1", "port" : 23},
        {"ip" : "10.0.0.1" },
        {"ip" : "8.8.8.8", "port" : 3389},
        {"ip" : "192.168.0.1" },
        {"ip" : "192.172.0.1", "port" : 26}
    ]

scan_summary(hosts)