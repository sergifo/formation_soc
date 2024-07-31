echo "Attention : Ce script va intentionnellement affaiblir la sécurité de votre système Ubuntu."
read -p "Êtes-vous sûr de vouloir continuer ? (oui/non) " response

if "$response" != "oui"; then
    echo "Opération annulée."
    exit


echo "Désactivation du firewall UFW..."
sudo ufw disable


echo "Installation de Telnet..."
sudo apt-get install -y telnet


echo "Création d'un utilisateur 'testuser' sans mot de passe..."
sudo useradd testuser -s /bin/bash
sudo passwd -d testuser

echo "Modification des permissions sur /etc/shadow pour qu'il soit accessible en écriture..."
sudo chmod o+w /etc/shadow


echo "Modification de SSH pour permettre la connexion directe de l'utilisateur root..."
sudo sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
sudo systemctl restart sshd


echo "Installation d'un service FTP vulnérable..."
sudo apt-get install -y vsftpd
sudo systemctl start vsftpd

echo "Installation et configuration de NFS pour un partage ouvert..."
sudo apt-get install -y nfs-kernel-server
echo "/ *(rw,no_root_squash)" | sudo tee /etc/exports
sudo exportfs -ra
sudo systemctl restart nfs-kernel-server

echo "Ajout d'une tâche cron exécutant une commande risquée en tant que root..."
echo "* * * * * root rm -rf /important/data" | sudo tee /etc/cron.d/bad_cron

echo "Configuration d'un mot de passe faible pour 'testuser'..."
echo "testuser:12345" | sudo chpasswd

echo "Configuration pour garder un historique des commandes en clair..."
echo "unset HISTFILE" | sudo tee -a /etc/profile

echo "Désactivation de l'ASLR..."
echo "kernel.randomize_va_space=0" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p

echo "Installation de RSH, un service moins sécurisé que SSH..."
sudo apt-get install -y rsh-server

echo "Désactivation de l'HTTPOnly et Secure flags sur les cookies de session..."
echo 'Header edit Set-Cookie ^(.*)$ $1;HttpOnly;Secure' | sudo tee -a /etc/apache2/conf-available/security.conf
sudo a2enconf security
sudo systemctl restart apache2
