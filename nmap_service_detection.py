# Exercice 3 : Scanner les Ports avec Nmap pour Détecter les Versions
# des Services
# Objectif : Utiliser Nmap avec Python pour identifier non seulement les ports
# ouverts, mais aussi les versions des services qui s’exécutent sur ces ports.
# Étape 1 : Préparation du Script Assurez-vous que la bibliothèque
# python-nmap est installée. Si ce n’est pas le cas, installez-la avec pip :
# pip install python-nmap
# Étape 2 : Écriture du Script Créez un fichier Python, nmap_service_detection.py,
# et ajoutez le code suivant :
# import nmap
# def service_version_scan(target):
# nm = nmap.PortScanner()
# nm.scan(target, arguments='-sV') # Utilise `-sV` pour la détection de version
# for host in nm.all_hosts():
# 2
# print(f'Scanning Host: {host}')
# for proto in nm[host].all_protocols():
# lport = nm[host][proto].keys()
# for port in sorted(lport):
# service = nm[host][proto][port]
# print(f'Port : {port}/tcp')
# print(f'Service : {service["name"]}')
# print(f'Product : {service["product"]}')
# print(f'Version : {service["version"]}')
# print(f'Extra Info: {service["extrainfo"]}')
# # Exemple d'utilisation
# service_version_scan('192.168.1.1')
# Exercice : Modifiez le script pour scanner différents types d’appareils ou plages
# d’IP dans votre réseau.
# Étape 3 : Exécution du Script Lancez votre script depuis le terminal pour
# voir quels services et quelles versions sont exposés sur la machine cible.


import nmap

def service_version_scan(targets):
    nm = nmap.PortScanner()

    try:
        # Utilisation de -sV pour la détection de version
        nm.scan(hosts=targets, arguments='-sV')
        
        for host in nm.all_hosts():
            print(f'\nScanning Host: {host}')
            print(f'State: {nm[host].state()}')  # Affiche l'état de l'hôte (up/down)
            
            for proto in nm[host].all_protocols():
                print(f'Protocol: {proto}')
                
                lport = nm[host][proto].keys()
                for port in sorted(lport):
                    service = nm[host][proto][port]
                    print(f'\nPort : {port}/{proto}')
                    print(f'Service : {service["name"]}')
                    print(f'Product : {service.get("product", "N/A")}')
                    print(f'Version : {service.get("version", "N/A")}')
                    print(f'Extra Info: {service.get("extrainfo", "N/A")}')
    except nmap.PortScannerError as e:
        print(f"Error scanning: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Exemple d'utilisation : Scanne une plage d'adresses IP
service_version_scan('192.168.1.1/254')
