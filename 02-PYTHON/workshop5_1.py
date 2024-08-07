# workshop5_1
#  Gestion des Utilisateurs du Data Center
# Consignes:
# Créez une fonction ajouter_utilisateur qui prend comme arguments le nom de l'utilisateur et son rôle (ex:
# "Administrateur", "Visiteur", "Opérateur") et l'ajoute à un dictionnaire global utilisateurs, où le nom est la
# clé et le rôle est la valeur.
# Écrivez une fonction changer_role qui modifie le rôle d'un utilisateur existant. La fonction doit vérifier si
# l'utilisateur existe avant de changer le rôle.
# Développez une fonction afficher_utilisateurs qui imprime tous les utilisateurs et leurs rôles.
# Utopios® Tous droits réservés 6

utilisateurs = {}
def ajouter_utilisateur(nom_utilisateur, role):
    print(f"utilisateur : {nom_utilisateur}, son role : {role}")





def changer_role(nom_utilisateur, nouveau_role):
     if nom_utilisateur in utilisateurs.keys():
         utilisateurs[nom_utilisateur] = nouveau_role
         print(f"le role de l'utilisateur {nom_utilisateur} a changé en {nouveau_role}")
     else:
         print(f"l'utisateur{nom_utilisateur} n'existe pas")




def afficher_utilisateurs():
    for nom_utilisateur, role in utilisateurs.items():
        print(f"nom utilisateur : {nom_utilisateur}, son role: {role}")
    
#ajouter_utilisateur("zidane", "numero 10")
# ajouter_utilisateur("adebayor", "numero 4")




#solution ihab

# dictionnaire_utilisateurs = {}
# def ajouter_utilisateur(nom_utilisateur: str, role_utilisater: str) -> None:
#     if nom_utilisateur not in dictionnaire_utilisateurs:
#         dictionnaire_utilisateurs[nom_utilisateur] = role_utilisater

# def changer_role(nom_utilisateur: str, nouveau_role_utilisater: str) -> None:
#     if nom_utilisateur in dictionnaire_utilisateurs:
#         dictionnaire_utilisateurs[nom_utilisateur] = nouveau_role_utilisater


# # def affecter_role_utilisateur(nom_utilisateur: str, role_utilisateur: str) -> None:
# #     dictionnaire_utilisateurs[nom_utilisateur] = role_utilisateur

# def afficher_utilisateur():
#     print("======== Liste utilisateurs =========")
#     for nom, role in dictionnaire_utilisateurs.items():
#         print(f"Nom : {nom}, Role : {role}")


# ajouter_utilisateur("toto", "admin")
# afficher_utilisateur()
# ajouter_utilisateur("tata", "dev")
# afficher_utilisateur()
# ajouter_utilisateur("titi", "admin")
# afficher_utilisateur()
# changer_role("titi", "dev")
# afficher_utilisateur()


        


















    
    

    


