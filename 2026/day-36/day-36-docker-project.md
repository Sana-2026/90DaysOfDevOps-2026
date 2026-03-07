## Day 36 – Docker Project: Dockerize a Full Application


### Challenge Tasks
### Task 1: Pick Your App

A 3-tier demo application using:

 + Web App (Flask)

+ Redis (Cache)

+ Database
  
#### Why I choose this project ?

- **Simple to build** – Flask is lightweight and beginner-friendly.
- **Real-world architecture** – Includes both application and database layers.
- **Learn container communication** – Practice how services interact in Docker.
- **Good for Docker Compose** – Helps manage multi-container applications.
- **Easy to extend** – Can later add Nginx, Redis, CI/CD, or Kubernetes.

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
