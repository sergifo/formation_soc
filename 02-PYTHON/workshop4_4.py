#Workshop N°4
 #4. Atelier sur les Ensembles: Surveillance de l'accès réseau: Utiliser les ensembles pour surveiller et gérer les
 #accès uniques au réseau d'un data center.
 #Consignes:
 #Imaginez que chaque accès au réseau est enregistré avec un identifiant unique.
 #Utilisez un ensemble pour stocker ces identifiants au fur et à mesure qu'ils sont enregistrés.
 #Permettez à l'utilisateur de saisir de nouveaux identifiants et vérifiez si l'accès a déjà été enregistré.
 #Affichez le nombre total d'accès uniques à la fin.

# Initialisation de l'ensemble pour stocker les identifiants uniques d'accès au réseau
acces_uniques = set()

# Boucle permettant à l'utilisateur de saisir de nouveaux identifiants
while True:
    identifiant = input("Entrez l'identifiant d'accès au réseau (ou tapez 'fin' pour terminer) : ")
    
    # Vérification de la condition de sortie
    if identifiant.lower() == 'fin':
        break

    # # Vérification si l'identifiant a déjà été enregistré
    # if identifiant in acces_uniques:
    #     print("Cet accès a déjà été enregistré.")
    # else:
    acces_uniques.add(identifiant)
   
    print("Accès enregistré.")

# Affichage du nombre total d'accès uniques
print(acces_uniques)
print(f"\nNombre total d'accès uniques enregistrés : {len(acces_uniques)}")