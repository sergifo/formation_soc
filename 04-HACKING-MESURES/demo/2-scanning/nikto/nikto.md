Nikto est un scanner de vulnérabilités web open-source qui permet d'analyser des sites web pour détecter diverses vulnérabilités, configurations dangereuses et autres problèmes de sécurité. Voici quelques commandes et exemples d'utilisation de Nikto :

### Installation de Nikto

Si Nikto n'est pas déjà installé sur votre machine Kali, vous pouvez l'installer en utilisant la commande suivante :

```bash
sudo apt update
sudo apt install nikto
```

### Utilisation de Nikto

#### 1. Scanner une URL

Pour scanner une URL spécifique, utilisez la commande suivante :

```bash
nikto -h http://m2i.com
```

#### 2. Scanner un site HTTPS

Pour scanner un site web sécurisé (HTTPS), utilisez la commande suivante :

```bash
nikto -h https://m2i.com
```

#### 3. Spécifier un port

Pour scanner un site web sur un port spécifique, utilisez l'option `-p` :

```bash
nikto -h http://m2i.com -p 8080
```

#### 4. Scanner un hôte avec un fichier de liste d'URLs

Vous pouvez scanner plusieurs URLs en les listant dans un fichier et en utilisant l'option `-h` pour spécifier le fichier :

```bash
nikto -h urls.txt
```

#### 5. Sauvegarder les résultats dans un fichier

Pour sauvegarder les résultats du scan dans un fichier, utilisez l'option `-o` et spécifiez le format de sortie avec `-Format` :

```bash
nikto -h http://m2i.com -o output.txt -Format txt
```

Nikto supporte plusieurs formats de sortie comme `txt`, `html`, `csv`, et `xml`.

#### 6. Exclure certains tests

Pour exclure certains tests, utilisez l'option `-T` suivie des numéros des tests à exclure :

```bash
nikto -h http://m2i.com -T 2,4,5
```

#### 7. Scanner avec une adresse IP

Pour scanner un site web en utilisant une adresse IP spécifique au lieu du nom de domaine, utilisez l'option `-nossl` pour éviter les erreurs SSL :

```bash
nikto -h http://192.168.1.1
```

#### 8. Utiliser un proxy

Pour scanner un site web en utilisant un proxy, utilisez les options `-useproxy` et `-proxy` :

```bash
nikto -h http://m2i.com -useproxy http://proxy.m2i.com:8080
```

#### 9. Spécifier l'agent utilisateur

Pour spécifier l'agent utilisateur (User-Agent) que Nikto utilise, utilisez l'option `-useragent` :

```bash
nikto -h http://m2i.com -useragent "Mozilla/5.0 (compatible; Nikto/2.1.5)"
```

#### 10. Scanner en utilisant des cookies

Pour inclure des cookies dans le scan, utilisez l'option `-C` :

```bash
nikto -h http://m2i.com -C "PHPSESSID=abc123; path=/"
```

### Commandes pratiques

#### 1. Afficher l'aide

Pour afficher toutes les options disponibles avec Nikto, utilisez l'option `-Help` :

```bash
nikto -Help
```

#### 2. Scanner en mode verbose

Pour exécuter un scan en mode verbose (détaillé), utilisez l'option `-v` :

```bash
nikto -h http://m2i.com -v
```

#### 3. Scanner une plage d'IP

Pour scanner une plage d'adresses IP, utilisez l'option `-h` avec la plage d'IP :

```bash
nikto -h 192.168.1.1-192.168.1.254
```

### Exemples concrets

#### Exemple 1 : Scan basique

```bash
nikto -h http://m2i.com
```

#### Exemple 2 : Scan avec sortie HTML

```bash
nikto -h http://m2i.com -o report.html -Format html
```

#### Exemple 3 : Scan d'un site web sécurisé sur un port spécifique

```bash
nikto -h https://m2i.com -p 8443
```

#### Exemple 4 : Scan en utilisant un proxy

```bash
nikto -h http://m2i.com -useproxy http://proxy.m2i.com:8080
```

#### Exemple 5 : Scan avec exclusion de certains tests

```bash
nikto -h http://m2i.com -T 2,4,5
```

En utilisant ces commandes, vous pouvez scanner des applications web pour diverses vulnérabilités et configurations dangereuses, ce qui vous aide à améliorer la sécurité de vos applications web.