from scapy.all import sniff, ARP
import time

ip_mac_mapping = {}

def handle_arp_packet(packet):
    if packet[ARP].op == 2:
        ip_source=packet[ARP].psrc
        mac_source = packet[ARP].hwsrc
        if ip_source in ip_mac_mapping:
            if mac_source != ip_mac_mapping[ip_source]:
                print(f"Alert Possible Spoofing {ip_source}, nouveau mac {mac_source}, ancien mac {ip_mac_mapping[ip_source]}")
        else:
            ip_mac_mapping[ip_source] = mac_source
            print(f"IP: {ip_source}, mac: {mac_source}")
    

sniff(filter="arp", prn=handle_arp_packet, store=False, count=10)