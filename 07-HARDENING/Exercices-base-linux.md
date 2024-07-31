### Exercice 1: Installation et premier audit avec Lynis

**Objectif**: Installer Lynis et réaliser un premier audit de sécurité.

**Étapes**:
1. Installez Lynis sur votre distribution Linux (par exemple, sur Debian/Ubuntu, utilisez `sudo apt install lynis`).
2. Exécutez Lynis pour un premier audit : `sudo lynis audit system`
3. Examinez le rapport généré et notez les avertissements et suggestions.

### Exercice 2: Durcissement des comptes utilisateurs

**Objectif**: Améliorer la sécurité des comptes utilisateurs selon les recommandations de Lynis.

**Étapes**:
1. Examinez les recommandations de Lynis concernant les comptes utilisateurs.
2. Mettez en œuvre des mots de passe plus forts et des politiques de verrouillage des comptes. Vous pouvez utiliser `passwd` pour changer les mots de passe et modifier `/etc/login.defs` pour les politiques.
3. Assurez-vous que tous les comptes utilisateurs ont des mots de passe ou sont désactivés s'ils ne sont pas utilisés.

### Exercice 3: Sécurisation de SSH

**Objectif**: Renforcer les paramètres de sécurité du service SSH.

**Étapes**:
1. Suivez les recommandations de Lynis concernant SSH (souvent situées dans `/etc/ssh/sshd_config`).
2. Désactivez la connexion root à distance en modifiant `PermitRootLogin` en `no`.
3. Limitez les utilisateurs qui peuvent se connecter via SSH avec l'option `AllowUsers`.

### Exercice 4: Mise en place de pare-feu

**Objectif**: Configurer un pare-feu de base avec `ufw` (Uncomplicated Firewall).

**Étapes**:
1. Installez `ufw` si ce n'est pas déjà fait (`sudo apt install ufw` sur Debian/Ubuntu).
2. Activez `ufw` et configurez des règles de base, comme `sudo ufw allow from 192.168.1.0/24 to any port 22` pour permettre le SSH seulement à partir de votre réseau local.
3. Activez le pare-feu avec `sudo ufw enable` et vérifiez son statut avec `sudo ufw status`.

### Exercice 5: Automatisation des audits de sécurité avec Lynis

**Objectif**: Configurer des audits réguliers avec Lynis.

**Étapes**:
1. Créez un script shell qui exécute `lynis audit system`.
2. Programmez ce script pour qu'il s'exécute régulièrement à l'aide de `cron`. Par exemple, pour le faire tourner chaque semaine, ajoutez une ligne à votre crontab (`sudo crontab -e`) comme ceci : `0 3 * * 1 /chemin/vers/votre/script.sh`.


Voici deux exercices supplémentaires pour continuer à renforcer la sécurité d'un système Linux avec l'aide de Lynis et d'autres pratiques de hardening.

### Exercice 6: Sécurisation des services réseau

**Objectif** : Minimiser les risques associés aux services réseau en désactivant ceux qui sont inutiles et en sécurisant ceux qui sont nécessaires.

**Étapes** :
1. Identifiez les services en cours d'exécution sur le système avec `sudo systemctl list-units --type=service`.
2. Analysez le rapport de Lynis pour voir quelles suggestions sont faites concernant les services réseau.
3. Désactivez les services inutiles. Par exemple, si vous n'utilisez pas `cups` (le système d'impression), désactivez-le avec `sudo systemctl disable cups`.
4. Pour les services nécessaires, assurez-vous qu'ils sont configurés de manière sécurisée. Par exemple, si vous utilisez Apache ou Nginx, assurez-vous que les configurations suivent les meilleures pratiques de sécurité, comme l'utilisation de HTTPS et la restriction des accès non autorisés.

