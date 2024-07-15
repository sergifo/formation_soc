# import nmap


# def host_discovery():
#     nmap_scanner = nmap.PortScanner()
#     network = "10.125.26.0/24"
#     nmap_scanner.scan(hosts=network, arguments='-sn')
#     print("Hosts actifs : ")
#     for host in nmap.all_hosts():
#         if nmap_scanner[host].state() == 'up':
#             print(f"{host} est actif")


# def service_scanner()
    
#Exercice
# Vous  êtes  un  analyste  SOC  pour  une  entreprise  avec  un  réseau
# interne qui contient plusieurs services critiques, y compris un serveur
# web,  un  serveur  de  bases  de  données,  et  des  systèmes  de  gestion
# interne.  Votre  tâche  est  de  scanner  régulièrement  le  réseau  pour
# détecter toute activité suspecte ou non autorisée et d’analyser les
# résultats pour identifier les risques potentiels
# Utopios® Tous droits réservés 14


import nmap

nm = nmap.PortScanner()
response = nm.scan('10.125.26.55', arguments='-p 22-443')
print(response)

# for host in nm.all_hosts():
#     print('Host : %s (%s)' % (host, nm[host].hostname()))
#     print('State : %s' % nm[host].state())
#     for proto in nm[host].all_protocols():
#         print('Protocol : %s' % proto)

#         lport = nm[host][proto].keys()
#         lport.sort()
#         for port in lport:
#             print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

    