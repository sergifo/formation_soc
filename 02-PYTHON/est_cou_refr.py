#demande entrer le cout par kw
cout_kw = input("entrer le cout par kw : ")

#demande entrer consommation energetique moyenne par heure
conso_heur = input("entrer consommation energetique par heure : ")

#demande nombre d'heure de fonctionnement
nbr_heur_fonc = input("entrer nombre d'heure de fonctionnemnt par jour : ")

#calcul coût total du refroidissement par jour
cout_total = float(cout_kw) * float(conso_heur) * float(nbr_heur_fonc)

#affichage
print("votre cout total est : " + str(cout_total) + " euros ")