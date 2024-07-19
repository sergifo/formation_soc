# first_dico = {
#     "nom": "abadi",
#     "prenom": "ihab",
#     "age": 36
# }
# ##afficher une clé
# first_dico["adrresse"] = "tourcoing"

# #supprimer un element
# del first_dico["age"]

# #iterer sur les valeurs
# for element  in first_dico.values():
#     print(element)

# #itere avec cles et valeurs
# for cle, element in first_dico.items():
#     print(f"{cle} => {element}")


    ### exercice dictionnaire

# Avec des variables de type dictionnaire dans une liste, vous réaliserez un logiciel pour stocker une série d'adresses avec : 
# - numéro de voie 
# - complément 
# - intitulé de voie 
# - commune 
# - code postal 
# - Pour ce faire, vous utiliserez des clés de type string qui représenteront les différentes lignes de l'adresse dans le dictionnaire. 
# - Le logiciel devra permettre l'ajout, l'édition, la suppression et la visualisation des données par l'utilisateur.

dico_liste = str(input("veuiller rentrer la liste des informations"))
dico_liste = {
    "numero de voie": "",
    "complement": "",
    "intitulé de voie": "",
    "commune": "",
    "code postal": ""

}

# l'ajout des données utilisateur
for cle, element in dico_liste.append():
    print(element)


# #edition des données utilisateur
# for cle, element in dico_liste.items():
#     print(f"{cle} => {element}")


# #suppression des données utilisateur
# del dico_liste  ["{element}"]


# #visualisation des données utilisateur