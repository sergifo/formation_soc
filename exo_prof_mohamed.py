# #exo1
# # Ecrire un programme qui prend en entrée une température temp et 
# # qui renvoie l'état de l'eau à cette température c'est à dire "SOLIDE", 
# # "LIQUIDE" ou "GAZEUX".

# # - On prendra comme conditions les suivantes :
# # - Si la température est strictement négative alors l'eau est à l'état solide.
# # - Si la température est entre 0 et 100 (compris) l'eau est à l'état liquide.
# # - Si la température est strictement supérieure à 100 l'eau est à l'état gazeux
# # - Il est possible de réaliser cet exercice sans if imbriqués grâce au elif


# # demande d'entrer la temperature de l'eau
# temperature = int(input("quel est la temperature de l'eau"))
# if temperature < 0 :
#    print("l'eau est solide")
# elif 0 < temperature < 100 :
#    print("l'eau est liquide")
# else:
#    print("l'eau est gazeux")

# #exo 
# #     Écrire un programme qui permet de tester si un profil est valable pour 
# # une candidature ou non selon ces trois critères :
# # - L’âge minimum pour le poste est 30 ans
# # - Le salaire maximum possible est 40 000 euros
# # - Le nombre d’années d’expérience minimum est de 5 ans.
# # - On affichera différents messages pour chaque condition non 
# # respectée.
# # - Il est possible de réaliser cet exercice avec une seule structure 
# # conditionnelle ne comportant qu’une condition par clause (pas de 
# # and/or)

# age = 30
# salaire = 40000
# annee = 5
# age = int(input("entrer votre age"))
# if age > 30 :
#     print("l'age minimum pour le poste est 30 ans")
# salaire = int(input("entrer votre salaire"))
# if salaire > 40000 :
#     print("le salaire minimum est 40000")
# annee = int(input("entrer votre année d'experience"))
# if annee < 5:
#     print("l'année d'experience minimum est 5 ans")


# #exo3
# # Écrire un programme qui demande à l'utilisateur de saisir un nombre entier. Le programme doit vérifier si ce nombre est divisible par 3 et afficher un message approprié.

# entier = int(input("entrer un nombre entier"))
# if entier % 3 == 0 :
#     print("le nombre est divisible par 3")


#exo4
#     Écrire un programme qui demande à l'utilisateur de saisir le nombre de photocopies effectuées. Le programme doit calculer et afficher le prix à payer en fonction du nombre de photocopies, selon les règles suivantes :
# - Moins de 10 copies : 0,15 euro par copie
# - Entre 10 et 19 copies : 0,10 euro par copie
# - 20 copies et plus : 0,05 euro par copie

photocopie = int(input("entre le nombre de photocopie effectué"))
prix = 0.0
if photocopie < 10 :
    prix = photocopie * 0.15
elif  10 < photocopie < 19 :
    prix = photocopie * 0.10
else :
    prix = photocopie * 0.05
 
print("vous devez payez " + str(prix) + "euros")