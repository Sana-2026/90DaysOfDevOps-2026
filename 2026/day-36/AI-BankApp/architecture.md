# ARCHITECTURE.md – AI BankApp DevOps Project

This document explains the **architecture of the AI BankApp DevOps project** and how different components interact with each other.

---

# 1. High Level Architecture

```
User Browser
      |
      | HTTP Request
      v
AWS EC2 Instance
      |
      | Port 8083
      v
Spring Boot Application Container
      |
      | Internal Docker Network
      v
MySQL Database Container
      |
      v
Docker Volume (Persistent Storage)
```

---

# 2. Components Explanation

## 1. User Browser

The user accesses the application using a web browser.

Example:

```
http://<EC2-PUBLIC-IP>:8083
```

Requests are sent to the **EC2 instance hosting the Docker containers**.

---

# 2. AWS EC2 Instance

The EC2 instance acts as the **host machine** running Docker.

Responsibilities:

* Runs Docker Engine
* Runs Docker Compose
* Hosts application containers
* Exposes port **8083** to the internet

---

# 3. Spring Boot Application Container

The application container contains the **BankApp backend and frontend**.

Technology used:

* Java 21
* Spring Boot
* Spring Security
* Spring Data JPA
* Thymeleaf

Container behavior:

```
Host Port 8083 → Container Port 8080
```

Spring Boot runs internally on **port 8080**.

---

# 4. MySQL Database Container

A separate container runs the MySQL database.

Responsibilities:

* Store user accounts
* Store transactions
* Provide persistent data storage

The application connects to MySQL using the service name:

```
mysql-db:3306
```

Because both containers are on the same Docker network.

---

# 5. Docker Network

Docker Compose automatically creates a **custom bridge network**.

Example:

```
bankapp-net
```

This network allows containers to communicate using **service names instead of IP addresses**.

Example:

```
Spring Boot → mysql-db:3306
```

---

# 6. Docker Volume

A Docker volume is used to **persist database data**.

Example volume:

```
mysql-data
```

Purpose:

* Prevent data loss when containers restart
* Store MySQL data outside the container filesystem

---

# 3. Deployment Flow

Deployment steps:

1. Build the application image

```
docker build -t bankapp .
```

2. Start containers with Docker Compose

```
docker compose up --build
```

3. Docker creates:

* Application container
* MySQL container
* Custom network
* Persistent volume

4. Application becomes accessible at:

```
http://<EC2-PUBLIC-IP>:8083
```

---

# 4. Environment Configuration

Configuration values are stored in a `.env` file.

Example:

```
APP_PORT=8083
MYSQL_HOST=mysql-db
MYSQL_PORT=3306
MYSQL_DATABASE=bankappdb
MYSQL_USER=bankuser
MYSQL_PASSWORD=bankpass
```

This allows **environment-specific configuration without modifying code**.

---

# 5. Security Considerations

The project includes several security best practices:

* Running container with **non-root user**
* Using **environment variables for credentials**
* Isolating services using **Docker networks**

---

# 6. Future Architecture Improvements

Planned DevOps improvements:

* CI/CD pipeline with GitHub Actions
* Docker image push to Docker Hub
* Kubernetes deployment
* Monitoring using Prometheus and Grafana
* Infrastructure as Code using Terraform

---

# 7. Architecture Summary

The project follows a **modern containerized architecture**:

* Application and database separated into containers
* Services communicate through Docker network
* Data stored in persistent volumes
* Deployment managed using Docker Compose

This architecture closely resembles **real-world DevOps deployment patterns used in production environments**.
