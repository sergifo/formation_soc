#Workshop N°4
 #3. Atelier sur les Dictionnaires: Inventaire des ressources: Apprendre à utiliser les dictionnaires pour gérer un
 #inventaire des ressources informatiques dans un data center.
 #Consignes:
 #Créez un dictionnaire pour stocker l'inventaire, où les clés sont les types de ressources (ex: serveurs,
 #routeurs, commutateurs) et les valeurs sont le nombre d'unités disponibles.
 #Permettez à l'utilisateur de mettre à jour cet inventaire en ajoutant ou en retirant des unités.
 #Affichez l'inventaire complet à la fin de l'exercice.


#dictionnaire inventaire
inventaire = {
  "serveurs" : 0,
  "routeurs" : 0,
  "commutateurs" : 0  
}

# Boucle pour permettre à l'utilisateur de mettre à jour l'inventaire
while True:
    print("\nOptions disponibles :")
    print("1. Ajouter des unités à l'inventaire")
    print("2. Retirer des unités de l'inventaire")
    print("3. Afficher l'inventaire et quitter")
    choix = input("Entrez votre choix (1/2/3) : ")

    # Traitement en fonction du choix de l'utilisateur
    if choix == '1' or choix == '2':
        type_ressource = input("Entrez le type de ressource (serveurs, routeurs, commutateurs) : ")
        
        if type_ressource in inventaire.keys():
            quantite = int(input("Entrez le nombre d'unités : "))
            
            if choix == '1':
                inventaire[type_ressource] += quantite
                print(f"{quantite} unités ajoutées à {type_ressource}.")
            elif choix == '2':
                inventaire[type_ressource] = max(0, inventaire[type_ressource] - quantite)  # Empêche les valeurs négatives
                print(f"{quantite} unités retirées de {type_ressource}.")
        else:
            print("Type de ressource non reconnu.")
    elif choix == '3':
        print("\nInventaire actuel :")
        for ressource, nombre in inventaire.items():
            print(f"{ressource}: {nombre} unités")
        break
    else:
        print("Choix non valide. Veuillez entrer 1, 2, ou 3.")
