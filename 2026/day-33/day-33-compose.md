# Day 33 – Docker Compose: Multi-Container Basics
### Challenge Tasks
### Task 1: Install & Verify

1. Check if Docker Compose is available on your machine
   
2. Verify the version

<img width="565" height="77" alt="task1" src="https://github.com/user-attachments/assets/73533b5b-c2a1-475d-823e-4d4eaade8468" />

### Task 2: Your First Compose File

1. Create a folder ``compose-basics``
   
2. Write a ``docker-compose.yml`` that runs a single Nginx container with port mapping

3. Start it with ``docker compose up``

4. Access it in your browser
   
5. Stop it with ``docker compose down``

[Docker Compose](https://github.com/Sana-2026/90DaysOfDevOps-2026/blob/master/2026/day-33/docker-compose.yml)

[Dockerfile](https://github.com/Sana-2026/90DaysOfDevOps-2026/blob/master/2026/day-33/Dockefi)

#### Case 1️⃣: Using an existing image ( Nginx example)

<img width="1357" height="712" alt="task2-part1-2-3" src="https://github.com/user-attachments/assets/b185d347-832a-4110-bdc8-4decb47a9cdb" />

<img width="1346" height="728" alt="task2-part4" src="https://github.com/user-attachments/assets/59a3d23e-1542-4d63-a60f-702709091f1f" />

<img width="1345" height="721" alt="task2-part5" src="https://github.com/user-attachments/assets/22f5e2ff-e375-4f60-a50f-96a30ce522d4" />

#### Case 2️⃣:Custom content 

<img width="1366" height="724" alt="task2-custom-index-docker-compse" src="https://github.com/user-attachments/assets/883f2a44-bf7d-4919-91bf-8405071d443d" />

<img width="1366" height="732" alt="docker-compose-down-custom-index" src="https://github.com/user-attachments/assets/69b7aada-b867-4385-b725-14b47f4dced0" />


### Task 3: Two-Container Setup

1.Write a docker-compose.yml that runs:

+ A ``WordPress`` container
+ A ``MySQL`` container

They should:

+ Be on the same network (Compose does this automatically)
+ MySQL should have a named volume for data persistence
+ WordPress should connect to MySQL using the service name
+ Start it, access WordPress in your browser, and set it up.

Verify: Stop and restart with docker compose down and docker compose up — is your WordPress data still there?

### Task 4: Compose Commands

Practice and document these:

Start services in detached mode
View running services
View logs of all services
View logs of a specific service
Stop services without removing
Remove everything (containers, networks)
Rebuild images if you make a change

### Task 5: Environment Variables
Add environment variables directly in your docker-compose.yml
Create a .env file and reference variables from it in your compose file
Verify the variables are being picked up
