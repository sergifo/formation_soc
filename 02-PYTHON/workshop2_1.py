# Workshop N°2
# 1. Allocation  de  bande  passante:  Allouer  la  bande  passante  à  différents  services  dans  un
# data center en fonction de leur priorité.
# Consignes:
# Demandez  à  l'utilisateur  d'entrer  la  bande  passante  totale  disponible  dans  le  data
# center (en Gbps).
# Pour  chaque  service  (par  exemple,  Web,  Email,  Base  de  données),  demandez  à
# l'utilisateur d'entrer la priorité du service (sur une échelle de 1 à 3, 1 étant le plus haut).
# Demandez ensuite la demande de bande passante pour chaque service (en Gbps).
# En  fonction  de  la  priorité,  allouez  la  bande  passante  disponible  aux  services,  en
# commençant par le service de priorité 1. Si la bande passante totale est insuffisante,
# répartissez-la proportionnellement en fonction de la priorité.
# Affichez la bande passante allouée à chaque service.
# Utopios® Tous droits réservés 39


# Demande à l'utilisateur  d'entrer  la  bande  passante  totale  disponible  dans  le  data center (en Gbps).
band_pass_tot = float(input("Entrez la bande passante totale disponible dans le data center (en Gbps) : "))
# demande d'entrer la priorité de service
prio_serv = int(input("entrer la priorité de service de 1 plus grand à 3 plus petit"))
#demande de bande passante pour chaque service
dem_band_pass = float(input("entrer la demande de bande passante pour le service concerné"))
allo_even = dem_band_pass if dem_band_pass <= band_pass_tot else band_pass_tot

match prio_serv:
    case 1:
        alloc = allo_even
    case 2:
        alloc = allo_even / 2
    case 3:
        alloc = allo_even / 3
    case _:
        alloc = 0

# Affichage de l'allocation
print(f"Bande passante allouée au service : {alloc:0.2f} Gbps.")
print(f"Bande passante à allouer : {(band_pass_tot - alloc):0.2f} Gbps.")