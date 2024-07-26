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
# nombre_depart2 = int(input("rentrer votre nombre de depart "))
# for i in range(1,11):
#     print(f"{nombre_depart2} X {i} = {nombre_depart2 * i}")


#exo5
#Écrire un programme qui demande à l'utilisateur de saisir 20 nombres. Le programme doit ensuite déterminer et afficher le plus grand de ces nombres.
# plus_grand_nombre_saisi = None

# print("merci de siair 20 nombres")
# for i in range(20):
#     nombre_saisi = float(input(f"nombre{i+1}:"))
#     if plus_grand_nombre_saisi is None or nombre_saisi > plus_grand_nombre_saisi:
#         plus_grand_nombre_saisi = nombre_saisi
# print(f"le plus grand nombre est plus{plus_grand_nombre_saisi}")


#exo7
#Écrire un programme qui demande à l'utilisateur de saisir 20 nombres. Le programme doit ensuite déterminer et afficher le plus grand de ces nombres ainsi que sa position (le numéro d'entrée).
# print("veuillez saisir 20 nombres")
# nombres  = None
# for i in range(20):
#     grand_nombre = max(i)

#exo8
#Écrire un programme qui demande à l'utilisateur de saisir un nombre de départ. Le programme doit ensuite calculer et afficher la factorielle de ce nombre.
nombre_afactoriser = int(input("veuillez saisir un nombreà facoriser :"))
#total = 1

for i in range(1, nombre_afactoriser + 1):
    print(i* nombre_afactoriser + i)

    
#print(total)










#exo9
#Écrire un programme de caisse qui permet à l'utilisateur de saisir le prix de plusieurs articles un par un.
#  Lorsqu'un prix de 0 est saisi, cela signifie la fin des saisies. Le programme doit ensuite afficher le total à payer, demander à 
#l'utilisateur le montant de son paiement, et calculer et afficher la monnaie à rendre, 
# en décomposant cette monnaie en billets de 10 euros, 5 euros, et en pièces de 1 euro.

print("veuiller saisir les prix un par un")
total = 0

while True:
    prix = float(input("veuller saisir les prix un par un"))
    total = total + prix
    if prix == 0:
        break
    print(total)
    print("quel est le montant de votre paiement")
paiement = 0
while paiement:
    monnaie = paiement - total
    print(monnaie)

    
        

