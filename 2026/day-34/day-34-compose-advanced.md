# Day 34 – Docker Compose: Real-World Multi-Container Apps

### Challenge Tasks

### Task 1: Build Your Own App Stack

1. Create a docker-compose.yml for a 3-service stack:

2. A web app (use Python Flask, Node.js, or any language you know)

3. A database (Postgres or MySQL)

4. A cache (Redis)


<img width="1363" height="727" alt="task1" src="https://github.com/user-attachments/assets/9d184b9f-546d-4848-9820-1cce464c2762" />

### Task 2: depends_on & Healthchecks

1. Add depends_on to your compose file so the app starts after the database

  [docker-compose](https://github.com/Sana-2026/90DaysOfDevOps-2026/blob/master/2026/day-34/app-stack/docker-compose.yml)
 
3. Add a healthcheck on the database service

3.Use depends_on with condition: service_healthy so the app waits for the database to be truly ready, not just started

<img width="1364" height="722" alt="task2" src="https://github.com/user-attachments/assets/4436da89-966b-4305-97cc-775c43bee6f1" />


Test: Bring everything down and up — does the app wait for the DB?
yes

When containers start we will see:

1️⃣ db container starts
2️⃣ healthcheck runs pg_isready
3️⃣ DB becomes healthy
4️⃣ web container starts

Task 3: Restart Policies

Add restart: always to your database service

Manually kill the database container — does it come back?
Try restart: on-failure — how is it different?
Write in your notes: When would you use each restart policy?v
