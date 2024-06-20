# for incr in range(10):
#   print("toto :", incr)

# notes = "fofo"
# # for note in range(10):
# #     print(notes)


# listes = [0,12,30,20]
# for liste in range()
#     print(liste)


#i dans la plage de 0 à 101 avec des pas de 5
# for i in range(0,101,5):
#     print("i vaut :", i)


# for a in range(11):
#     print(f"la puissance de {a} est {a**2}")

# for i in range(11):
#     if(i==5):
#         continue
#     print(i)
#     if(i == 7):
#         break


# for i in range(10):
#     for y in range(3):
#         print(i,y)


#boucle while
# i = 0
# while(i < 10):
#     print("i vaut", i)
#     i+= 1


# for i in range(10):
#     print("i vaut",i)
# else:
#     print("ce que je veux afficher dans la console sinon")


#exo1
# Écrire un programme qui demande à l'utilisateur de saisir un nombre compris entre 10 et 20. Tant que le nombre saisi n'est pas dans cet intervalle, 
# le programme doit continuer à demander un nombre et indiquer si le nombre saisi est trop grand ou trop petit. Lorsque l'utilisateur saisit un nombre correct, le programme se termine.

# nombre = int(input("entrer un nombre entre 10 et 20\n ")) 
# while (10 < nombre < 20):
#     print("le programme est terminé")
#     break
# if nombre < 10 :
#     print("le nombre est trop petit")
# else:
    
#     print("le nombre est trop grand")

#exo2
#Ecrire un programme qui demande à l'utilisateur de saisir un nombre de départ. Le programme doit ensuite afficher les 10 nombres suivants ce nombre de départ.

# nombre_depart = int(input("rentrer votre nombre de depart\n"))
# for i in range(1,11):
#     print(nombre_depart + i)

#exo3
#Écrire un programme qui demande à l'utilisateur de saisir un nombre de départ. Le programme doit ensuite afficher les 10 nombres suivants à partir de ce nombre de départ.
# nombre_depart1 = int(input("rentrer votre nombre de depart"))
# for i in range(nombre_depart1+ 1, nombre_depart1 + 11):
#     print(i)

#exo4
# Écrire un programme qui demande à l'utilisateur de saisir un nombre de départ. Le programme doit ensuite afficher la table de multiplication de ce nombre pour les nombres de 1 à 10.
# Donnez-moi le nombre de départ ? 5
# Table de multiplication 5
# 5 X 1 = 5
# 5 X 2 = 10
# 5 X 3 = 15
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35
# 5 X 8 = 40
# 5 X 9 = 45
# 5 X 10 = 50
nombre_depart2 = int(input("rentrer votre nombre de depart "))
for i in range(1,11):
    print(f"{nombre_depart2} X {i} = {nombre_depart2 * i}")






    
        

