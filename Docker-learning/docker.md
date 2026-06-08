
# Command learn in docker learning 
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
