#Workshop N°3
 #1. Surveillance de Serveurs: Vous devez vérifier l'état de fonctionnement de plusieurs
 #serveurs. Pour cet exercice, nous simulerons la vérification de 5 serveurs.
 #Consignes:
 #Utilisez une boucle pour simuler la vérification de chaque serveur.
 #Pour chaque serveur, demandez à l'utilisateur de saisir l'état du serveur (actif/inactif).
 #À la fin, affichez le nombre de serveurs actifs et inactifs.

serveurs_actif = 0
serveurs_inactif = 0
for i in range(1, 6):
    while True:
        etat_serveur = print("veuillez saisir l'etat du serveur; actif ou inactif")
        if etat_serveur == "actif":
            serveurs_actif = serveurs_actif + 1
            break
        elif etat_serveur == "inactif":
            serveurs_actif == serveurs_inactif + 1
            break
        else:
            print("veuillez saisir actif ou inactif")
print(f"nombres de serveurs actifs {serveurs_inactif} nombres serveurs inactif {serveurs_inactif}")



                           




