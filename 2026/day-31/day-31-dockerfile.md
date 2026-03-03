# Day 31 – Dockerfile: Build Your Own Images

## Challenge Tasks
## Task 1: Your First Dockerfile

1. Create a folder called `` my-first-image ``
2. Inside it, create a  ``Dockerfile `` that:
 - Uses  ``ubuntu`` as the base image
 - Installs  ``curl ``
 - Sets a default command to print  ``"Hello from my custom image!" ``
3. Build the image and tag it  ``my-ubuntu:v1 ``

<img width="1348" height="724" alt="first-dockerfile" src="https://github.com/user-attachments/assets/9415a17c-9481-47fc-913c-4912c707b546" />

4. Run a container from your image
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

2. Create an image with ENTRYPOINT ["echo"] — run it, then run it with additional arguments. What happens?
   
<img width="1384" height="618" alt="task3-part2" src="https://github.com/user-attachments/assets/be0f9e31-fd82-4742-a3c0-b88a93671048" />

### Runing the Image (No Arguments)
docker run cmd-test
<blank line>

+ echo runs with no arguments

+ echo just prints a newline

👉 ENTRYPOINT runs, but nothing is passed to it
   
3. Write in your notes: When would you use CMD vs ENTRYPOINT?

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

<img width="593" height="232" alt="image" src="https://github.com/user-attachments/assets/7519fab8-bdd6-4ad2-a53b-adf770a0b751" />

2. Write a Dockerfile that:
* Uses nginx:alpine as base
* Copies your index.html to the Nginx web directory

<img width="1345" height="556" alt="task4-part1" src="https://github.com/user-attachments/assets/e0e3343d-6d56-44e3-b748-9ee5ca4ab0c8" />

* Build and tag it my-website:v1
  
<img width="1360" height="586" alt="task4-build" src="https://github.com/user-attachments/assets/e21cbac0-5493-4ef7-93a2-82869b48af50" />

* Run it with port mapping and access it in your browser
  
<img width="1058" height="697" alt="task4-app-run-on-browser" src="https://github.com/user-attachments/assets/f543dc4b-0374-4c78-8992-51036eb3e45d" />


## Task 5: .dockerignore

1. Create a .dockerignore file in one of your project folders
2. Add entries for: node_modules, .git, *.md, .env
    
<img width="1372" height="677" alt="task5-part1" src="https://github.com/user-attachments/assets/3574af92-5d5b-4751-a8c7-5c9063019986" />

3. Build the image — verify that ignored files are not included

<img width="778" height="71" alt="task5-part3" src="https://github.com/user-attachments/assets/e51d308a-af56-427f-8bf9-981a4b5420c3" />

+ node_modules, .git, any .md files, and .env are not present.

+ index.html or required files are present.


## Task 6: Build Optimization

1. Build an image, then change one line and rebuild — notice how Docker uses cache
   
<img width="1345" height="728" alt="task6-part1" src="https://github.com/user-attachments/assets/f890ff45-ea9e-46e7-81c6-c7173d333720" />
👉 Docker reused unchanged layers and rebuilt only what changed.

2. Reorder your Dockerfile so that frequently changing lines come last

❌ Bad order (slow builds)

FROM nginx:alpine
COPY . /usr/share/nginx/html/

Any file change → entire COPY layer invalidated

✅ Good order (fast builds)
FROM nginx:alpine

#### Copy only static / less-changing files first
COPY nginx.conf /etc/nginx/nginx.conf

#### Copy frequently changing content LAST
COPY index.html /usr/share/nginx/html/

Now:

* Changing index.html → only last layer rebuilds

* Everything above stays cached

1. Write in your notes: Why does layer order matter for build speed?

+ Docker builds images layer by layer and caches each layer.
+ If a layer changes, all layers after it are rebuilt.
+ By placing frequently changing instructions (COPY source code, config, HTML) at the end of the Dockerfile.
+ Docker can reuse cached layers above them, resulting in faster builds, less CPU usage, and smaller rebuild times.
