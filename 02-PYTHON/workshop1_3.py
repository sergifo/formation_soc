# Workshop N°1
# 3. Simulation  de  panne  de  courant:  Calculer  le  temps  de  fonctionnement  restant  du  data
# center en cas de panne de courant, en utilisant les batteries de secours.
# Consignes:
# Demandez à l'utilisateur d'entrer la capacité totale des batteries de secours (en kWh).
# Demandez ensuite la consommation énergétique moyenne du data center par heure (en kw)
# Calculez combien de temps (en heures) le data center peut continuer à fonctionner en
# utilisant uniquement les batteries de secours.
# Affichez le temps de fonctionnement restant.
# Utopios® Tous droits réservés 30


# Demande à l'utilisateur d'entrer la capacité totale des batteries de secours (en kWh).
cap_tot_bat = float(input("entrer la capacité totale des batteries de secours (en kWh)"))

# Demandez ensuite la consommation énergétique moyenne du data center par heure (en kw)
con_ene_moy = float(input(" quel est la consommation énergétique moyenne du data center par heure (en kw)"))

#calcul du temps de fonctionnement en heure
tem_fon_tot = cap_tot_bat / con_ene_moy
tem_fon_heu = int(tem_fon_tot)

#on affiche le temps de fonctionnement restant
print(f"le temps de fonctionnement restant est {tem_fon_tot} heures")


# #demande d'entrer capacité totale des batteries de secours  en kwh
# cap_bat_sec = input("entrer la capacité totale des batteries de secours")

# #demande consommation energetique moyenne du data center par heure
# conso_ene_moy = input("entrer la consommation energetique moyenne du data center par heure")

# #combien de temps en heure le data center peut continuer à fonctionner
# temps_rest = float(cap_bat_sec) / float(conso_ene_moy)

# print(f"le data center peut fonctionner pendant : {temps_rest:.2f} heures")