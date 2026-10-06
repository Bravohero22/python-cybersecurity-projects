

allowed_port = [22, 80,443]
connection_attempt = [
    {"ip" : "192.168.1.1", "port" : 23},
    {"ip" : "192.168.1.2", "port" : 80},
    {"ip" : "192.168.1.3", "port" : 443},
    {"ip" : "192.168.1.4", "port" : 8080},
    {"ip" : "192.168.1.5", "port" : 22}
]

allowed_count = 0
blocked_count = 0
blocked_ips = set()

for attempt in connection_attempt:
    if attempt["port"] in allowed_port:
        print(f"{attempt["ip"]} -> port {attempt["port"]} : ALLOWED")
        allowed_count +=1
    else:
        print(f"{attempt["ip"]} -> port {attempt["port"]} : BLOCKED")
        blocked_count +=1
        blocked_ips.add(attempt["ip"])
        pass

print(f"Total attempts: {len(connection_attempt)}  ")
print(f"Allowed: {allowed_count}")
print(f"Blocked: {blocked_count}")
print(f"Blocked percentage: {blocked_count/len(connection_attempt):.0%}")
print(blocked_ips)
