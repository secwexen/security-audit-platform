def analyze_logs(logfile):
    print(f"\n[+] Analyzing log file: {logfile}\n")

    suspicious_keywords = ["failed", "error", "invalid", "denied"]

    try:
        with open(logfile, "r") as f:
            for line in f:
                if any(keyword in line.lower() for keyword in suspicious_keywords):
                    print(f"[!] Suspicious entry: {line.strip()}")
    except FileNotFoundError:
        print("[ERROR] Log file not found.")

    print("\n[+] Log analysis completed.\n")
