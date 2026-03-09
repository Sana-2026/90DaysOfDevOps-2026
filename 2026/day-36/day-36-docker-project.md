## Day 36 – Docker Project: Dockerize a Full Application


### Challenge Tasks
### Task 1: Pick Your App

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

Task 2: Write the Dockerfile
Create a Dockerfile for your application
Use a multi-stage build if applicable
Use a non-root user
Keep the image small — use alpine or slim base images
Add a .dockerignore file
Build and test it locally.

Task 3: Add Docker Compose
Write a docker-compose.yml that includes:

Your app service (built from Dockerfile)
A database service (Postgres, MySQL, MongoDB — whatever your app needs)
Volumes for database persistence
A custom network
Environment variables for configuration (use .env file)
Healthchecks on the database
Run docker compose up and verify everything works together.

Task 4: Ship It
Tag your app image
Push it to Docker Hub
Share the Docker Hub link
Write a README.md in your project with:
What the app does
How to run it with Docker Compose
Any environment variables needed
Task 5: Test the Whole Flow
Remove all local images and containers
Pull from Docker Hub and run using only your compose file
Does it work fresh? If not — fix it until it does
