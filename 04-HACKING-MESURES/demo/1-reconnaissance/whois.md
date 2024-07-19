La commande `whois` est utilisée pour interroger les bases de données de registres pour obtenir des informations sur les noms de domaine, les adresses IP, les ASN (Autonomous System Numbers), etc. C'est un outil précieux pour la collecte d'informations sur la propriété d'un domaine, les contacts administratifs, les dates de création et d'expiration, et bien plus encore.


#### 2. Utilisation de la commande `whois`

##### Requête de base

Pour effectuer une recherche `whois` de base sur un nom de domaine, utilisez la commande suivante :

```bash
whois example.com
```

Cette commande renverra les informations enregistrées pour le domaine `example.com`.

##### Requête pour une adresse IP

Pour effectuer une recherche `whois` sur une adresse IP, utilisez la commande suivante :

```bash
whois 8.8.8.8
```

Cette commande renverra les informations enregistrées pour l'adresse IP `8.8.8.8`.

##### Requête pour un ASN (Autonomous System Number)

Pour effectuer une recherche `whois` sur un ASN, utilisez la commande suivante :

```bash
whois AS15169
```

Cette commande renverra les informations enregistrées pour l'ASN `15169`, qui appartient à Google.

### Exemple concret : Recherche sur `scanme.nmap.org`

1. **Requête de base pour le domaine** :

```bash
whois scanme.nmap.org
```

**Exemple de sortie** :

```plaintext
Domain Name: NMAP.ORG
Registry Domain ID: D96829275-LROR
Registrar WHOIS Server: whois.godaddy.com
Registrar URL: http://www.godaddy.com
Updated Date: 2021-01-29T01:26:15Z
Creation Date: 2003-04-09T18:28:39Z
Registry Expiry Date: 2022-04-09T18:28:39Z
Registrar Registration Expiration Date:
Registrar: GoDaddy.com, LLC
Registrar IANA ID: 146
Registrar Abuse Contact Email: abuse@godaddy.com
Registrar Abuse Contact Phone: +1.4806242505
Reseller:
Domain Status: clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited
Domain Status: clientRenewProhibited https://icann.org/epp#clientRenewProhibited
Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited
Domain Status: clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited
Registrant Organization: Gordon Lyon
Registrant State/Province: Oregon
Registrant Country: US
Name Server: NS-1897.AWSDNS-45.CO.UK
Name Server: NS-893.AWSDNS-47.NET
Name Server: NS-174.AWSDNS-21.COM
Name Server: NS-1022.AWSDNS-63.ORG
DNSSEC: unsigned
URL of the ICANN Whois Inaccuracy Complaint Form https://www.icann.org/wicf/)
>>> Last update of WHOIS database: 2021-12-04T15:00:38Z <<<
```

Cette sortie montre des informations telles que les dates de création et d'expiration du domaine, le registraire, l'état du domaine, les serveurs de noms, et les informations de contact du propriétaire du domaine.

2. **Requête pour une adresse IP** :

```bash
whois 45.33.32.156
```

**Exemple de sortie** :

```plaintext
NetRange:       45.32.0.0 - 45.35.255.255
CIDR:           45.32.0.0/14
NetName:        LINODE-US
NetHandle:      NET-45-32-0-0-1
Parent:         NET45 (NET-45-0-0-0-0)
NetType:        Direct Allocation
OriginAS:       AS63949
Organization:   Linode, LLC (LINODE)
RegDate:        2015-02-18
Updated:        2016-04-14
Ref:            https://rdap.arin.net/registry/ip/45.32.0.0

OrgName:        Linode, LLC
OrgId:          LINODE
Address:        249 Arch St.
City:           Philadelphia
StateProv:      PA
PostalCode:     19106
Country:        US
RegDate:        2008-04-24
Updated:        2019-08-22
Ref:            https://rdap.arin.net/registry/entity/LINODE
```

Cette sortie montre des informations telles que le propriétaire de l'adresse IP, la plage d'adresses IP associée, l'organisation, et les informations de contact.

### Options supplémentaires de `whois`

- **Afficher des informations brutes** : Parfois, les informations retournées sont filtrées. Vous pouvez demander des informations brutes avec :
  ```bash
  whois -B example.com
  ```

- **Spécifier un serveur whois** : Si vous souhaitez interroger un serveur whois spécifique, utilisez l'option `-h` :
  ```bash
  whois -h whois.verisign-grs.com example.com
  ```

- **Aide et options** : Pour voir toutes les options disponibles avec `whois`, utilisez l'option `--help` :
  ```bash
  whois --help
  ```

