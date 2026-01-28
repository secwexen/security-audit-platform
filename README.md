# Security Audit Platform

![License](https://img.shields.io/github/license/secwexen/security-audit-platform)

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

- Cryptography Utilities  
  Hashing and encryption utilities built on well-established Python cryptography libraries. 

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
 ┣ .gitignore            # Files and directories excluded from version control.  
 ┣ CODE_OF_CONDUCT.md   # Guidelines for maintaining a respectful and professional community.  
 ┣ CONTRIBUTING.md      # Instructions and standards for contributing to the project.  
 ┣ LICENSE              # Open-source license
 ┣ README.md            # Documentation
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

### CLI Options

--scan <target>        Run network and port scanning  
--compliance           Run baseline security policy checks  
--logs <path>          Analyze authentication and system logs

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

## Disclaimer

This tool is intended for authorized security testing and educational purposes only.
Unauthorized scanning or testing of systems without explicit permission may be illegal.
The authors assume no liability for misuse.

---

## License

This project is licensed under the **Apache-2.0 License**.  
See the [LICENSE](LICENSE) file for full details.

---

## Author

**Secwexen** – Project Author & Maintainer  
**Role:** Project Manager | Lead Developer   
**GitHub:** [github.com/secwexen](https://github.com/secwexen)  