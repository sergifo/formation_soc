# workshop5_1
#  Gestion des Utilisateurs du Data Center
# Consignes:
# Créez une fonction ajouter_utilisateur qui prend comme arguments le nom de l'utilisateur et son rôle (ex:
# "Administrateur", "Visiteur", "Opérateur") et l'ajoute à un dictionnaire global utilisateurs, où le nom est la
# clé et le rôle est la valeur.
# Écrivez une fonction changer_role qui modifie le rôle d'un utilisateur existant. La fonction doit vérifier si
# l'utilisateur existe avant de changer le rôle.
# Développez une fonction afficher_utilisateurs qui imprime tous les utilisateurs et leurs rôles.
# Utopios® Tous droits réservés 6

# def ajouter_utilisateur(nom_utilisateur, role):
#     utilisateur = {
#         "nom_utilisateur" : nom_utilisateur,
#         "role": role
#     }
# input()






# ajouter_utilisateur("zidane", "numero_10")
# ajouter_utilisateur("adebayor", "numero_4")


# nouveau_utilisateur = [ajouter_utilisateur]
# print(nouveau_utilisateur)

# def changer_role(modifie_role):
#     if nouveau_utilisateur
#     nouveau_role = modifie_role



# def afficher_utilisateurs(nom_utilisateur, role):
    

#solution ihab

# dictionnaire_utilisateurs = {}
# def ajouter_utilisateur(nom_utilisateur: str, role_utilisater: str) -> None:
#     if nom_utilisateur not in dictionnaire_utilisateurs:
#         dictionnaire_utilisateurs[nom_utilisateur] = role_utilisater

# def changer_role(nom_utilisateur: str, nouveau_role_utilisater: str) -> None:
#     if nom_utilisateur in dictionnaire_utilisateurs:
#         dictionnaire_utilisateurs[nom_utilisateur] = nouveau_role_utilisater


# # def affecter_role_utilisateur(nom_utilisateur: str, role_utilisateur: str) -> None:
# #     dictionnaire_utilisateurs[nom_utilisateur] = role_utilisateur

# def afficher_utilisateur():
#     print("======== Liste utilisateurs =========")
#     for nom, role in dictionnaire_utilisateurs.items():
#         print(f"Nom : {nom}, Role : {role}")


# ajouter_utilisateur("toto", "admin")
# afficher_utilisateur()
# ajouter_utilisateur("tata", "dev")
# afficher_utilisateur()
# ajouter_utilisateur("titi", "admin")
# afficher_utilisateur()
# changer_role("titi", "dev")
# afficher_utilisateur()


        





# Workshop N°52. Suivi des Tâches de Maintenance
# Consignes:
# Définissez une liste globale taches_maintenance où chaque élément est un tuple contenant l'ID de la tâche,
# la description, et le statut ("En cours", "Terminé").
# Créez  une  fonction  ajouter_tache  pour  ajouter  une  nouvelle  tâche  à  la  liste,  en  s'assurant  que  l'ID  est
# unique.
# Implémentez une fonction mettre_a_jour_tache qui change le statut d'une tâche basée sur son ID.

# tache_maintenance = []
# tache_trouve = None
# def ajouter_tache(id, description, status):
#     for tache in tache_maintenance :
#         if tache[0] == id:
#             tache_trouve = tache
#             break
#         return tache_trouve
#     if tache_trouve is None:
#         tache_maintenance.append((id,description,status))

# def mettre_a_jout_

# #correction ihab

# taches_maintenance = []


# def rechercher_par_id(id):
#     tache_trouve = None
#     for index, tache in enumerate(taches_maintenance):
#         if tache[0] == id:
#             tache_trouve = (tache, index)
#             break
#     return tache_trouve

# def ajouter_tache(id, description, statut):
#     ### Rechercher une tâche
#     # tache_trouve = None
#     # for tache in taches_maintenance:
#     #     if tache[0] == id:
#     #         tache_trouve = tache
#     #         break
    
#     if rechercher_par_id(id) is None:
#         taches_maintenance.append((id, description, statut))
    

# def mettre_a_jout_tache(id, description, statut):
#     tache_trouve = rechercher_par_id(id)
#     if tache_trouve is not None:
#         taches_maintenance[tache_trouve[1]] = (id, description, statut)


# ajouter_tache(1, "tache 1", "En cours")

# print(rechercher_par_id(1))

# ajouter_tache(2, "tache 2", "En cours")

# print(rechercher_par_id(2))
# mettre_a_jout_tache(1, "tache 1", "Fait")
# print(rechercher_par_id(1))




# workshop N°5
# 3. Analyse des Logs du Système
# Consignes:
# Imaginez que vous avez une liste logs de chaînes de caractères, où chaque entrée représente un message
# log du système avec son niveau de priorité (ex: "ERROR: Échec de connexion", "INFO: Maintenance prévue à
# 23h00").
# Créez une fonction filtrer_logs qui accepte un niveau de priorité et retourne une nouvelle liste contenant
# uniquement les logs de ce niveau.
# Écrivez une fonction compter_logs qui retourne le nombre de logs pour chaque niveau de priorité, en
# utilisant une compréhension de dictionnaire.
# logs_de_chaînes_de_caractères = []
# message = None
# def filtrer_logs():
#     message = str(input("mettez votre niveau de priorité:Échec de connexion ou Maintenance prévue à 23h00 "))
#     print(message)
#     if message == [0]:
#         logs_de_chaînes_de_caractères.append(message)
#         print("Echec de connexion")
#     if message == [1]:
#         logs_de_chaînes_de_caractères.append(message)
#         print("maintenance prevue à 23 h")
    

# nombre_de_log = None
# def compter_logs():
#     for message in logs_de_chaînes_de_caractères:
#         message += 1
#         nombre_de_log = message
#         print(nombre_de_log)



logs = ['Error : Échec de connexion', 'Info : Maintenance prévue à 23h00', 'warning: attention']
def rechercher_par_niveau(niveau):
    logs_niveau = []
    for log in logs:
        if log.startswith(niveau):
            logs_niveau.append(log)

    return logs_niveau

# logs avec erreur
print(rechercher_par_niveau("erreur"))
# logs avec info
print(rechercher_par_niveau("info"))

def compter_logs() :
    nombre_par_log = {}
    for log in nombre_par_log:
        print(log) 
        nombre_par_log[log] += 1
    else:
        nombre_par_log[log] = 1








    
    

    


