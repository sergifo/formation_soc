import socket

ip = "172.21.191.184"

ports = [22,80,443]

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip, port))
    if result == 0:
        print(f"Port {port} est ouvert sur {ip}.")
    else:
        print(f"Port {port} est fermé sur {ip}.")
    sock.close()