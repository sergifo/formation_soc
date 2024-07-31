La commande `nslookup` est utilisée pour interroger les serveurs DNS pour obtenir des informations sur les domaines, les adresses IP et d'autres enregistrements DNS.

### Utilisation de `nslookup` sur Kali Linux


1. **Requête DNS de base**

Pour effectuer une requête DNS de base pour `scanme.nmap.org`, utilisez la commande suivante :

```bash
nslookup scanme.nmap.org
```

Cette commande retournera l'adresse IP associée au domaine `scanme.nmap.org`.

2. **Requête DNS inversée**

Pour effectuer une recherche DNS inversée (obtenir le nom de domaine à partir d'une adresse IP), utilisez l'option `-x` :

```bash
nslookup 45.33.32.156
```

Remplacez `45.33.32.156` par l'adresse IP obtenue dans la requête DNS de base.

3. **Spécifier un serveur DNS**

Pour interroger un serveur DNS spécifique, utilisez l'option `server` :

```bash
nslookup scanme.nmap.org 8.8.8.8
```

Dans cet exemple, `8.8.8.8` est l'adresse IP du serveur DNS de Google.

4. **Obtenir des enregistrements spécifiques**

Pour interroger des types d'enregistrements spécifiques, vous pouvez utiliser `set type` :

- **Enregistrements A** (Adresse IP) :
  ```bash
  nslookup -type=A scanme.nmap.org
  ```

- **Enregistrements MX** (Serveur de messagerie) :
  ```bash
  nslookup -type=MX scanme.nmap.org
  ```

- **Enregistrements TXT** (Informations textuelles) :
  ```bash
  nslookup -type=TXT scanme.nmap.org
  ```

- **Enregistrements NS** (Serveur de noms) :
  ```bash
  nslookup -type=NS scanme.nmap.org
  ```

#### 3. Mode interactif

`nslookup` peut également être utilisé en mode interactif pour exécuter plusieurs requêtes successives. Voici comment entrer en mode interactif :

```bash
nslookup
```

Ensuite, dans le mode interactif, vous pouvez entrer les commandes suivantes :

- Pour définir le type de requête :
  ```plaintext
  > set type=A
  ```

- Pour interroger un domaine :
  ```plaintext
  > scanme.nmap.org
  ```

- Pour changer de serveur DNS :
  ```plaintext
  > server 8.8.8.8
  ```

- Pour quitter le mode interactif :
  ```plaintext
  > exit
  ```

### Exemples concrets

1. **Requête DNS de base** :
   ```bash
   nslookup scanme.nmap.org
   ```

   **Sortie** :
   ```plaintext
   Server:         192.168.1.1
   Address:        192.168.1.1#53

   Non-authoritative answer:
   Name:   scanme.nmap.org
   Address: 45.33.32.156
   ```

2. **Recherche DNS inversée** :
   ```bash
   nslookup 45.33.32.156
   ```

   **Sortie** :
   ```plaintext
   156.32.33.45.in-addr.arpa   name = scanme.nmap.org.
   ```

3. **Spécifier un serveur DNS** :
   ```bash
   nslookup scanme.nmap.org 8.8.8.8
   ```

4. **Requête pour un enregistrement MX** :
   ```bash
   nslookup -type=MX scanme.nmap.org
   ```

5. **Mode interactif** :
   ```bash
   nslookup
   ```

   Ensuite, dans le mode interactif :
   ```plaintext
   > set type=NS
   > scanme.nmap.org
   ```

