### Étapes pour utiliser Maltego sur Kali Linux pour analyser `scanme.nmap.org`

#### 1. Installation de Maltego

Maltego est souvent pré-installé sur Kali Linux, mais si ce n'est pas le cas, vous pouvez l'installer en suivant ces étapes :

```bash
sudo apt update
sudo apt install maltego
```

#### 2. Lancer Maltego

Une fois installé, lancez Maltego :

```bash
maltego
```

#### 3. Configuration initiale de Maltego

1. **Créer un compte** : Lors de votre première utilisation, vous serez invité à créer un compte Maltego ou à vous connecter à un compte existant. Suivez les instructions à l'écran pour configurer votre compte.

2. **Sélectionner un profil** : Maltego propose plusieurs profils de travail (par exemple, Standard, Penetration Testing, etc.). Sélectionnez le profil qui convient le mieux à votre utilisation.

#### 4. Créer un nouveau graph

1. **Nouveau document** : Cliquez sur "New" pour créer un nouveau document.

2. **Sélectionner un type d'entité** : Vous commencerez par sélectionner une entité de départ. Dans ce cas, vous pouvez choisir "Domain".

#### 5. Ajouter `scanme.nmap.org` comme entité de départ

1. **Ajouter une entité** : Faites glisser l'entité "Domain" dans le canvas.

2. **Configurer l'entité** : Double-cliquez sur l'entité et entrez `scanme.nmap.org` comme nom de domaine.

#### 6. Exécuter les transformations

Les transformations sont des actions automatiques que Maltego peut exécuter pour récupérer des informations sur l'entité. Voici comment les utiliser :

1. **Sélectionner les transformations** : Cliquez avec le bouton droit sur l'entité `scanme.nmap.org` pour afficher le menu des transformations disponibles.

2. **Exécuter les transformations** : Vous pouvez exécuter plusieurs transformations pour collecter différentes informations :
    - **To DNS Name** : Pour découvrir les noms DNS associés.
    - **To IP Address** : Pour obtenir l'adresse IP du domaine.
    - **To Domain WHOIS Information** : Pour obtenir les informations WHOIS du domaine.
    - **To Website** : Pour récupérer les informations du site web.
    - **To Email Address** : Pour trouver des adresses email associées.

3. **Analyser les résultats** : Les résultats de chaque transformation seront ajoutés au graph sous forme de nouvelles entités reliées à l'entité de départ.

#### 7. Analyser les résultats

1. **Explorer le graph** : Utilisez les outils de navigation et de zoom pour explorer les entités et leurs relations sur le graph.

2. **Inspecter les entités** : Cliquez sur chaque entité pour afficher ses détails dans le panneau de propriétés.

3. **Utiliser les transformations sur les nouvelles entités** : Vous pouvez continuer à exécuter des transformations sur les nouvelles entités pour approfondir votre analyse.

#### 8. Exporter les résultats

Une fois l'analyse terminée, vous pouvez exporter le graph et les données pour une utilisation ultérieure :

1. **Exporter le graph** : Allez dans "File" -> "Export" et choisissez le format d'exportation (par exemple, PDF, GraphML, etc.).

2. **Sauvegarder le document** : Enregistrez le document Maltego pour pouvoir le réouvrir et le modifier ultérieurement.

