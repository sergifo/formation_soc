from scapy.all import IP, TCP, sr1, Ether, sendp, ARP, srp


# Scan des ports
# target_ip = "172.21.191.184"
# ports = [22,80, 443]
# for port in ports:
#     packet = IP(dst=target_ip)/TCP(dport=port, flags="S")
#     response = sr1(packet, timeout=1, verbose=0)
#     if response and response.haslayer(TCP) and response[TCP].flags & 0x12:
#         print(f"Port {port} est ouvert sur {target_ip}.")
#     else:
#         print(f"Port {port} est fermé sur {target_ip}.")

# Simulation de trafic réseau
# packet = Ether()/IP(dst=target_ip)/TCP(dport=80, flags="S")
# sendp(packet, loop=1, inter=0.1)

# Création des paquets ARP
target_ip = "172.21.191.184/20"
arp = ARP(pdst=target_ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp
result = srp(packet, timeout=1, verbose=1)[0]
print(result)
for sent, received in result:
    print(f"IP {received.psrc}, MAC: {received.hwsrc}")