## Day 29 – Introduction to Docker

### Challenge Tasks
### Task 1: What is Docker?
#### 🧱 1a. What is a Container?

A container is a lightweight, portable unit that packages:

* your application

* all its dependencies (libraries, binaries)

* runtime

* basic system tools

…into one isolated environment so the app runs the same everywhere.

Think of it like this 👇

📦 “If it runs on my laptop, it will run exactly the same on the server.”

Containers are created and managed using tools like Docker.

Tools like Docker and Kubernetes made this the industry standard.

#### 1b. Containers vs Virtual Machines — what's the real difference?

##### Containers vs Virtual Machines (VMs)

🔹 Core Idea

* Virtual Machine → Virtualizes hardware

* Container → Virtualizes the operating system

 | Feature        | Containers       | Virtual Machines |
| -------------- | ---------------- | ---------------- |
| OS Required    | ❌ No separate OS | ✅ Full Guest OS|
| Boot Time      | Seconds ⚡        | Minutes ⏳      |
| Resource Usage | Very low         | High             |
| Performance    | Near-native      | Slower           |
| Isolation      | Process-level    | Hardware-level   |
| Image Size     | MBs              | GBs              |
| Scalability    | Very fast        | Slow             |
| Portability    | Excellent        | Limited          |


##### 🚀 Why Containers Are Preferred Today

✔ Faster deployments

✔ Lower infrastructure cost

✔ Perfect for microservices

✔ CI/CD friendly

✔ Cloud-native

When Should You Use Virtual Machines?

Use VMs when:

- You need different OS kernels (Linux + Windows together)

- Strong security isolation is required

- Running legacy applications

- Compliance-heavy environments

VMs are managed using hypervisors like VMware or VirtualBox.


##### 🧠 Real-World Analogy

🏠 VM → Renting a full house (own kitchen, bathroom, electricity)

🏢 Container → Renting a room in a shared apartment

#### 1c. What is the Docker architecture? (daemon, client, images, containers, registry)

#### 🏗️ Docker Architecture 

Docker follows a Client–Server architecture.

Main components:

- Docker Client

- Docker Daemon

- Docker Images

- Docker Containers

- Docker Registry

All of this is part of Docker.

1️⃣ Docker Client

This is what we use.

Examples:

docker build
docker pull
docker run

👉 The client does not do the work itself.
👉 It sends requests to the Docker Daemon using REST APIs.

2️⃣ Docker Daemon (dockerd)

This is the brain of Docker.

Responsibilities:

- Builds images

- Runs containers

- Manages networks & volumes

- Communicates with registries

- Runs in the background on the host machine.

3️⃣ Docker Images

🖼️ A Docker Image is:

A read-only template

Contains app code + dependencies + instructions

Images are built using a Dockerfile.

📌 Images are the blueprint → containers are the running version.

4️⃣ Docker Containers

📦 A container is:

A running instance of an image

- Lightweight & isolated

- Shares host OS kernel

- We can:

    * Start

    * Stop

    * Delete

    * Restart containers anytime

5️⃣ Docker Registry

🗂️ Stores Docker images.

Types:

- Public registry → Docker Hub

- Private registries (AWS ECR, GCR, Azure ACR)

Commands:

docker pull nginx
docker push myimage:latest

🖼️ Docker Architecture Diagram

<img width="879" height="873" alt="mermaid-diagram" src="https://github.com/user-attachments/assets/eae5e7a9-e7f9-442a-a487-8a2c6ce44441" />


### Task 2: Install Docker

1. Install Docker on your machine (https://docs.docker.com/engine/install/)
```bash
# Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo apt update
sudo systemctl status docker
sudo systemctl start docker

sudo usermod -aG docker $USER
newgrp docker

```

  2. Verify the installation
 
<img width="704" height="566" alt="task1-ques2-correct" src="https://github.com/user-attachments/assets/ff79633e-c55f-4039-9dfd-532804f0b4b8" />

3. Run the hello-world container
   
<img width="837" height="400" alt="helloworld-docker" src="https://github.com/user-attachments/assets/70638c74-5e31-42e3-8225-d18cef864eed" />

4. Read the output carefully — it explains what just happened

   To generate this message, Docker took the following steps:
   
 -  The Docker client contacted the Docker daemon.
  
 -  The Docker daemon pulled the "hello-world" image from the Docker Hub.
   
 -  The Docker daemon created a new container from that image which runs the
    executable that produces the output we are currently reading.
    
 -  The Docker daemon streamed that output to the Docker client, which sent it
    to our terminal.

### Task 3: Run Real Containers

1. Run an Nginx container and access it in your browser

  ###### docker run -d -p 80:80 nginx <EC2 port 80>:<container port 80>
  
<img width="1051" height="557" alt="welcome-nginx" src="https://github.com/user-attachments/assets/afb1a7a4-2bdb-4da5-bde6-da07790d1984" />

2. Run an Ubuntu container in interactive mode —

   ###### docker run -it ubuntu

<img width="936" height="141" alt="ubuntu" src="https://github.com/user-attachments/assets/c606ae15-65ca-48d4-bdb6-5d0a99591d4a" />
  ##### cat /etc/os-release
  
<img width="870" height="313" alt="etc-s-release" src="https://github.com/user-attachments/assets/4edc43db-5a7a-4ac8-9529-63d45059b393" />

3. List all running containers: docker ps
   
<img width="798" height="128" alt="docker-ps-command" src="https://github.com/user-attachments/assets/8f535250-b27b-4ed4-ac9d-7920e75eb42f" />

4. List all containers (including stopped ones): docker ps -a

   <img width="1218" height="206" alt="docker-ps-a" src="https://github.com/user-attachments/assets/68b6461e-a1e4-4bc9-b9ee-de572b8c2e33" />

5. Stop and remove a container: docker stop && docker rm
   
 <img width="1335" height="346" alt="stopping-removing-cont" src="https://github.com/user-attachments/assets/a842e0a0-4521-4972-a6a9-7f844c3d221a" />

### Task 4: Explore

1. Run a container in detached mode : detach mode run containers in background mode : docker run -d httpd
   
<img width="823" height="255" alt="detach-mode-container" src="https://github.com/user-attachments/assets/2b2e8f02-07dc-4758-8d13-92bcb360ef52" />

2. Give a container a custom name :
   
<img width="777" height="137" alt="container-name" src="https://github.com/user-attachments/assets/0190ff13-ada5-4fb9-82d8-cc2e3e6d49c8" />

3. Map a port from the container to your host: docker run -d --name mysql-db -p 3306:3306 mysql
   
<img width="738" height="297" alt="port-mapping-container-host" src="https://github.com/user-attachments/assets/b241c86e-1d76-48d7-ac71-2db8c4c8cb7f" />

4. Check logs of a running container: docker logs

<img width="1339" height="203" alt="docker-logs" src="https://github.com/user-attachments/assets/c0791015-b892-496d-acce-14238c591eec" />

5. Run a command inside a running container : docker exec -it <container-ID> bash

<img width="1154" height="432" alt="cmd-exec-inside-running-container" src="https://github.com/user-attachments/assets/a2ab340b-78e0-476b-9809-560a34a2d14f" />

