#demande de la comsomation energetique 
con_ener_moy = input("entrer votre consommation energetique moyenne en kw >> ")

#demande d'heure de fonctionnement dans la journée
heur_fonct_journ = input("entrer combien d'heure le data center a été en fonctionnemnt la journée  >> ")

#calcul consommation
conso_ener_tot = int(con_ener_moy) * int(heur_fonct_journ)
print(str(conso_ener_tot) + " kwh")