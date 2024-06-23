#Workshop N°4
 #1. Gestion des tâches de maintenance: Apprendre à utiliser les listes pour gérer une file d'attente de tâches de
 #maintenance dans un data center.
 #Consignes:
 #Demandez à l'utilisateur de saisir des tâches de maintenance prévues pour la journée.
 #Stockez ces tâches dans une liste.
 #Affichez ensuite la liste complète des tâches, puis simulez l'exécution de chaque tâche une par une en les
 #supprimant de la liste après leur "exécution".
# Après chaque suppression, affichez la liste mise à jour des tâches restantes.

taches_maintenance_journee= ""
taches_maintenance = []
taches_maintenance_journee = input("saisissez les taches de maintenence prévus pour la journée")
for taches_maintenance_journee in taches_maintenance:
    taches_maintenance.append(taches_maintenance_journee)

