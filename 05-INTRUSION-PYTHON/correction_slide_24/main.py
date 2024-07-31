from scapy.all import IP, TCP, Raw, fragment, send
import base64
import ssl
import socket


def fragmented_packet(dst_ip, dst_port):
    payload = "GET /#/search?q=apple HTTP/1.1\r\nHost: {}\r\n\r\n".format(dst_ip)
    packets = fragment(IP(dst=dst_ip)/TCP(dport=dst_port)/Raw(load=payload))
    for packet in packets:
        send(packet)

def obfuscated_payload(dst_ip, dst_port):
    payload = "GET /#/search?q=apple HTTP/1.1\r\nHost: {}\r\n\r\n".format(dst_ip)
    obfuscated_payload = base64.b64encode(payload.encode()).decode()
    packet = IP(dst=dst_ip)/TCP(dport=dst_port)/Raw(load=obfuscated_payload)
    send(packet)


def encrypted_traffic(dst_ip, dst_port):
    context = ssl.create_default_context()
    with socket.create_connection((dst_ip, dst_port)) as sock:
        with context.wrap_socket(sock, server_hostname=dst_ip) as ssock:
            request = "GET /#/search?q=apple HTTP/1.1\r\nHost: {}\r\n\r\n".format(dst_ip)
            ssock.sendall(request.encode())


def flood_with_requests(dst_ip, dst_port):
    payload = "GET /#/search?q=apple HTTP/1.1\r\nHost: {}\r\nUser-Agent: Mozilla/5.0\r\n\r\n".format(dst_ip)
    for _ in range(1000):
        packet = IP(dst=dst_ip)/TCP(dport=dst_port)/Raw(load=payload)
        send(packet)


fragmented_packet("juiceshop", 3000)
obfuscated_payload("juiceshop", 3000)
encrypted_traffic("juiceshop", 443)
flood_with_requests("juiceshop", 3000)