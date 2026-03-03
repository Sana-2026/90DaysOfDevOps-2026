## Challenge Tasks
## Task 1: Your First Dockerfile

1. Create a folder called `` my-first-image ``
1. Inside it, create a  ``Dockerfile `` that:
 - Uses  ``ubuntu`` as the base image
 - Installs  ``curl ``
 - Sets a default command to print  ``"Hello from my custom image!" ``
1. Build the image and tag it  ``my-ubuntu:v1 ``

<img width="1348" height="724" alt="first-dockerfile" src="https://github.com/user-attachments/assets/9415a17c-9481-47fc-913c-4912c707b546" />

1. Run a container from your image
   Verify: The message prints on  ``docker run ``

<img width="1361" height="472" alt="docker-run-part1" src="https://github.com/user-attachments/assets/2b8082ac-2922-4bf0-a8ae-fee3dfd7ec35" />

<img width="1359" height="486" alt="docker-runpart2" src="https://github.com/user-attachments/assets/536929fd-c892-4609-bae9-73e957bd22f3" />

### 🐳 Docker Errors Faced and debugged

❌ Error 1: [echo: not found
 ``/bin/sh: 1: [echo: not found ``

Reason :

 - Image  ``(my-ubuntu:v1) `` was built earlier with an  ``incorrect CMD ``

 - Dockerfile was fixed later, but image was  ``not rebuilt ``

 - Docker kept using the old broken image

Fix :

docker build -t my-ubuntu:v2 .
docker run my-ubuntu:v2

Key Learning :

Docker images are  ``immutable — always rebuild after Dockerfile changes. ``

 ❌ Error 2: ``Wrong Dockerfile Name``

 Docker only auto-detects a file named exactly Dockerfile
(case-sensitive).

If the file is named incorrectly (e.g. DockerFile, dockerfile, Dockerfile-dev), Docker will fail to build unless explicitly     told which file to use.

Fix:

❌ Error 3:  ``Container name already in use ``

Conflict. The container name "/first-container" is already in use

Reason :

 - A container named first-container already exists

 - Docker does not allow  ``duplicate container names ``

Fix :

docker rm first-container
or
docker run --name first-container-v2 my-ubuntu:v1

Key Learning :

Container names must be unique.


## Task 2: Dockerfile Instructions

### Create a new Dockerfile that uses all of these instructions:

 *  ``FROM python:3.10-slim``                                This Dockerfile builds a lightweight Python image
*  ``RUN pip install --no-cache-dir -r requirements.txt``    Installs Python dependencies
*  ``COPY requirements.txt, app.py``                         Copies dependency file into the container
*  ``WORKDIR /app``                                          Sets /app as the working directory inside the container
*  ``EXPOSE ``— 5000                                         Documents that the app listens on port 5000
*  ``CMD ["python", "app.py"]``                              Runs the Python application when the container starts
  
 ``Build and run it. `` Understand what each line does.
 
<img width="1365" height="560" alt="task2-part1" src="https://github.com/user-attachments/assets/cdba5e51-9d00-4815-93b1-d638dbd1969d" />

<img width="1337" height="113" alt="task2-dockerrun" src="https://github.com/user-attachments/assets/7b50ba64-846c-40c0-a301-d173ab5d6eae" />

## Task 3: CMD vs ENTRYPOINT

1. Create an image with CMD ["echo", "hello"] — run it, then run it with a custom command. What happens?

 <img width="1352" height="484" alt="task3-part1" src="https://github.com/user-attachments/assets/d7c5ea89-a8e7-4ec7-8900-475775680ef0" />

### Run the Image Normally:

+ Docker uses the default CMD

+ So it runs: ``echo hello``

### Run the Image with a Custom Command :

+ ``CMD ["echo", "hello"]`` is the default command

+ When you pass a command at ``docker run,`` it overrides CMD

+ Docker now runs:

``echo "custom command"``

👉 The original CMD ["echo", "hello"] is ignored

1. Create an image with ENTRYPOINT ["echo"] — run it, then run it with additional arguments. What happens?
   
<img width="1384" height="618" alt="task3-part2" src="https://github.com/user-attachments/assets/be0f9e31-fd82-4742-a3c0-b88a93671048" />

### Runing the Image (No Arguments)
docker run cmd-test
<blank line>

+ echo runs with no arguments

+ echo just prints a newline

👉 ENTRYPOINT runs, but nothing is passed to it
   
1. Write in your notes: When would you use CMD vs ENTRYPOINT?

   ## CMD vs ENTRYPOINT — Quick Memory Table

| Aspect | CMD | ENTRYPOINT |
|------|-----|-----------|
| Purpose | Provides a default command | Defines the main executable |
| Overridden by `docker run` | ✅ Yes | ❌ No (unless `--entrypoint`) |
| User input treated as | New command | Arguments to the executable |
| Flexibility | High | Low (fixed behavior) |
| Best use case | Dev, utility, base images | Apps, CLIs, production services |
| Common example | `CMD ["bash"]` | `ENTRYPOINT ["nginx"]` |
| If both are used | CMD is replaced | ENTRYPOINT always runs |
| Interview memory line | “CMD is a default” | “ENTRYPOINT is mandatory” |

### One-Line Memory Trick
**CMD = suggestion | ENTRYPOINT = rule**

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
