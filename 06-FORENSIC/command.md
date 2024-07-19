# Command regripper
rip.exe -r c:\Windows\System32\config\SYSTEM -f system

# Fichier Registre
1. SYSTEM
- Informations sur le matériel et os.
- Sécurité système
- Information sur le boot
- Configuration réseau

2. SAM
- Information sur les utilisateurs et groupes 
- Hash mot de passe

3. SOFTWARE
- Installations logicielles
- Chemins d'application

...


## Commande pour calculer le hash d'un fichier avec power shell
```ps1
Get-FileHash -Path "chemin/vers/fichier" -Algorithm <Type_ALGO>
```
