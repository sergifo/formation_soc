# Exercice 6 : Détection et Réponse à des Paquets SYN pour Simuler
# un Half-open Scan
# Un autre scénario intéressant serait de simuler une réponse à un scan SYN (util-
# isé parfois pour identifier des ports ouverts sans établir de connexion complète).
# Étape 1 : Script Python pour Simuler une Réponse SYN
# from scapy.all import *
# def handle_syn_packet(packet):
# if packet.haslayer(TCP) and packet[TCP].flags == 'S': # SYN flag
# print(f"Received SYN on port {packet[TCP].dport} from {packet[IP].src}")
# # Créer un paquet SYN-ACK
# syn_ack_pkt = IP(dst=packet[IP].src) / TCP(dport=packet[TCP].sport, sport=packet[TCP].dport, flags='SA', seq=12345, ack=packet[TCP].seq + 1)
# send(syn_ack_pkt, verbose=0)
# print(f"Sent SYN-ACK to {packet[IP].src}")
# # Filtrer les paquets TCP entrants et traiter les paquets SYN
# sniff(filter="tcp", prn=handle_syn_packet)


from scapy.all import TCP, IP, TCP_SYN, sniff, send

def handle_syn_packet(packet):
    # Vérifie si le paquet a une couche TCP et si le flag SYN est défini
    if packet.haslayer(TCP) and packet[TCP].flags & TCP_SYN:
        print(f"Received SYN on port {packet[TCP].dport} from {packet[IP].src}")

        # Créer un paquet SYN-ACK
        syn_ack_pkt = IP(dst=packet[IP].src) / TCP(
            dport=packet[TCP].sport, 
            sport=packet[TCP].dport, 
            flags='SA', 
            seq=12345, 
            ack=packet[TCP].seq + 1
        )
        send(syn_ack_pkt, verbose=0)
        print(f"Sent SYN-ACK to {packet[IP].src}")

# Filtrer les paquets TCP entrants et traiter les paquets SYN
sniff(filter="tcp", prn=handle_syn_packet)

