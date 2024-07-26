# Exercice Liste
# Via l'utilisation d'une variable de type **liste**, vous devrez réaliser un logiciel permettant à l'utilisateur d'entrer
# une **série de notes**, dont le nombre possible à entrer sera soit (au choix de l'utilisateur) : 
# - saisie avant la saisie de notes 
# - permissif et pourra aller jusqu'à entrer une note négative qui stoppera la saisie des notes. 
# - Une fois la **saisie des notes terminée**, l'utilisateur aura à sa disposition un **affichage** lui permettant d'avoir 
# la **note max**, la **note min** ainsi que la **moyenne** (possible de faire un menu pour choisir) 

liste_notes = []
serie_notes = int(input("votre serie de notes >>"))

for note in range(serie_notes):
    valeur_note = int(input("votre listes notes:"))
    liste_notes.append(valeur_note)

print(liste_notes)

print(f"la note maximun est {max(liste_notes)}")
print(f"la note minimun est {min(liste_notes)}")
print(f"la moyenne est est {(sum(liste_notes) / len(liste_notes))}")


