# Utiliser l'image PHP avec Apache
FROM php:7.4-apache

# Copier les fichiers de l'application dans le répertoire web
COPY ./src/ /var/www/html/

# Définir les permissions correctes
RUN chown -R www-data:www-data /var/www/html \
    && chmod -R 755 /var/www/html

# Exposer le port 80
EXPOSE 80
