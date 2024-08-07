# Workshop N°63: Filtrage Dynamique de Données
# Consignes:
# Imaginez que vous avez une liste de dictionnaires représentant différents types de ressources dans un data
# center (ex: serveurs, disques de stockage, etc.), où chaque ressource a des attributs comme type, capacité,
# utilisation, etc.
# Écrivez une fonction filtrer_ressources qui utilise *args pour accepter plusieurs critères de filtrage sous
# forme de tuples (attribut, valeur) et **kwargs pour spécifier une condition supplémentaire de filtrage basée
# sur un seuil d'utilisation.
# Utilisez  des  fonctions  lambda  pour  appliquer  le  filtrage  et  retourner  une  nouvelle  liste  de  ressources
# filtrées.
# Utopios® Tous droits réservés 16



from functools import reduce
# def calculer(*args, **kwargs):
#     operation = kwargs.get('operation', 'somme')
#     if operation == 'somme':
#         return sum(args)
#     elif operation == 'moyenne':
#         return sum(args) / len(args) if args else 0
#     elif operation == 'produit':
#         return reduce(lambda x, y: x * y, args, 1)
    

def calculer(*args, **kwargs):
    operation = kwargs.get('operation')
    # if operation == 'somme':
    #     return sum(args)
    # elif operation == 'moyenne':
    #     return sum(args) / len(args) if args else 0
    # elif operation == 'produit':
    #     return reduce(lambda x, y: x * y, args, 1)

    return operation(args)

# Test
print(calculer(1, 2, 3, 4, operation= lambda args: sum(args) / len(args) if args else 0))

print(calculer(1, 2, 3, 4, operation= lambda args: sum(args)))