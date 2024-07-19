SpiderFoot est un outil open-source d'intelligence artificielle qui permet de recueillir des informations sur une cible à partir de diverses sources de données en ligne. Il peut être utilisé pour effectuer des reconnaissances automatisées sur des noms de domaine, des adresses IP, des adresses email, des noms d'utilisateur, etc. Voici comment installer et utiliser SpiderFoot sur Kali Linux pour analyser une cible comme `scanme.nmap.org`.

### Installation de SpiderFoot

#### 1. Mise à jour de Kali Linux

Assurez-vous que votre système Kali est à jour :

```bash
sudo apt update
sudo apt upgrade -y
```

### Utilisation de SpiderFoot

#### 1. Lancer SpiderFoot

##### Méthode 1: Utilisation native

Pour lancer SpiderFoot installé via les dépôts Kali Linux, utilisez la commande suivante :

```bash
spiderfoot -l 127.0.0.1:5001
```

#### 2. Accéder à l'interface web de SpiderFoot

Ouvrez votre navigateur web et accédez à l'URL suivante :

```
http://127.0.0.1:5001
```

Vous verrez l'interface utilisateur de SpiderFoot.

#### 3. Créer une nouvelle analyse

1. **Accéder à l'interface utilisateur de SpiderFoot**.
2. **Cliquer sur "New Scan"**.
3. **Configurer l'analyse** :
   - **Target** : Entrez `scanme.nmap.org`.
   - **Scan Options** : Sélectionnez les modules que vous souhaitez exécuter. SpiderFoot propose de nombreux modules pour récupérer des informations à partir de diverses sources.
4. **Lancer l'analyse** :
   - Cliquez sur "Run Scan".

#### 4. Analyser les résultats

Une fois l'analyse terminée, vous pouvez explorer les résultats en cliquant sur le nom de l'analyse dans la liste des scans. Les résultats seront organisés en différentes catégories, telles que :

- **Domaines et sous-domaines**.
- **Adresses IP**.
- **Serveurs de noms**.
- **Informations WHOIS**.
- **Adresses email**.
- **Fuites de données**.
- **Informations sur les réseaux sociaux**.

### Exemple de configuration et de scan

1. **Lancer SpiderFoot** :

```bash
spiderfoot -l 127.0.0.1:5001
```

2. **Accéder à l'interface web** :

Ouvrez votre navigateur et allez à `http://127.0.0.1:5001`.

3. **Créer une nouvelle analyse** :

- **Target** : `scanme.nmap.org`.
- **Modules** : Sélectionnez des modules comme `DNS`, `WHOIS`, `Subdomains`, `Email Addresses`, `Social Media`, etc.
- **Options** : Configurez les options spécifiques du module si nécessaire.

4. **Lancer l'analyse** :

Cliquez sur "Run Scan".

5. **Explorer les résultats** :

Une fois l'analyse terminée, cliquez sur l'analyse pour explorer les résultats détaillés. Vous pouvez voir les informations récupérées, telles que les sous-domaines, les adresses IP associées, les informations WHOIS, les adresses email trouvées, etc.

### Utilisation de SpiderFoot CLI

SpiderFoot propose également une interface en ligne de commande (CLI) pour automatiser les scans et intégrer les résultats dans des scripts ou des pipelines CI/CD.

#### Exécuter un scan en CLI

```bash
spiderfoot -s scanme.nmap.org -m all
```

- **-s** : Spécifie la cible.
- **-m** : Spécifie les modules à exécuter (`all` pour tous les modules).
