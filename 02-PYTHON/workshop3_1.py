# Workshop N°3
# 1. Surveillance  de  Serveurs:  Vous  devez  vérifier  l'état  de  fonctionnement  de  plusieurs
# serveurs. Pour cet exercice, nous simulerons la vérification de 5 serveurs.
# Consignes:
# Utilisez une boucle pour simuler la vérification de chaque serveur.
# Pour chaque serveur, demandez à l'utilisateur de saisir l'état du serveur (actif/inactif).
# À la fin, affichez le nombre de serveurs actifs et inactifs.
# Utopios® Tous droits réservés 5

numero_serveur = 1
serveurs_actifs = 0
serveurs_inactifs = 0
while numero_serveur <= 5:
    etat_serveur = input(f"Entrez l'état du serveur {numero_serveur} (actif/inactif) : ").lower()
    if etat_serveur == "actif":
        serveurs_actifs += 1
    elif etat_serveur == "inactif":
        serveurs_inactifs += 1
    else:
        print("Entrée non valide, ce serveur sera considéré comme inactif.")
        serveurs_inactifs += 1
    
    numero_serveur += 1




print(f"Le nombre serveur actif {serveurs_actifs} et serveur inactif {serveurs_inactifs}")





    
   



                           




