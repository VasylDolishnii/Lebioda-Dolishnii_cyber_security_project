import socket
from colorama import Fore, Style, init

# Initialize colorama
init()

# Target IP
target = input("Enter target IP: ")

# Ports to scan
ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 8080]

print(f"\nScanning target: {target}")
print("-" * 50)

for port in ports:
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    result = scanner.connect_ex((target, port))

    if result == 0:
        print(f"{Fore.GREEN}[OPEN]{Style.RESET_ALL} Port {port}")
    else:
        print(f"{Fore.RED}[CLOSED]{Style.RESET_ALL} Port {port}")

    scanner.close()

print("\nScan completed.")
