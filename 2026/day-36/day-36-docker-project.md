## Day 36 – Docker Project: Dockerize a Full Application


### Challenge Tasks
### Task 1: Pick Your App

[App](https://github.com/Sana-2026/90DaysOfDevOps-2026/tree/master/2026/day-36/AI-BankApp)

For this task, I selected an existing project from my GitHub that does not yet have Docker support.

### Selected Application
**BankApp – Spring Boot Banking Application**

### Tech Stack
- Backend: Spring Boot
- Frontend: Thymeleaf
- Database: MySQL
- Security: Spring Security
- Monitoring: Spring Boot Actuator + Prometheus metrics

### Reason for Choosing This App
- It is a **multi-tier application** (frontend + backend + database)
- Ideal for learning **Docker containerization**
- Helps simulate **real-world DevOps workflows**
- Can be extended later with **CI/CD, Kubernetes, and monitoring**

### Goal
Dockerize the application and run it along with MySQL using **Docker Compose**.

### Task 2: Write the Dockerfile
1. Create a Dockerfile for your application
   
2. Use a multi-stage build if applicable
   
3. Use a non-root user
   
4. Keep the image small — use alpine or slim base images
   
5. Add a .dockerignore file
   
6. Build and test it locally.

[Dockerfile](https://github.com/Sana-2026/90DaysOfDevOps-2026/blob/master/2026/day-36/AI-BankApp/Dockerfile)

[.dockerignore](https://github.com/Sana-2026/90DaysOfDevOps-2026/blob/master/2026/day-36/AI-BankApp/.dockerignore)

### Task 3: Add Docker Compose

Write a docker-compose.yml that includes:

1. Your app service (built from Dockerfile)
   
2. A database service (Postgres, MySQL, MongoDB — whatever your app needs)
   
3. Volumes for database persistence
   
4. A custom network
   
5. Environment variables for configuration (use .env file)
   
6. Healthchecks on the database
   
7. Run docker compose up and verify everything works together.

[docker-compose.yml](https://github.com/Sana-2026/90DaysOfDevOps-2026/blob/master/2026/day-36/AI-BankApp/docker-compose.yml)

### Task 4: Ship It

1. Tag your app image
   
2. Push it to Docker Hub
   
3. Share the Docker Hub link

   [Docker hub](https://hub.docker.com/repository/docker/sana2026/ai-bankapp/general)
   
5. Write a README.md in your project with:
   
   + What the app does
   
   + How to run it with Docker Compose
 
   + Any environment variables needed

[README.md](https://github.com/Sana-2026/90DaysOfDevOps-2026/blob/master/2026/day-36/AI-BankApp/README.md)

### Task 5: Test the Whole Flow

1. Remove all local images and containers
   
2. Pull from Docker Hub and run using only your compose file
   
3. Does it work fresh? If not — fix it until it does

<img width="1365" height="590" alt="welcomepage" src="https://github.com/user-attachments/assets/1648a811-7b90-4493-845c-3d9749f7a778" />

<img width="1355" height="635" alt="dashboard-app" src="https://github.com/user-attachments/assets/4b53310e-f499-4bb5-b2f7-39fcc5718d5f" />

<img width="1361" height="639" alt="run-withdrawal" src="https://github.com/user-attachments/assets/784f310b-f79b-4f9f-8927-f6dcadc805d1" />



5. Challenges you faced and how you solved them

[troubleshooting.md](https://github.com/Sana-2026/90DaysOfDevOps-2026/blob/master/2026/day-36/AI-BankApp/troubleshooting.md)


