import os

def run_compliance_checks():
    print("\n[+] Running compliance checks...\n")

    checks = {
        "Firewall active": "ufw status | grep -i active",
        "SSH root login disabled": "grep -i 'PermitRootLogin no' /etc/ssh/sshd_config",
        "Password authentication disabled": "grep -i 'PasswordAuthentication no' /etc/ssh/sshd_config"
    }

    for description, command in checks.items():
        result = os.system(f"{command} > /dev/null 2>&1")
        status = "PASS" if result == 0 else "FAIL"
        print(f"{description}: {status}")

    print("\n[+] Compliance checks completed.\n")
