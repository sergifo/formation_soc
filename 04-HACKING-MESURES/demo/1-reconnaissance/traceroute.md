Sur Kali : 

La commande `traceroute` est utilisée pour diagnostiquer le chemin que prend un paquet pour atteindre une destination spécifique sur un réseau. C'est un outil utile pour identifier les problèmes de connectivité et comprendre le cheminement des paquets à travers différents routeurs et points d'accès réseau.

### Utilisation de Traceroute sur une IP Locale

Pour utiliser `traceroute` sur une IP locale, suivez ces étapes :


#### 2. Exécution de Traceroute

Pour exécuter `traceroute` sur une IP locale, utilisez simplement la commande suivie de l'adresse IP cible. Par exemple, pour tracer la route vers l'IP locale `192.168.1.1` :

```bash
traceroute 192.168.1.1
```

#### Options utiles pour Traceroute

Voici quelques options utiles que vous pouvez utiliser avec `traceroute` :

- **-n** : Ne résout pas les noms d'hôtes, affiche uniquement les adresses IP.
  ```bash
  traceroute -n 192.168.1.1
  ```

- **-I** : Utilise des paquets ICMP Echo au lieu des paquets UDP.
  ```bash
  traceroute -I 192.168.1.1
  ```

- **-T** : Utilise le protocole TCP SYN au lieu des paquets UDP.
  ```bash
  traceroute -T 192.168.1.1
  ```

- **-p** : Spécifie le port de destination pour les paquets UDP ou TCP.
  ```bash
  traceroute -p 80 192.168.1.1
  ```

- **-m** : Spécifie le nombre maximum de sauts (TTL) que les paquets peuvent traverser.
  ```bash
  traceroute -m 20 192.168.1.1
  ```

- **-w** : Définit le délai d'attente en secondes pour chaque réponse.
  ```bash
  traceroute -w 2 192.168.1.1
  ```

#### Exemple de Traceroute

Voici quelques exemples concrets de commandes `traceroute` :

1. **Traceroute de base** :
   ```bash
   traceroute 192.168.1.1
   ```

2. **Traceroute sans résolution de noms** :
   ```bash
   traceroute -n 192.168.1.1
   ```

3. **Traceroute en utilisant ICMP** :
   ```bash
   traceroute -I 192.168.1.1
   ```

4. **Traceroute en utilisant TCP sur le port 80** :
   ```bash
   traceroute -T -p 80 192.168.1.1
   ```

5. **Traceroute avec un nombre maximum de 10 sauts** :
   ```bash
   traceroute -m 10 192.168.1.1
   ```

6. **Traceroute avec un délai d'attente de 5 secondes** :
   ```bash
   traceroute -w 5 192.168.1.1
   ```

### Analyse des résultats

Lors de l'exécution de la commande `traceroute`, vous verrez une sortie qui affiche chaque saut que le paquet traverse pour atteindre la destination. Chaque ligne de la sortie représente un saut (routeur ou point d'accès intermédiaire) entre votre machine et la machine cible. 

Les colonnes affichent généralement :

- Le numéro du saut.
- L'adresse IP (ou le nom d'hôte s'il est résolu) du routeur intermédiaire.
- Les temps de réponse pour chaque tentative de ping (généralement trois tentatives).

Voici un exemple de sortie typique de `traceroute` :

```plaintext
traceroute to 192.168.1.1 (192.168.1.1), 30 hops max, 60 byte packets
 1  192.168.1.1 (192.168.1.1)  1.123 ms  1.025 ms  1.037 ms
```

Ce résultat montre que la destination `192.168.1.1` a été atteinte en un seul saut avec des temps de réponse d'environ 1 milliseconde.

