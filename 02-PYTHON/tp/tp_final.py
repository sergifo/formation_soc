# ### Sujet de TP Final Intrusion avec Python

# #### Objectif
# L'objectif de ce TP est de mener une évaluation complète de la sécurité d'une application web anonyme fournie. Les participants devront identifier, exploiter les vulnérabilités trouvées et produire un rapport détaillé de leurs découvertes et recommandations pour la mitigation des risques identifiés.


# #### Instructions Générales
# 1. **Analyse Initiale**:
#    - Effectuer un balayage initial de l'application pour identifier les points d'entrée, les fonctionnalités exposées, et les technologies sous-jacentes utilisées.
#    - Documenter l'architecture de l'application et les flux de données significatifs.

# 2. **Recherche de Vulnérabilités**:
#    - Utiliser des scanners de vulnérabilités automatisés pour détecter les failles potentielles.
  
# 3. **Exploitation des Failles**:
#    - Exploiter les vulnérabilités identifiées de manière contrôlée pour comprendre l'impact et la portée de chaque faille.

# 4. **Automatisation**:
#    - Développer des scripts d'automatisation pour les tests de vulnérabilité répétitifs identifiés durant le TP.
#    - Assurer que chaque script est documenté pour permettre une utilisation future sans connaissance préalable.

# 5. **Rédaction du Rapport**:
#    - Préparer un rapport détaillé incluant :
#      - Une introduction à l'analyse et aux méthodologies utilisées.
#      - Une description des vulnérabilités découvertes, classées par sévérité.
#      - Les détails de l'exploitation et les preuves associées.
#      - Les recommandations pour chaque vulnérabilité exploitée.
# import nmap
# from scapy.all import IP, TCP, Raw, fragment, send
# import base64
# import ssl
# import socket


# print(f"*********(EVALUATION COMPLETE DE LA SECURITE D4UNE APPLICATION WEB)**********")
# print("veuillez rentrer votre choix")
# choix = {
#     1. Analyse initiale 
#     2. Recherche de vulnerabilités
#     3. Exploitation des failles
#     4. Automatisation
#     5. Redaction de rapport
#     netstat -ano

# # }
# def detect_technologies(target):
#     scanner = nmap.PortScanner()
#     scanner.scan(target, arguments='-sV --script banner')  # Utilise le script de bannière pour identifier les technologies
#     for host in scanner.all_hosts():
#         print(f"Host : {host} ({scanner[host].hostname()})")
#         for proto in scanner[host].all_protocols():
#             print(f"Protocol : {proto}")
#             ports = scanner[host][proto].keys()
#             for port in ports:
#                 service = scanner[host][proto][port]
#                 print(f"Port : {port}\tState : {service['state']}\tService : {service['name']}\tVersion : {service.get('version', 'Unknown')}")
#                 if 'script' in service:
#                     print("Technology Details :")
#                     for key, value in service['script'].items():
#                         print(f"  {key} :")
#                         # Afficher chaque ligne du texte de la valeur pour une meilleure lisibilité
#                         if isinstance(value, str):
#                             for line in value.splitlines():
#                                 print(f"    {line}")
#                         else:
#                             print(f"    {value}")

# def host_discovery():
#     nmap_scanner = nmap.PortScanner()
#     network = "10.125.26.0/24"
#     nmap_scanner.scan(hosts=network, arguments='-sn')
#     print("Hosts actifs : ")
#     # for host in nmap_scanner.all_hosts():
#     #     if nmap_scanner[host].state() == 'up':
#     #         print(f"{host} est actif")


import socket
from concurrent.futures import ThreadPoolExecutor

# Fonction pour vérifier un port
def check_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Timeout d'une seconde pour chaque connexion
    try:
        sock.connect((ip, port))
    except (socket.timeout, ConnectionRefusedError):
        return False
    else:
        return True
    finally:
        sock.close()

# Fonction principale pour scanner les ports
def scan_ports(ip, ports):
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        future_to_port = {executor.submit(check_port, ip, port): port for port in ports}
        for future in future_to_port:
            port = future_to_port[future]
            if future.result():
                open_ports.append(port)
    return open_ports

# Adresse IP et plage de ports à scanner
ip_address = '10.125.26.56'  # Remplacez par l'adresse IP que vous voulez scanner
ports_to_scan = range(1, 65536)  # Scanne tous les ports de 1 à 65535

# Exécution du scan
open_ports = scan_ports(ip_address, ports_to_scan)

# Affichage des résultats
if open_ports:
    print(f"Les ports ouverts sur {ip_address} sont :")
    for port in open_ports:
        print(f"Port {port} est ouvert")
else:
    print(f"Aucun port ouvert trouvé sur {ip_address}")
