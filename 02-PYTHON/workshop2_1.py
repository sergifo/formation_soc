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
ban_pas_tot = float(input("Entrez la bande passante totale disponible dans le data center (en Gbps) : "))