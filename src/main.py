import argparse
from scanner import run_port_scan
from compliance import run_compliance_checks
from logparser import analyze_logs
from crypto import crypto_menu

def main():
    parser = argparse.ArgumentParser(description="Security Audit Platform")
    parser.add_argument("--scan", help="Run port scan on target host")
    parser.add_argument("--compliance", action="store_true", help="Run compliance checks")
    parser.add_argument("--logs", help="Analyze log file")
    parser.add_argument("--crypto", action="store_true", help="Open cryptography utilities")

    args = parser.parse_args()

    if args.scan:
        run_port_scan(args.scan)

    elif args.compliance:
        run_compliance_checks()

    elif args.logs:
        analyze_logs(args.logs)

    elif args.crypto:
        crypto_menu()

    else:
        print("No valid option provided. Use --help for usage details.")

if __name__ == "__main__":
    main()
