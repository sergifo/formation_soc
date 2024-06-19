#demande d'entrer capacité totale des batteries de secours  en kwh
cap_bat_sec = input("entrer la capacité totale des batteries de secours")

#demande consommation energetique moyenne du data center par heure
conso_ene_moy = input("entrer la consommation energetique moyenne du data center par heure")

#combien de temps en heure le data center peut continuer à fonctionner
temps_rest = float(cap_bat_sec) / float(conso_ene_moy)

print(f"le data center peut fonctionner pendant : {temps_rest:.2f} heures")





