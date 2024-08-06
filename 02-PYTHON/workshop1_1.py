# Workshop N°1
# 1. Calcul  de  la  consommation  énergétique:  Calculer  la  consommation  énergétique  totale
# d'un data center sur une journée donnée.
# Consignes:
# Demandez  à  l'utilisateur  d'entrer  la  consommation  énergétique  moyenne  (en  kW)  de
# son data center par heure.
# Demandez ensuite combien d'heures le data center a été en fonctionnement durant la
# journée.
# Calculez la consommation énergétique totale de la journée.
# Affichez le résultat en kW.



#demande de la comsomation energetique 
con_ener_moy = float(input("entrer votre consommation energetique moyenne en kw >> "))

#demande d'heure de fonctionnement dans la journée
heur_fonct_journ = float(input("entrer combien d'heure le data center a été en fonctionnemnt la journée  >> "))

#calcul consommation
conso_ener_tot = (con_ener_moy) * (heur_fonct_journ)
#On affiche le calcul
print(str(conso_ener_tot) + " kwh")