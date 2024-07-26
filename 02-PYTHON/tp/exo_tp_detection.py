from scapy.all import ARP, Ether, srp

def discover_network(network):

    #creation des paquets ARP
    arp_request = ARP(pdst=network)
    ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether_frame/arp_request

    result = srp(packet, timeout=1, verbose= 1)[0]

    devices = []
    for sent, received in result:
        devices.append(f"IP {received.psrc}, MAC: {received.hwsrc}")
    return devices

def main():
    network = "10.125.26.55/24"
    hosts = discover_network(network)
    print(hosts)

main()




