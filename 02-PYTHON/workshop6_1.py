# Workshop N°6_1. Tri Personnalisé de Serveurs
# Consignes:
# Vous avez une liste de tuples représentant des serveurs, où chaque tuple contient le nom du serveur et son
# utilisation du CPU en pourcentage (ex: [("Serveur1", 70), ("Serveur2", 20), ...]).
# Écrivez une fonction trier_serveurs qui accepte la liste des serveurs et un argument nommé cle_tri utilisant
# **kwargs. Cette clé de tri doit permettre de trier soit par nom, soit par utilisation CPU.
# Utilisez une fonction lambda à l'intérieur de trier_serveurs pour effectuer le tri en fonction de la cle_tri
# spécifiée

serveurs = [("serveur1", 80), ("serveur3", 50), ("serveur2", 10)]

def trier_serveur(serveurs, **kwargs):
    #cle_tri = kwargs["cle_tri"] if kwargs["cle_tri"] else "nom"
    cle_tri = kwargs.get("cle_tri", "nom") # dans le cadre ou la cle_tri n'existe pas la valeur par defaut serait nom
    index_tri = 0 if cle_tri == 'nom' else 1
    return sorted(serveurs, key=lambda serveur : serveur[index_tri])


print(trier_serveur(serveurs, cle_tri="cpu"))
print(trier_serveur(serveurs, cle_tri="nom"))

