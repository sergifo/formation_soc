#### Analyse détaillée des logs de sécurité

# Améliorer la capacité à extraire, analyser, et rapporter des données depuis des fichiers log de manière automatisée.


# 1. **Lecture et analyse des logs:**
#    - Écrivez un script Python qui lit un fichier de logs. Chaque entrée de log contient la date, l'heure, l'utilisateur, l'adresse IP source, l'action (par exemple, "login_attempt"), et le résultat ("SUCCESS" ou "FAILURE").
#    - Exemple de log: `"2023-06-25 14:22:01, john_doe, 192.168.1.1, login_attempt, FAILED"`

# 2. **Filtrage des données:**
#    - Extraites les tentatives de connexion échouées et identifiez les adresses IP qui ont des tentatives échouées répétées.
#    - Générez un rapport qui liste ces adresses IP avec le nombre de tentatives échouées et la première et dernière tentative notée.

# 3. **Visualisation:**
#    - Utilisez une bibliothèque comme `matplotlib` pour visualiser le nombre de tentatives de connexion échouées par adresse IP sur un histogramme.

# 4. **Alerte:**
#    - Si une adresse IP dépasse un certain seuil de tentatives échouées, générer une alerte formatée prête à être envoyée à une équipe de réponse aux incidents.



#1. lecture et analyse des logs
import matplotlib
import pandas as file_reader
choix_menu = input("""
1. Lecture et analyse des logs
2. Filtrage des données
3. Visualisation
4. Alerte

Choisissez une option (1-4) : """)

match choix_menu:
    case 1:
        # Définir le chemin vers votre fichier de logs
        df =  file_reader.read_fwf('bureau/formation_soc/python/tp')  
        print(df)

    case 2:
        # Liste pour stocker les tentatives de connexion échouées
        log_file = "bureau/formation_soc/python/tp"
        tentatives_echouees = []
        # Dictionnaire pour compter les occurrences des adresses IP
        compteur_ips = {}
         # Ouvrir le fichier en mode lecture
        with open(log_file, 'r') as f:
            # Lire chaque ligne du fichier
            for ligne in f:
                # Vérifier si la ligne contient 'FAILED'
                if 'FAILED' in ligne:
            # Mettre à jour le compteur d'occurrences des adresses IP
            if adresse_ip in compteur_ips:
                compteur_ips[adresse_ip] += 1
            else:
                compteur_ips[adresse_ip] = 1

# Afficher les tentatives de connexion échouées
print("Tentatives de connexion échouées :")
for tentative in tentatives_echouees:
    print(f"Date/Heure: {tentative['Date/Heure']}, Utilisateur: {tentative['Utilisateur']}, Adresse IP: {tentative['Adresse IP']}, Action: {tentative['Action']}, Statut: {tentative['Statut']}")

# Afficher les adresses IP avec tentatives échouées répétées
print("\nAdresses IP avec tentatives échouées répétées :")
for ip, count in compteur_ips.items():
    if count > 1:
        print(f"Adresse IP: {ip}, Nombre de tentatives échouées: {count}")
        case 3:
       
    


    










#### Détection de configurations anormales

# Utiliser Python pour analyser des configurations de système ou d'application et détecter des anomalies.

# **Description et étapes:**

# 1. **Lecture de la configuration:**
#    - Créez un script pour lire un fichier de configuration simulé qui contient des paramètres tels que les ports ouverts, les services en cours d'exécution, et les niveaux d'accès.
#    - Exemple de contenu: `port: 22, service: ssh, status: active`

# 2. **Détection d'anomalies:**
#    - Écrivez une fonction pour identifier et signaler toute configuration qui ne respecte pas une politique de sécurité standard (par exemple, un port non standard ouvert ou un service inattendu en cours d'exécution).

# 3. **Rapport:**
#    - Produisez un rapport des anomalies détectées avec des recommandations pour chaque anomalie identifiée.

open












#### Création d'un petit système de détection d'intrusion

# Simuler la détection d'activités suspectes en temps réel.


# 1. **Surveillance en temps réel:**
#    - Implémentez un système basique qui surveille en continu un flux de données ou un fichier log pour des signatures d'activités suspectes (comme des chaînes de requêtes SQL pour injection SQL).

# 2. **Détection et alerte:**
#    - Utilisez des expressions régulières pour détecter les activités suspectes. Lorsqu'une activité suspecte est détectée, le système doit enregistrer l'événement et générer une alerte.

# 3. **Automatisation:**
#    - Assurez-vous que le système peut fonctionner de manière autonome et envoyer des alertes sans intervention manuelle, potentiellement via email.

