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

### Task 3: Restart Policies

1.Add restart: always to your database service.

<img width="1363" height="696" alt="task3-part1" src="https://github.com/user-attachments/assets/c50566d1-3acc-42c2-9d29-a27b94a3744f" />


2. Manually kill the database container — does it come back?
   Yes the container comes back
   
   <img width="1367" height="339" alt="task3-part2" src="https://github.com/user-attachments/assets/eb942731-85ac-40b7-9d3c-71a935c5eeb6" />

4. Try restart: on-failure — how is it different?

``restart: on-failure``this policy means:

+ Restart the container only if it exits with a non-zero error code (failure).

+  ``docker kill`` sends SIGKILL (signal 9) to the container.

+ Docker treats this as an abnormal termination, so the container exits with a failure code.
so container ``restart: on-failure``

+ ``docker stop`` is considered a normal exit, not a failure.

   
<img width="1348" height="757" alt="task3-correct-a" src="https://github.com/user-attachments/assets/453c90d8-2430-4969-9e1f-1b0656b0f784" />

<img width="1363" height="725" alt="task3-correct-b" src="https://github.com/user-attachments/assets/7f741030-6bd1-454d-9a13-f22d967631ad" />

<img width="1364" height="724" alt="task3-correct-c" src="https://github.com/user-attachments/assets/1247a52b-0294-49bc-b952-36bf5aef5101" />


| Action | restart: on-failure |
|------|---------------------|
| `docker kill` | ✅ container restarts |
| container crash | ✅ container restarts |
| `docker stop` | ❌ container does NOT restart |

6. Write in your notes: When would you use each restart policy?

| Restart Policy | When to Use | Example Services |
|---------------|-------------|------------------|
| no | When you do not want the container to restart automatically. Useful for testing or debugging. | Temporary test containers |
| always | When the service must always stay running, even if the container crashes or Docker restarts. | Databases, Redis, Monitoring tools |
| on-failure | When the container should restart only if it crashes (non-zero exit code). It will not restart if stopped manually. | Web apps, APIs, workers |
| unless-stopped | Similar to `always`, but the container will not restart if it was manually stopped by the user. | Production services that should run continuously |

### Task 4: Custom Dockerfiles in Compose
1. Instead of using a pre-built image for your app, use build: in your compose file to build from a Dockerfile
   
2. Make a code change in your app
   
3. Rebuild and restart with one command

<img width="1364" height="699" alt="task4" src="https://github.com/user-attachments/assets/3c05b83b-175a-4d16-b33d-4075353a082d" />

### Task 5: Named Networks & Volumes
1. Define explicit networks in your compose file instead of relying on the default4
   
2. Define named volumes for database data
   
3. Add labels to your services for better organization
   
[docker-compose](https://github.com/Sana-2026/90DaysOfDevOps-2026/blob/master/2026/day-34/Demo-app/docker-compose.yml)

### Task 6: Scaling (Bonus)
1. Try scaling your web app to 3 replicas using docker compose up --scale
   
2. What happens? What breaks?
   
3.Write in your notes: Why doesn't simple scaling work with port mapping?


#### Scaling a Service with Docker Compose
Command Used

``docker compose up -d --scale web=3``

+ This command instructs Docker Compose to create 3 replicas of the web service.

+ Example containers created:

web-1
web-2
web-3

#### What Happens During Scaling

+ Docker successfully starts the first container.

+ When Docker attempts to start additional replicas, it encounters a port conflict.

+ The additional containers fail to start.

#### Typical error:

port is already allocated

#### Why This Happens

+ In the docker-compose.yml, the web service exposes a port like this:

ports:
  - "5001:5000"

This means:
 - Host Port	5001
 - Container Port	5000

#### When scaling occurs:

Container	Port Mapping  Attempt	  Result
web-1	    5001 → 5000	  Starts    successfully
web-2	    5001 → 5000	  Fails     (port already used)
web-3	    5001 → 5000	  Fails     (port already used)

A host port can only be bound to one container at a time, causing scaling to fail.

#### What Breaks

- Port binding conflict

- Only one replica becomes accessible

- Remaining replicas cannot start

- No traffic distribution between containers

#### Why Simple Scaling Doesn't Work with Port Mapping

- Simple scaling fails because:

- Host ports cannot be shared by multiple containers.

- Docker Compose does not automatically provide load balancing.

 - Each replica attempts to bind to the same host port.

#### How Production Systems Solve This

Production architectures use a reverse proxy or load balancer to distribute traffic across replicas.

Example architecture:
```
User Request
     │
     ▼
Load Balancer (Nginx / Traefik)
     │
 ┌───┴────┬─────┐
 ▼        ▼     ▼
web-1    web-2  web-3
```
The load balancer listens on a single host port and routes requests to multiple container replicas.

Key Takeaway

Simple container scaling with Docker Compose does not work when host port mapping is used, because multiple containers cannot bind to the same host port. A load balancer or reverse proxy is required to distribute traffic across scaled containers.

