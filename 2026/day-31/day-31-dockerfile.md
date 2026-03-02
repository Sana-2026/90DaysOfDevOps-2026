## Challenge Tasks
## Task 1: Your First Dockerfile

1. Create a folder called ``bash my-first-image ``
1. Inside it, create a Dockerfile that:
 - Uses ubuntu as the base image
 - Installs curl
 - Sets a default command to print "Hello from my custom image!"
1. Build the image and tag it my-ubuntu:v1

<img width="1348" height="724" alt="first-dockerfile" src="https://github.com/user-attachments/assets/9415a17c-9481-47fc-913c-4912c707b546" />

1. Run a container from your image
   Verify: The message prints on docker run

<img width="1361" height="472" alt="docker-run-part1" src="https://github.com/user-attachments/assets/2b8082ac-2922-4bf0-a8ae-fee3dfd7ec35" />

<img width="1359" height="486" alt="docker-runpart2" src="https://github.com/user-attachments/assets/536929fd-c892-4609-bae9-73e957bd22f3" />

### 🐳 Docker Errors Faced 

❌ Error 1: [echo: not found
/bin/sh: 1: [echo: not found

Reason :

 - Image (my-ubuntu:v1) was built earlier with an incorrect CMD

 - Dockerfile was fixed later, but image was not rebuilt

 - Docker kept using the old broken image

Fix :

docker build -t my-ubuntu:v2 .
docker run my-ubuntu:v2

Key Learning :

Docker images are immutable — always rebuild after Dockerfile changes.

❌ Error 2: Container name already in use

Conflict. The container name "/first-container" is already in use

Reason :

 - A container named first-container already exists

 - Docker does not allow duplicate container names

Fix :

docker rm first-container
# or
docker run --name first-container-v2 my-ubuntu:v1

Key Learning :

Container names must be unique.


## Task 2: Dockerfile Instructions
### Create a new Dockerfile that uses all of these instructions:

* FROM — base image
* RUN — execute commands during build
* COPY — copy files from host to image
* WORKDIR — set working directory
* EXPOSE — document the port
* CMD — default command
Build and run it. Understand what each line does.

## Task 3: CMD vs ENTRYPOINT

1. Create an image with CMD ["echo", "hello"] — run it, then run it with a custom command. What happens?
1. Create an image with ENTRYPOINT ["echo"] — run it, then run it with additional arguments. What happens?
1. Write in your notes: When would you use CMD vs ENTRYPOINT?

## Task 4: Build a Simple Web App Image

1. Create a small static HTML file (index.html) with any content
2. Write a Dockerfile that:
* Uses nginx:alpine as base
* Copies your index.html to the Nginx web directory
* Build and tag it my-website:v1
* Run it with port mapping and access it in your browser

## Task 5: .dockerignore

1. Create a .dockerignore file in one of your project folders
1. Add entries for: node_modules, .git, *.md, .env
1. Build the image — verify that ignored files are not included

## Task 6: Build Optimization
1. Build an image, then change one line and rebuild — notice how Docker uses cache
1. Reorder your Dockerfile so that frequently changing lines come last
1. Write in your notes: Why does layer order matter for build speed?
