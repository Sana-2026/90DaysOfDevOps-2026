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

Install Docker on your machine (https://docs.docker.com/engine/install/)
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

```
  
