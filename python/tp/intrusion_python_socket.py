# import socket

# ip = "172.27.192.1"

# ports = [22,80,443]

# for port in ports:
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     result = sock.connect_ex((ip,port))
#     if result == 0:
#         print(f"port est ouvert sur {ip}.")
#     else:
#         print(f"port est fermé sur {ip}.")
#     sock.close()



    
#exercice_1_socket
# import socket
# from ipaddress import ip_address
# from concurrent.futures import ThreadPoolExecutor

# def scan_port(ip, port):
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     result = sock.connect_ex((str(ip),port))
#     if result == 0:
#         print(f"port {port} is open on  {ip}")
#     else:
#          print(f"port {port} is close on  {ip}")
#     sock.close()

# def main():
#     start_ip = ip_address('10.125.26.66')
#     end_ip = ip_address('10.125.26.66')
#     target_ip = start_ip
#     start_port = 80
#     end_port = 443
#     while ThreadPoolExecutor(max_workers=100) as executor
#         while target_ip <= end_ip:
#             for port in range(start_port, end_port + 1):
#                 executor.submit(scan_port, target_ip, port)
#                 #scan_port(target_ip, port)
#             target_ip += 1
#             scan_port(target_ip,port) 
#         target_ip += 1


        