import os
from datetime import datetime

nom_fichier = "data.txt"

def ajouter_une_ligne(ligne):
    # vérification si le fichier exist
    if os.path.exists(nom_fichier):
        with open(nom_fichier, 'a') as fichier:
            fichier.write(f"{ligne}\n")
    else:
        with open(nom_fichier, 'w') as fichier:
            fichier.write(f"{ligne}\n")

ajouter_une_ligne("La première ")
ajouter_une_ligne("La deuxième ")


## Exercice : Journalisation des événements de sécurité

# **Objectif** : Créer un script Python qui enregistre des événements de sécurité dans un fichier. Chaque événement doit être horodaté avec la date et l’heure actuelles.

# 	1.	Vérifiez l’existence d’un fichier de journalisation nommé security_log.txt.
# 	- Si le fichier existe, ajoutez un nouvel événement avec la date et l’heure actuelles.
# 	- Si le fichier n’existe pas, créez-le et ajoutez le premier événement avec la date et l’heure actuelles.
# 	2.	Demandez à l’utilisateur de saisir une description de l’événement de sécurité.
# 	3.	Écrivez l’événement dans le fichier avec le format suivant :
#   [YYYY-MM-DD HH:MM:SS] - Description de l'événement

import os
from datetime import datetime

fichier_journalisation = "data.txt"

def security_log():
    if os.path.exists(fichier_journalisation):
        with open(fichier_journalisation, 'a') as log_fichier:
            log_fichier.write(f"{datetime(evenement)}\n")
    else:
        with open(fichier_journalisation, 'w') as log_fichier:
            log_fichier.write()


#correction ihab
from datetime import datetime
import os
def convertir_format_datetime_pour_log():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def ajouter_log_dans_fichier(nom_fichier, description_evenement):
    if os.path.exists(nom_fichier):
        mode = 'a'
    else:
        mode = 'w'
    
    with open(nom_fichier, mode) as fichier:
        fichier.write(f"{convertir_format_datetime_pour_log()} - {description_evenement} \n")

