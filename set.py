first_set = set()
first_set.add("element1")
first_set.add(True)
first_set.add(10)
for element in first_set:
    print(element)
    print(id(element))


## exercice
# Via l'utilisation d'une variable de type set contenant des noms de familles, vous devrez réaliser une application permettant à l'utilisateur : 
# - de les stocker 
# - de les afficher 
# - de les éditer 
# - de les supprimer 
# - Pour ce faire, l'utilisateur aura à sa disposition un menu permettant de naviguer entre les différentes fonctionnalités du programme

nom_de_famille = set()
while True:
    print('''
          1.Ajouter nom
          2.Afficher les noms
          3.Supprimer les noms
          4.Editer les noms
          0. Quitter''')
    choix_menu = input("Merci d'indiquer votre choix : ")
    match choix_menu:
        case "1":
            print("=== Ajout d'un nom de famille ===")
            nom_famille = input("Merci de saisir le nom de famille : ")
            set_nom_famille.add(nom_famille)
        case "2":
            print("=== Affichage des noms de famille ===")
            for nom in set_nom_famille:
                print(nom)
        case "3":
            print("=== Suppression d'un nom de famille ===")
            nom_famille = input("Merci de saisir le nom de famille : ")
            set_nom_famille.discard(nom_famille)
        case "4":
            print("=== Edition d'un nom de famille ===")
            nom_famille_a_modifier = input("Merci de saisir le nom de famille à modifier : ")
            nouvelle_valeur_nom_famille = input("Merci de saisir la nouvell valeur : ")
            set_nom_famille.remove(nom_famille_a_modifier)
            set_nom_famille.add(nouvelle_valeur_nom_famille)
        case "0":
            break