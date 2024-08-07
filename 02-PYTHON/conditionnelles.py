mon_age = int(input("quel age avez vous"))

if mon_age >= 21:
    print("vous etes majeur aux usa")
elif mon_age >= 18:
    print("vous etes majeur en france")
else:
    print("vous etes mineur")



  # utilisation match case
jour = int(input("donner un numero du jour de la semaine :")) 
match jour: 
    case 1:
        print("lundi")
    case 2:
         print("mardi")
    case 3:
        print("mercredi")
    case 4:
        print("jeudi")
    case 5:
        print("vendredi")
    case 6:
        print("samedi")
    case 7:
        print("dimanche")
    case _:
        print("rentrer un numero entre 1 et 7")