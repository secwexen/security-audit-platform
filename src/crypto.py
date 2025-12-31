import hashlib

def crypto_menu():
    print("\n[+] Cryptography Utilities")
    print("1) Generate SHA256 hash")
    print("2) Generate MD5 hash")

    choice = input("Select option: ")

    if choice == "1":
        text = input("Enter text: ")
        print("SHA256:", hashlib.sha256(text.encode()).hexdigest())

    elif choice == "2":
        text = input("Enter text: ")
        print("MD5:", hashlib.md5(text.encode()).hexdigest())

    else:
        print("Invalid option.")
