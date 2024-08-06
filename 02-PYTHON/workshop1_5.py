# Workshop N°1
# 5. Vérification  de  l'état  de  maintenance  d'un  serveur:  Déterminer  si  un  serveur  est
# actuellement en maintenance ou non, sans utiliser de structures conditionnelles.
# Consignes:
# Demandez à l'utilisateur si le serveur est en maintenance. L'utilisateur doit répondre
# par "oui" ou "non".
# Convertissez  la  réponse  de  l'utilisateur  en  un  booléen  (True  pour  "oui",  False  pour
# "non").
# Affichez  un  message  indiquant  si  le  serveur  est  en  maintenance  ou  non,  en  utilisant
# directement la valeur booléenne dans la phrase.
# Utopios® Tous droits réservés 31





# est ce que le serveur est en maintenance
serv_maint = input("est ce que le serveur est en maintenance ?  repondez oui ou non : ")
serv_maint = serv_maint.lower()
maint = bool(serv_maint == "oui")
print(f"le serveur est en maintenance :{maint}")


