**app** directory includes all files realted to the flask application
**static** directory is where assests such as images, CSS, and JavaScript files live
**templates** directory iw here you will putt the HTML templates
##Docker commands
- docker build \
docker build -t flaskapp:latest .


- docker -it flag \
Allows to interract with bin/bash or bin/sh o the container. That means now you have a bash session inside a container, so you can ls, mkdir, or do any bash commands inside the container\
docker run -it flaskapp /bin/sh

- go inside the container\
docker run -it flaskapp/bin/sh

- daemon mode\
-d is short for --detach which means you just run the container and then detach from it so basically you run container in the background.
