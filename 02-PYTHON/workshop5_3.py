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