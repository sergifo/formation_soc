# Workshop N°6_3: Filtrage Dynamique de Données
# Consignes:
# Imaginez que vous avez une liste de dictionnaires représentant différents types de ressources dans un data
# center (ex: serveurs, disques de stockage, etc.), où chaque ressource a des attributs comme type, capacité,
# utilisation, etc.
# Écrivez une fonction filtrer_ressources qui utilise *args pour accepter plusieurs critères de filtrage sous
# forme de tuples (attribut, valeur) et **kwargs pour spécifier une condition supplémentaire de filtrage basée
# sur un seuil d'utilisation.
# Utilisez  des  fonctions  lambda  pour  appliquer  le  filtrage  et  retourner  une  nouvelle  liste  de  ressources
# filtrées


def filtrer_ressources(ressources, *critere_filtrage, **kwargs):
    seuil = kwargs.get('seuil_utilisation')
    resultats = [res for res in ressources if all(res[crit[0]] == crit[1] for crit in critere_filtrage)]
    if seuil:
        resultats = [res for res in resultats if res['utilisation'] < seuil]
    return resultats

# Test
ressources = [
    {"type": "serveur", "capacité": "32GB", "utilisation": 60},
    {"type": "serveur", "capacité": "320GB", "utilisation": 60},
    {"type": "stockage", "capacité": "1TB", "utilisation": 80},
]
print(filtrer_ressources(ressources, ("type", "serveur"),("capacité", "32GB"), seuil_utilisation=70))