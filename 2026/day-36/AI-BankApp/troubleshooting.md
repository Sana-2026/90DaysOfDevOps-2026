# TROUBLESHOOTING.md – AI BankApp DevOps Project

This document records the **real troubleshooting steps performed while deploying the Spring Boot + MySQL BankApp using Docker and Docker Compose on an EC2 instance**.

It also serves as a **reference guide for debugging containerized applications in the future**.

---

# 1. Application Not Visible in Browser

## Problem

The application was not accessible from the browser.

```
http://<EC2-PUBLIC-IP>:8083
```

The browser showed **connection failure or no response**.

---

# 2. Checking Running Containers

First step in debugging any Docker deployment.

```
docker ps
```

Purpose:

* Verify containers are running
* Confirm port mapping
* Ensure services started successfully

If containers are not running, inspect logs.

---

# 3. Inspecting Application Logs

To check whether the Spring Boot application started successfully:

```
docker logs <app-container-name>
```

Observed logs:

```
Tomcat initialized with port 8080
Tomcat started on port 8080
Started BankappApplication
```

### Conclusion

The application started successfully but was running on **port 8080 inside the container**.

---

# 4. Port Mapping Issue

Original Docker Compose configuration:

```
ports:
  - "8083:8083"
```

### Problem

Spring Boot default port:

```
8080
```

Therefore, the container had nothing listening on port **8083**.

This resulted in:

```
curl: (56) Recv failure: Connection reset by peer
```

---

# 5. Fixing Port Mapping

Updated docker-compose configuration:

```
ports:
  - "8083:8080"
```

Meaning:

```
EC2 Host Port 8083 → Container Port 8080
```

Now the browser requests correctly reach the application.

---

# 6. Restarting Containers

After modifying the compose file, containers were restarted.

```
docker compose down
docker compose up --build
```

Purpose:

* Stop existing containers
* Rebuild images
* Apply new configuration

---

# 7. Testing Application Locally on EC2

Before opening the browser, verify locally.

```
curl localhost:8083
```

If the application responds, it confirms:

* Docker networking is working
* The application is reachable from the host

---

# 8. Database Connection Verification

From application logs:

```
HikariPool-1 - Start completed
Hibernate: create table accounts
Hibernate: create table transactions
```

Meaning:

* MySQL container started successfully
* Spring Boot connected to the database
* Tables were created automatically

---

# 9. MySQL Container Errors

### Error

```
MYSQL_USER="root", MYSQL_USER and MYSQL_PASSWORD are for configuring a regular user and cannot be used for the root user
```

### Cause

The `.env` file incorrectly set:

```
MYSQL_USER=root
```

MySQL Docker image does not allow creating the root user this way.

### Fix

Updated `.env` file:

```
MYSQL_ROOT_PASSWORD=root123
MYSQL_DATABASE=bankappdb
MYSQL_USER=bankuser
MYSQL_PASSWORD=bankpass
```

---

# 10. Port Already in Use

### Error

```
failed to bind host port 3306: address already in use
```

### Cause

The EC2 host already had MySQL running on port **3306**.

### Fix

Removed host port exposure for MySQL.

Original:

```
ports:
  - "3306:3306"
```

Updated:

```
(no port mapping required)
```

Containers communicate internally through Docker network.

---

# 11. Undefined Volume Error

### Error

```
service "mysql-db" refers to undefined volume mysql-data
```

### Cause

Volume used in service but not declared.

### Fix

Add volume definition:

```
volumes:
  mysql-data:
```

---

# 12. Environment Variables Missing

### Warning

```
MYSQL_PORT variable is not set
MYSQL_DATABASE variable is not set
```

### Cause

`.env` file was missing.

### Fix

Create `.env` file in project root.

```
APP_PORT=8083
MYSQL_HOST=mysql-db
MYSQL_PORT=3306
MYSQL_ROOT_PASSWORD=root123
MYSQL_DATABASE=bankappdb
MYSQL_USER=bankuser
MYSQL_PASSWORD=bankpass
```

---

# 13. Cleaning Docker Environment

Sometimes old containers or networks cause issues.

Cleanup commands used:

```
docker compose down -v
docker system prune -a
docker network prune
```

Purpose:

* Remove stopped containers
* Remove unused images
* Reset Docker environment

---

# 14. Useful Debug Commands

### Check running containers

```
docker ps
```

### Check container logs

```
docker logs <container>
```

### Inspect container ports

```
docker port <container>
```

### Test application locally

```
curl localhost:<port>
```

### Stop containers

```
docker compose down
```

---

# 15. Final Working Setup

```
Browser
   |
   | HTTP (Port 8083)
   v
Spring Boot Container
Port 8080
   |
   v
MySQL Container
Port 3306
```

Both containers communicate using a **custom Docker network**.

---

# 16. DevOps Debugging Workflow

When an application is not accessible:

1. Check containers

```
docker ps
```

2. Inspect logs

```
docker logs <container>
```

3. Verify port mapping

```
docker port <container>
```

4. Test locally

```
curl localhost:<port>
```

5. Verify firewall or security group settings

Following this structured approach helps identify deployment problems quickly.

---

# Final Result

The application is successfully accessible via browser:

```
http://<EC2-PUBLIC-IP>:8083
```

The deployment now includes:

* Spring Boot application container
* MySQL database container
* Docker Compose orchestration
* Persistent database storage
* Environment-based configuration
