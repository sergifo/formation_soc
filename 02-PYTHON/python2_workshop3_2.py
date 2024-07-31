#Workshop N°3
 #2. Vérification des Unités de Stockage avec Tentatives Limitées: Un data center doit régulièrement vérifier
 #l'état de santé de ses unités de stockage pour prévenir les défaillances. Chaque unité de stockage doit passer
 #une série de tests. Si un test échoue, le système doit retenter jusqu'à un maximum de 3 fois avant de marquer
 #l'unité comme nécessitant une inspection manuelle.
 #Consignes:
 #Simulez la vérification de 3 unités de stockage en utilisant une boucle pour chaque unité.
 #Pour chaque unité, le système tente de passer un test (vous pouvez simuler cela en demandant à
 #l'utilisateur si le test a réussi ou échoué).
 #Si un test échoue, le système retente jusqu'à 3 fois au total. Si les tests échouent après 3 tentatives, l'unité
 #est marquée pour inspection manuelle.
 #Après avoir traité les 3 unités, affichez combien nécessitent une inspection manuelle.

unites_de_stockages = [1,4]
test_reussi = ""
test_echoue = ""
for i in (unites_de_stockages):
    if test_reussi == "oui":
        unites_de_stockages.append = i
    elif test_echoue == "non":
        unites_de_stockages.append = i
    else:
        input("saisir oui ou non")



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

latence_reseau = 0
latences_reseau =[]
for latence_reseau in latences_reseau:
    input("saisir la latence du reseau")
    if latence_reseau > 100 :
        print("avertissemnt!! les actions correstives ont été prises? ")
        reponse =input("repoudez oui ou non")
        if (reponse == "oui" and latence_reseau < 100):
            input("saisir la latence du reseau"
                  if reponse== 3* "oui":
                  print("probleme majeur")
                  break
                  elif:
                  reponse == "stop"
                  break




                  



        
        










