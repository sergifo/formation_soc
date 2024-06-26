#liste
first_list = ['bonjour', 'toto', 10, True]

print(first_list)
#ajouter un element
first_list.append(50.00)

#obtenir le nombre d'elements
print(len(first_list))

#trie les elements de la liste
first_list.sort()

#pour parcourir unr liste
for element in first_list:
    print(element)

# pour afficher l'element ( on ne rajoute ou enlever un element jamais dans une liste pendant son parcours) 
for i in range(len(first_list)):
    print(f"index {i} value {first_list[i]}")



