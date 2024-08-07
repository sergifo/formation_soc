# Workshop N°5_2. Suivi des Tâches de Maintenance
# Consignes:
# Définissez une liste globale taches_maintenance où chaque élément est un tuple contenant l'ID de la tâche,
# la description, et le statut ("En cours", "Terminé").
# Créez  une  fonction  ajouter_tache  pour  ajouter  une  nouvelle  tâche  à  la  liste,  en  s'assurant  que  l'ID  est
# unique.
# Implémentez une fonction mettre_a_jour_tache qui change le statut d'une tâche basée sur son ID.

tache_maintenance = []
def ajouter_tache(id_tache, description):
    tache_existante = False
    # if len([tache for tache in tache_existante if tache[0] == id_tache]) == 0:
    #     taches_maintenance.append((id_tache, description, "En cours"))
    
    if not any(tache[0] == id_tache for tache in tache_existante):
        tache_maintenance.append((id_tache, description, "En cours"))
    else:
        print("Une tâche avec cet ID existe déjà.")






def mettre_a_jour_tache(id_tache, statut):
    tache_trouvee = False
    for index, tache in  enumerate(tache_maintenance):
        if  tache[0] == id_tache:
            taches_maintenance[index] = (tache[0], tache[1], statut)
            tache_trouvee = True
            print(f"Statut de la tâche {id_tache} mis à jour.")
            break
    
    if not tache_trouvee:
        print("Tâche non trouvée.")



def mettre_a_jour_tache(id_tache, statut):
    tache_trouvee = False
    for index, tache in  enumerate(tache_maintenance):
        if  tache[0] == id_tache:
            tache_maintenance[index] = (tache[0], tache[1], statut)
            tache_trouvee = True
            print(f"Statut de la tâche {id_tache} mis à jour.")
            break
    
    if not tache_trouvee:
        print("Tâche non trouvée.")


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
