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




