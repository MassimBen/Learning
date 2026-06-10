
# Command learn in docker learning 

# Commande docker 

[Docker documentation officiel](https://docs.docker.com/reference)
## Base command docker 
```
## Afficher de l'aide
docker help
docker <sous-commande> --help

## Afficher des informations sur l'installation de Docker
docker --version
docker version
docker info

## Executer une image Docker
docker run hello-world

## Lister des images Docker
docker image ls
# ou
docker images

## Supprimer une image Docker
docker images rmi <IMAGE_ID ou IMAGE_NAME>  # si c'est le nom de l'image qui est spécifié alors il prendra par défaut le tag latest
    -f ou --force : forcer la suppression

## Supprimer tous les images Docker
docker rmi -f $(docker images -q)

## Rechercher une image depuis le Docker hub Registry
docker search ubuntu
    --filter "is-official=true" : Afficher que les images officielles

## Télécharger une image depuis le Docker hub Registry
docker pull <IMAGE_NAME>  # prendra par défaut le tag latest
docker pull ubuntu:16.04 # prendra le tag 16.04
```

## Other docker command
```
## Exécuter une image Docker
docker run <CONTAINER_ID ou CONTAINER_NAME>
    -t ou --tty : Allouer un pseudo TTY
    --interactive ou -i : Garder un STDIN ouvert
    --detach ou -d : Exécuter le conteneur en arrière-plan
    --name : Attribuer un nom au conteneur
    --expose: Exposer un port ou une plage de ports
    -p ou --publish : Mapper un port  "<PORT_CIBLE:PORT_SOURCE>"
    --rm : Supprimer automatiquement le conteneur quand on le quitte

## Lister des conteneurs en état running Docker
docker container ls
# ou
docker ps
    -a ou --all : Afficher tous les conteneurs peut-importe leur état

## Supprimer un conteneur Docker
docker rm <CONTAINER_ID ou CONTAINER_NAME>
    -f ou --force : forcer la suppression

## Supprimer tous les conteneurs Docker
docker rm -f $(docker ps -aq)

## Exécuter une commande dans un conteneur Docker
docker exec <CONTAINER_ID ou CONTAINER_NAME> <COMMAND_NAME>
    -t ou --tty : Allouer un pseudo TTY
    -i ou --interactive : Garder un STDIN ouvert
    -d ou --detach : lancer la commande en arrière plan

## sorties/erreurs d'un conteneur
docker logs <CONTAINER_ID ou CONTAINER_NAME>
    -f : suivre en permanence les logs du conteneur
    -t : afficher la date et l'heure de la réception de la ligne de log
    --tail <NOMBRE DE LIGNE> = nombre de lignes à afficher à partir de la fin (par défaut "all")
## Transformer un conteneur en image
docker commit <CONTAINER_NAME ou CONTAINER_ID> <NEW IMAGENAME>
    -a ou --author <string> : Nom de l'auteur (ex "John Hannibal Smith <hannibal@a-team.com>")
    -m ou --message <string> : Message du commit
```

## Build image

Create a dockerfile for example and use docker build to create a image

```
docker build -t mass/docker-learn/image_name:version
```
-t : it's tag you give to docker image otherwise it's a name

mass : it's username

docker-learn : it's the repository to put the image

image_name : name of image you create

version : the version of image


After build image you can push to your docker hub

```
docker push mass/docker-learn/image_name:version
```
Container is isolate environnement you can do task, you can run something like frontend of you page. You use multiple containers to run multiple think in web or something else.

Image like package you put you want in it for the thing to create and use a container to excute the image 

## what is image

```
docker search docker/welcome-to-docker : search a image welcome-to-docker in repository docker
docker pull docker/welcome-to-docker : dowloads the image from docker hub
docker image ls : list the image
docker image hitory docker/welcome-to-docker : list the history of image 
```

Image in docker can several layers for build it for dowload he dowload all layers.

```
docker tag name/dcker name/docker:1.0 : rename the docker image
docker push name/docker:1.0 : to push to docker hub repository
```
## Volume command

```
# Lister tous les volumes présents sur votre machine
docker volume ls

# Voir les détails techniques d'un volume (et voir où il est stocké sur l'hôte)
docker volume inspect nom_du_volume

# Supprimer un volume spécifique (Attention : supprime définitivement les données !)
docker volume rm nom_du_volume

# Nettoyer tous les volumes qui ne sont plus branchés à aucun conteneur
docker volume prune
```

## Compose command

```
# Lancer TOUS les services en arrière-plan
docker compose up -d

# Voir le statut des services lancés
docker compose ps

# Voir les logs en temps réel
docker compose logs -f

# Tout arrêter et nettoyer les conteneurs
docker compose down
```

# Architure of Docker file

- Determine your base image
  
-Install application dependencies

-Copy in any relevant source code and/or binaries

-Configure the final image

## Example Dockerfile

```
# 1. On part d'une image existante (légère)
FROM node:18-alpine

# 2. On crée et on se place dans le dossier de l'app dans le conteneur
WORKDIR /app

# 3. On copie les fichiers de configuration des dépendances
COPY package*.json ./

# 4. On installe les dépendances
RUN npm install

# 5. On copie le reste du code source de l'application
COPY . .

# 6. On expose le port de notre application
EXPOSE 3000

# 7. La commande exécutée au démarrage du conteneur
CMD ["npm", "start"]
```

```
# Construire l'image et lui donner le nom "mon-app"
docker build -t mon-app .

# Lancer le conteneur à partir de cette image
docker run -p 3000:3000 mon-app
```
```
# commit a new layer to exist layer
docker container commit -m "Add node" base-container node-base
```

Layer it's diffrentes thing you put to create image you for example app source, app dependencie, installation of python depenendicies.
