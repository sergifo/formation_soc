#Workshop N°3
 #3. Surveillance des Performances de Réseau avec des Seuils: Dans un data center, il est crucial de surveiller la
 #performance du réseau pour s'assurer qu'elle répond aux exigences. Vous devez simuler un système de
 #surveillance qui vérifie périodiquement la latence du réseau. Si la latence dépasse un seuil spécifique, des
 #actions doivent être prises.
 #Consignes:
 #Utilisez une boucle pour simuler la surveillance continue de la latence du réseau.
 #À chaque itération, demandez à l'utilisateur de saisir la latence actuelle du réseau.
 #Si la latence dépasse 100 ms, affichez un avertissement et demandez si des actions correctives ont été
 #prises (l'utilisateur répond par oui ou non).
 #Si des actions correctives ont été prises et la latence revient en dessous de 100 ms dans les tentatives
 #suivantes, continuez la surveillance; sinon, après 3 avertissements consécutifs, le système doit signaler un
 #problème majeur et s'arrêter.
 #La surveillance s'arrête également si l'utilisateur saisit "stop" à tout moment.




# Initialisation des variables
avertissements_consecutifs = 0
seuil_latence = 100  # en ms

# Boucle de surveillance continue
while True:
    # Demande à l'utilisateur de saisir la latence actuelle ou 'stop' pour arrêter
    saisie_utilisateur = input("Entrez la latence actuelle du réseau en ms ou 'stop' pour arrêter la surveillance : ")
    
    # Vérification si l'utilisateur souhaite arrêter la surveillance
    if saisie_utilisateur.lower() == 'stop':
        print("Arrêt de la surveillance du réseau.")
        break

    # Vérification si la saisie est un nombre
    if saisie_utilisateur.isdigit():
        latence_actuelle = int(saisie_utilisateur)
        if latence_actuelle > seuil_latence:
            print("Avertissement : la latence dépasse le seuil autorisé de 100 ms.")
            avertissements_consecutifs += 1  # Incrémentation du compteur d'avertissements
            action_corrective = input("Des actions correctives ont-elles été prises ? (oui/non) : ").lower()
            
            # Vérification si des actions correctives ont été prises
            if action_corrective == 'oui':
                avertissements_consecutifs = 0  # Réinitialisation du compteur d'avertissements
                print("Surveillance continue...")
            elif avertissements_consecutifs >= 3:
                print("Problème majeur détecté. Arrêt de la surveillance et nécessité d'une intervention immédiate.")
                break
        else:
            avertissements_consecutifs = 0  # Réinitialisation du compteur si la latence est en dessous du seuil
            print("La latence est dans les limites acceptables. Surveillance continue...")
    else:
        print("Veuillez entrer une valeur numérique pour la latence ou 'stop' pour arrêter la surveillance.")