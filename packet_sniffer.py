# Exercice 2 : Analyse de Paquets avec Scapy
# Objectif : Utiliser Scapy pour capturer et analyser les paquets réseau.
# Étape 1 : Installation de Scapy Installez Scapy via pip :
# pip install scapy
# 1
# Étape 2 : Écriture du Script d’Analyse de Paquets Créez un fichier
# Python, nommé packet_sniffer.py, et ajoutez le code suivant :
# from scapy.all import sniff, IP, TCP
# def packet_callback(packet):
# if IP in packet:
# ip_src = packet[IP].src
# ip_dst = packet[IP].dst
# print(f"IP Source: {ip_src} --> IP Destination: {ip_dst}")
# if TCP in packet:
# tcp_sport = packet[TCP].sport
# tcp_dport = packet[TCP].dport
# print(f"TCP Source Port: {tcp_sport} --> TCP Destination Port: {tcp_dport}")
# # Sniff continuously for 10 packets.
# sniff(prn=packet_callback, count=10)
# Exercice : Modifiez le script pour filtrer différents types de trafic, comme ICMP
# ou UDP. Essayez d’ajouter des conditions pour capturer des paquets spécifiques
# basés sur des critères comme des adresses IP ou des numéros de port.
# Étape 3 : Exécution du Script Lancez le script depuis votre terminal (peut
# nécessiter des privilèges administrateur) :
# sudo python packet_sniffer.py




from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    # Vérifiez si le paquet contient une couche IP
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst

        # Vérifiez si le paquet contient une couche TCP
        if TCP in packet:
            tcp_sport = packet[TCP].sport
            tcp_dport = packet[TCP].dport
            # Filtrez les paquets TCP sur le port 80
            if tcp_dport == 80:
                print(f"TCP Packet: IP Source: {ip_src} --> IP Destination: {ip_dst}")
                print(f"TCP Source Port: {tcp_sport} --> TCP Destination Port: {tcp_dport}")

        # Vérifiez si le paquet contient une couche UDP
        elif UDP in packet:
            udp_sport = packet[UDP].sport
            udp_dport = packet[UDP].dport
            # Filtrez les paquets UDP sur le port 53
            if udp_dport == 53:
                print(f"UDP Packet: IP Source: {ip_src} --> IP Destination: {ip_dst}")
                print(f"UDP Source Port: {udp_sport} --> UDP Destination Port: {udp_dport}")

        # Vérifiez si le paquet contient une couche ICMP
        elif ICMP in packet:
            print(f"ICMP Packet: IP Source: {ip_src} --> IP Destination: {ip_dst}")

# Sniff continuellement avec un filtre BPF
# 'icmp or udp port 53 or tcp port 80' capture les paquets ICMP et les paquets UDP destinés au port 53, et les paquets TCP destinés au port 80
sniff(prn=packet_callback, filter="icmp or udp port 53 or tcp port 80", count=10)

