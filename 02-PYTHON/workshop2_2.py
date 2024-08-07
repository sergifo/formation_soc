# Workshop N°2
# 2. Classification des incidents: Classer les incidents reportés dans un data center selon leur
# niveau de gravité en utilisant l'expression match.
# Consignes:
# Demandez à l'utilisateur de saisir un niveau de gravité pour un incident (par exemple,
# "faible", "modéré", "élevé").
# Utilisez une expression match pour associer le niveau de gravité à une action prédéfinie.
# Affichez l'action à entreprendre selon le niveau de gravité de l'incident.
# Utopios® Tous droits réservés 40


# Demande à l'utilisateur de saisir un niveau de gravité pour un incident (par exemple, "faible", "modéré", "élevé").
niv_grav = input("veuiller saisir un niveau de gravitéde l'incident: faible, modéré, élevé :")
# Utilisation de  l'expression match pour associer le niveau de gravité à une action prédéfinie
match niv_grav.lower():
    case "faible":
        act_pred = "incident faible continuez à surveiller "
    case "modéré":
        act_pred = "incident modéré ,faites attention ou signalez cette incident"
    case "élevé":
        act_pred = "incident élevé"
        act_pred = "incident élevé ,intervention urgente"
    

#affichage de l'action predefinie
print(act_pred)