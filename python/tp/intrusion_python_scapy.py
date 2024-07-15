#from scapy.all import IP,TCP,sr1, Ether, sendp, ARP,srp

#scan des ports
#target_ip = "172.27.192.1"
#ports = [22,80,443]
#for port in ports:
    #packet = IP(dst=target_ip)/TCP(dport=port,flags="S")
    #response = sr1(packet, timeout=1, verbose=0)
    #if response and response.haslayer(TCP) and response[TCP].flags & 0x12:
     #   print(f"port {port} est ouvert sur {target_ip}.")
    #else:
       # print(f"port {port} est fermé sur {target_ip}")

        #simulation de trafic réseau

        #packet = Ether()/IP(dst=target_ip)/TCP(dport=80, flags="S")
        #sendp(packet, looop=1, inter=0.1)

#creation des paquets ARP
# target_ip = "172.27.196.82/20"
# arp = ARP(pdst=target_ip)
# ether = Ether(dst="ff:ff:ff:ff:ff:ff")
# packet = ether/arp
# result = srp(packet, timeout=1, verbose= 1)[0]
# for sent, received in result:
#         print(f"IP {received.psrc}, MAC: {received.hwsrc}")



#exercice_2_scapy
from scapy.all import ARP, Ether, srp

def discover(network) :
    arp_request = ARP(pdst=network)
    ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether_frame / arp_request

    result = srp(packet, timeout = 2, verbose = 1)[0]

    devices = []
    for sent, received in result:
          devices.append({'ip': received.psrc, 'MAC' : received.hwsrc})
    return devices

def main():
      network = '10.125.26.0/24'
      hosts = discover(network=)
      print(hosts)

