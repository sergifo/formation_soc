# Workshop N°23.Allocation de ressources basée sur la disponibilité: Décider de l'allocation des ressources à
# un processus basé sur la disponibilité des ressources en utilisant un opérateur ternaire.
# Consignes:
# Demandez  à  l'utilisateur  le  nombre  total  de  ressources  disponibles  et  le  nombre  de
# ressources demandées par un processus.
# Utilisez un opérateur ternaire pour allouer les ressources si la demande est inférieure
# ou égale à la disponibilité, sinon refusez la demande.
# Affichez le résultat de l'allocation.
# Utopios® Tous droits réservés 41

# Demande à l'utilisateur le nombre total de ressources disponible
ress_dispo = int(input("Entrez le nombre total de ressources disponible : "))

# Demande du nombre de ressources demandées par le processus
ress_dema = int(input("Entrez le nombre de ressources demandées par le processus : "))

# Utilisation de l'opérateur ternaire pour décider de l'allocation
alloc = " Les ressources sont allouées." if ress_dema <= ress_dispo else "les ressources sont refusées"

# Affichage du résultat de l'allocation
print(alloc)
