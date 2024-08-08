# Exercice 4 : Écoute et Filtrage de Paquets avec Scapy
# Objectif : Utiliser Scapy pour capturer et filtrer les paquets ICMP, qui sont
# souvent utilisés pour le ping.
# Étape 1 : Installation de Scapy Si Scapy n’est pas déjà installé :
# pip install scapy
# Étape 2 : Écriture du Script Créez un fichier Python, icmp_filter_sniffer.py,
# et ajoutez le code suivant :
# from scapy.all import sniff, ICMP
# def icmp_packet_callback(packet):
# if ICMP in packet:
# print(f"ICMP Packet: {packet.summary()}")
# # Filtrer pour écouter uniquement les paquets ICMP
# sniff(filter='icmp', prn=icmp_packet_callback, count=10)
# Exercice : Adaptez le script pour écouter d’autres types de paquets, comme
# ceux utilisés pour les protocoles TCP ou UDP spécifiques.
# Étape 3 : Exécution du Script Exécutez le script dans un terminal, idéale-
# ment avec des droits administrateur pour permettre à Scapy d’intercepter les
# paquets :
# 3
# sudo python icmp_filter_sniffer.py


from scapy.all import sniff, IP, ICMP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        print(f"\nIP Source: {ip_src} --> IP Destination: {ip_dst}")
        
        if TCP in packet:
            tcp_sport = packet[TCP].sport
            tcp_dport = packet[TCP].dport
            print(f"TCP Packet: Source Port: {tcp_sport}, Destination Port: {tcp_dport}")
        
        elif UDP in packet:
            udp_sport = packet[UDP].sport
            udp_dport = packet[UDP].dport
            print(f"UDP Packet: Source Port: {udp_sport}, Destination Port: {udp_dport}")
        
        elif ICMP in packet:
            icmp_type = packet[ICMP].type
            icmp_code = packet[ICMP].code
            print(f"ICMP Packet: Type: {icmp_type}, Code: {icmp_code}")

# Capture ICMP, TCP, and UDP packets
sniff(filter='icmp or tcp or udp', prn=packet_callback, count=10)
