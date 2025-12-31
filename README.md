# Security Audit Platform

## Overview

The **Security Audit Platform** is a lightweight yet professional solution designed to perform automated security assessments on servers, applications, and networks. It provides organizations with actionable insights into their security posture through modular checks and clear reporting.  

This project is built with a focus on **simplicity, scalability, and corporate**, making it suitable for both educational use and enterprise environments.

---

## Key Features

- **Automated Port Scanning**  
  Detect open ports and services with configurable scanning ranges.  

- **Policy Compliance Checks**  
  Validate system configurations against common security standards (e.g., firewall rules, SSH policies).  

- **Log Analysis**  
  Parse system logs to identify suspicious activities and potential intrusion attempts.  

- **Cryptography Utilities**  
  Generate and verify hashes, encrypt/decrypt sensitive data with modern algorithms.  

- **Reporting**  
  Export results in structured formats (JSON, HTML, PDF) for corporate documentation and audits.  

---

## Project Structure

```
 security-audit-platform
 ┣ src
 ┃ ┣ main.py            # Entry point
 ┃ ┣ scanner.py         # Network and port scanning
 ┃ ┣ compliance.py      # Policy checks
 ┃ ┣ logparser.py       # Log analysis
 ┃ ┗ crypto.py          # Cryptography utilities
 ┣ tests
 ┃ ┗ unit_tests.py      # Basic unit tests
 ┣ README.md            # Documentation
 ┣ LICENSE              # Open-source license
 ┗ requirements.txt     # Dependencies
```

---

## Installation

```bash
git clone https://github.com/secwexen/security-audit-platform.git
cd security-audit-platform
pip install -r requirements.txt
```

---

## Usage

Run a quick audit on a target system:
```bash
python src/main.py --scan target.com
```

Perform compliance checks:
```bash
python src/main.py --compliance
```

Analyze logs:
```bash
python src/main.py --logs /var/log/auth.log
```

---

## Example Output

```text
[+] Port 22 open - SSH service detected
[+] Firewall active - default deny policy
[!] Suspicious login attempt found in logs
[+] System compliant with baseline security policies
```

---

## Vision

The Security Audit Platform aims to provide a **transparent, modular, and professional framework** for security auditing. It is designed to be extended with new modules, ensuring long-term relevance in evolving cybersecurity landscapes.

---

## License

Released under the **Apache-2.0 License** for open collaboration and corporate adoption.
