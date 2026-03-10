# AI BankApp DevOps Project

A **production-style DevOps project** demonstrating how to build, containerize, and deploy a **Spring Boot Banking Application with MySQL using Docker and Docker Compose on AWS EC2**.

This project is designed to practice **real-world DevOps workflows**, including containerization, environment configuration, and multi-service orchestration.

---

# Project Overview

The **AI BankApp** is a simple banking application that supports:

* User registration and login
* Account management
* Transaction history
* Secure authentication using Spring Security
* Persistent storage using MySQL

The goal of this project is to learn how to **take an application from code → container → multi-container deployment**.

---

# Tech Stack

### Backend

* Java 21
* Spring Boot
* Spring Security
* Spring Data JPA
* Thymeleaf

### Database

* MySQL 8

### DevOps Tools

* Docker
* Docker Compose
* AWS EC2

### Monitoring

* Spring Boot Actuator
* Prometheus metrics endpoint

---

# Project Architecture

```
User Browser
      |
      | HTTP (Port 8083)
      v
Spring Boot Container
      |
      | Internal Docker Network
      v
MySQL Container
```

The application and database communicate through a **custom Docker network**.

---

# Project Structure

```
AI-BankApp-DevOps
│
├── src/
│   └── main/
│       ├── java/
│       └── resources/
│
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .env
│
├── TROUBLESHOOTING.md
└── README.md
```

---

# Phase 1 – Application Setup

The application includes:

* Spring Boot backend
* Thymeleaf frontend
* Spring Security authentication
* MySQL database integration
* Actuator metrics endpoint
* Externalized configuration via environment variables

---

# Phase 2 – Dockerization

The application is containerized using Docker.

Key Docker features used:

* Multi-stage build
* Non-root container user
* Small base image
* Docker ignore for optimized builds

Build the image:

```
docker build -t bankapp .
```

Run the container:

```
docker run -p 8083:8080 bankapp
```

---

# Phase 3 – Docker Compose Setup

Docker Compose is used to run the **application and database together**.

Services included:

* Spring Boot application
* MySQL database
* Persistent storage with Docker volumes
* Custom Docker network
* Environment variables from `.env`

Start the stack:

```
docker compose up --build
```

---

# Environment Configuration

Create a `.env` file in the project root.

```
APP_PORT=8083

MYSQL_HOST=mysql-db
MYSQL_PORT=3306

MYSQL_ROOT_PASSWORD=root123
MYSQL_DATABASE=bankappdb
MYSQL_USER=bankuser
MYSQL_PASSWORD=bankpass
```

These variables are used by both **Spring Boot and Docker Compose**.

---

# Access the Application

After starting containers:

```
http://<EC2-PUBLIC-IP>:8083
```

Example:

```
http://54.xxx.xxx.xxx:8083
```

---

# DevOps Concepts Demonstrated

This project demonstrates important DevOps practices:

* Containerizing applications with Docker
* Writing production-ready Dockerfiles
* Multi-container orchestration with Docker Compose
* Using environment variables for configuration
* Database persistence with Docker volumes
* Container networking
* Cloud deployment using EC2
* Systematic troubleshooting

---

Detailed troubleshooting steps are documented in:

```
TROUBLESHOOTING.md
```

---

# Future Improvements

Planned enhancements:

* CI/CD pipeline with GitHub Actions
* Push Docker image to Docker Hub
* Kubernetes deployment
* Monitoring with Prometheus and Grafana
* Infrastructure provisioning with Terraform

---

# Learning Outcome

Through this project, the following DevOps skills were developed:

* Writing production-grade Dockerfiles
* Building multi-container applications
* Debugging Docker networking issues
* Managing configuration using environment variables
* Deploying containerized applications on cloud servers

---

# Author

**Sana Shaik**

DevOps learner building hands-on projects to master modern cloud, container, and automation technologies.

---

# License

This project is for learning and educational purposes.

