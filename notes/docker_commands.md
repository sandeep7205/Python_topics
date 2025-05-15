
-------------------
Docker Commands
--- --- --- ---
-------------------
>>> docker -v || docker --version === docker version.
>>> docker images === list of images
>>> docker pull <image_name> [Eg: docker pull python || ubuntu || hello-world] === pull the latest version image from DOCKER-HUB. 
>>> docker pull <image_name>:<version> [Eg: docker pull python:3.11] === pull the mentioned version image from DOCKER-HUB. 
>>> docker run <image_id/image_name> [Eg: docker run python || ubuntu || hello-world] === create a new container from the image.
>>> docker run -it <image_id/image_name> [Eg: docker run -it python || ubuntu] ===  to download an image and create a new container from it in "Interactive Mode [to access the container from terminal]".
>>> docker ps === list of running containers
>>> docker ps -a === list of all containers
>>> docker start <container_id/container_name> === to start an existing container using it's id/name
>>> docker stop <container_id/container_name> === to stop an existing container using it's id/name
>>> docker restart <container_id/container_name> === to restart an existing container using it's id/name
>>> docker rm <container_id/container_name> === to remove a docker container [first stop the container]
>>> docker rmi <image_name> === to remove a docker image [first remove it's container]
>>> <image_name>:<version> === to download the specific verion from docker hub [command: pull/run]
>>> docker run -d <image_id/image_name> === create a new container from the image in "Detached Mode"
>>> docker run --name <container_name> -d <image_id/image_name> === create a new container with "custom name" from the image in "Detached Mode"
>>> docker run -p8080:3306 <image_id/image_name>  ==== "-p" is use for port binding the "Container Port[3306] with Host Port[8080]" 
>>> docker logs <container_id/container_name> === to check the container logs
>>> docker exec -it <container_id/container_name> /bin/bash ===  "exec" give access to run additional commands in the existing container by accessing it's bash.
>>> docker exec -it <container_id/container_name> /bin/sh ===  "exec" give access to run additional commands in the existing container by accessing it's shell.
>>> docker network create <network_name> === create a isolated space using "networks", where container can intearacts withouts any ports with eachothers inside the common network.
>>> docker network ls === list of networks with scopes
>>> docker rename <current_name_or_id> <new_name> === replacing <current_name_or_id> with the container's actual name or ID and <new_name> with the name you want to give it.
>>> docker exec -it <container_id/container_name> bash from the command line. It opens a terminal session directly into the running container.




-------------------
create a container
--- --- --- --- ---
Exapmple - Mongodb
--- --- --- --- ---
docker run -d \
-p27017:27017 \
--name mongo \
--network mongo_network
-e USERNAME=root \
-e PASSWORD=root\
mongo

>>> th above run the container from the image.





-------------------
Docker Image Layer
--- --- --- --- ---
>>> Image is consist of different layers
    Eg: -> Base Layer, Layer1, Layer2, .. [Read only layer]
      -> Container Layer

Port Binding
--- --- --- ---
>>> Every docker container having default port are binding with them realated to container
>>> docker run -p8080:3306 <image_id/image_name>  ==== "-p" is use for port binding the "Container Port[3306] with Host Port[8080]" 

-------------------


----------------------------------------------------------------------------------------------------
# Docker Note
-------------------
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon[desktop].
 2. The Docker daemon[desktop] pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon[desktop] created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon[desktop] streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

----------------------------------------------------------------------------------------------------


