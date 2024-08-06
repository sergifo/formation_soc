# Workshop N°1
# 2. Estimation  des  coûts  de  refroidissement:  Estimer  le  coût  quotidien  du  refroidissement
# nécessaire pour maintenir le data center à une température optimale.
# Consignes:
# Demandez à l'utilisateur d'entrer le coût par kWh (kilowatt-heure).
# Demandez à l'utilisateur d'entrer la consommation énergétique moyenne du système de
# refroidissement par heure.
# Demandez le nombre d'heures de fonctionnement du système de refroidissement dans
# la journée.
# Calculez le coût total du refroidissement pour la journée.
# Affichez le coût total.
# Utopios® Tous droits réservés 29



#demande entrer le cout par kw
cout_kw = float(input("entrer le cout par kw : "))

#demande entrer consommation energetique moyenne par heure
conso_heur = float(input("entrer consommation energetique par heure : "))

#demande nombre d'heure de fonctionnement
nbr_heur_fonc = float(input("entrer nombre d'heure de fonctionnemnt par jour : "))

#calcul coût total du refroidissement ppor la journée
cout_total = cout_kw * conso_heur * nbr_heur_fonc

#affichage
print("votre cout total est : " + str(cout_total) + " euros ")