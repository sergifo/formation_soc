#### Création d'un réseau
```bash
docker network create --driver=bridge --subnet=172.20.0.0/16 spoofing_net 
```

 

#### Création des conteneurs host1, host2, host3
```bash
docker run -it -d --name host1 --network spoofing_net python bash
docker run -it -d --name host2 --network spoofing_net python bash
docker run -it -d --name host3 --network spoofing_net python bash
```

### Copie les applications dans le conteneur host1 et host3
```bash
docker cp send_spoofed.py host3:/send_spoofed.py
docker cp sniff_app.py host1:/sniff_app.py
```

### commmande pour install libpcap sur ubuntu
```bash
apt install -y libpcap0.8
```

### Commande pour ouvrir une communication ssh avec un conteneur en bash
```
docker exec -it host1 bash
```