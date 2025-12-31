import socket

def run_port_scan(target):
    print(f"\n[+] Starting port scan on: {target}\n")

    common_ports = [22, 80, 443, 3306, 8080]

    for port in common_ports:
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((target, port))
            print(f"[OPEN] Port {port} is open")
            s.close()
        except:
            pass

    print("\n[+] Scan completed.\n")
