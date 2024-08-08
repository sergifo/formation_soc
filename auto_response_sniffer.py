# Exercice 5 : Réponse Automatisée à des Événements Réseau avec
# Scapy
# Objectif : Utiliser Scapy pour surveiller le trafic réseau spécifique et répondre
# automatiquement à des conditions pré-définies, comme répondre à des pings ou
# à des requêtes spécifiques.
# Étape 1 : Installation de Scapy Si Scapy n’est pas déjà installé, installez-le
# avec pip :
# pip install scapy
# Étape 2 : Écriture du Script Créez un fichier Python, auto_response_sniffer.py,
# pour surveiller et répondre automatiquement au trafic ICMP (ping requests).
# Le script interceptera les paquets ICMP et enverra une réponse personnalisée.
# from scapy.all import *
# import time
# def auto_respond(packet):
# if packet.haslayer(ICMP):
# if packet[ICMP].type == 8: # Echo request
# print(f"Received ICMP request from {packet[IP].src}")
# # Préparer une réponse ICMP
# icmp_reply = IP(dst=packet[IP].src) / ICMP(type=0, id=packet[ICMP].id, seq=packet[ICMP].seq) / packet[Raw].load
# send(icmp_reply, verbose=0)
# print(f"Sent ICMP reply to {packet[IP].src}")
# # Sniffer qui filtre les paquets ICMP et utilise la fonction auto_respond pour chaque paquet
# sniff(filter='icmp', prn=auto_respond)
# Étape 3 : Fonctionnement du Script
# 1. Interception de paquets ICMP : Le script écoute tous les paquets
# ICMP (utilisés notamment pour les commandes ping).
# 2. Réponse aux requêtes ICMP : Lorsqu’un paquet ICMP de type “echo
# request” (ping request) est détecté, le script génère une réponse “echo
# reply” (ping reply) et l’envoie au demandeur.


from scapy.all import ICMP, IP, Raw, send, sniff

def auto_respond(packet):
    if packet.haslayer(ICMP):
        if packet[ICMP].type == 8:  # Echo request (ping request)
            print(f"Received ICMP request from {packet[IP].src}")

            # Préparer une réponse ICMP
            icmp_reply = IP(dst=packet[IP].src) / ICMP(type=0, id=packet[ICMP].id, seq=packet[ICMP].seq)

            # Ajouter la charge utile si elle est présente
            if packet.haslayer(Raw):
                icmp_reply = icmp_reply / packet[Raw].load
            
            # Envoyer la réponse ICMP
            send(icmp_reply, verbose=0)
            print(f"Sent ICMP reply to {packet[IP].src}")

# Sniffer qui filtre les paquets ICMP et utilise la fonction auto_respond pour chaque paquet
sniff(filter='icmp', prn=auto_respond)


