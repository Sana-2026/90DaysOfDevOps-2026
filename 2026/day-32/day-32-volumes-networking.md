# Day 32 – Docker Volumes & Networking

## Challenge Tasks
### Task 1: The Problem

1.Run a Postgres or MySQL container

2.Create some data inside it (a table, a few rows — anything)

<img width="1340" height="720" alt="task1-1-2" src="https://github.com/user-attachments/assets/02eabcd1-5e98-4ff8-815c-043c5cf50961" />

3. Stop and remove the container

<img width="1345" height="205" alt="task1-part3" src="https://github.com/user-attachments/assets/dddbdba7-e7d4-4152-8626-328eb257246c" />

4. Run a new one — is your data still there?

<img width="1319" height="522" alt="task1-part4" src="https://github.com/user-attachments/assets/ec91a12b-8597-4235-953a-0276f283f446" />

👉 testdb is missing
👉 Tables and rows are gone

5. Write what happened and why.

+ Docker containers are ephemeral (temporary).
+ When a container is removed, its writable layer is destroyed.
+ Since no volume was attached, PostgreSQL stored its data inside the container filesystem, which was deleted.

### Task 2: Named Volumes

1. Create a named volume
   
<img width="1370" height="717" alt="task2-vol-part1" src="https://github.com/user-attachments/assets/d0a7f9c6-787d-441d-9928-d39ea817d2a0" />

#### 📌 Encountered PostgreSQL Docker Volume Issue (18+)

+ From PostgreSQL 18 onward, Docker images changed how database data is stored.

+ Data is now kept in version-specific directories (e.g. /var/lib/postgresql/18/data).

+ Mounting a volume to /var/lib/postgresql/data (old path) causes PostgreSQL to fail and exit.

+ Correct approach: mount the volume at /var/lib/postgresql, and let PostgreSQL manage subdirectories.

         #### ✅ Step-by-step FIX 
         
         1️⃣ Remove old container and volume
         
         2️⃣ Create volume again
         
         3️⃣ Run Postgres with CORRECT mount path
         
         4️⃣ Verify container is running
         
         5️⃣ Connect and test persistence

2. Run the same database container, but this time attach the volume to it

3. Add some data, stop and remove the container

<img width="1370" height="643" alt="task2-vol-post-error-part1" src="https://github.com/user-attachments/assets/3b218319-c835-4cf8-b3c0-c28516d15917" />

<img width="1271" height="320" alt="task2-vol-part3" src="https://github.com/user-attachments/assets/a2e105ab-8dd1-46e4-8478-daee27d7d558" />


4.Run a brand new container with the same volume

<img width="1357" height="393" alt="task2-vol-part4" src="https://github.com/user-attachments/assets/a6751d20-6169-4347-a9ab-7a5388b48437" />
 
5.Is the data still there?

Verify: docker volume ls, docker volume inspect
🎉 Data is still there.

+ Yes, the data is still there because the container was using a named volume, which persists beyond the container lifecycle.
  
<img width="1341" height="404" alt="task2-vol-final" src="https://github.com/user-attachments/assets/4fd7254d-6ec8-4151-bea9-5753c8843630" />


### Task 3: Bind Mounts
1. Create a folder on your host machine with an index.html file

2. Run an Nginx container and bind mount your folder to the Nginx web directory

3. Access the page in your browser

<img width="1354" height="718" alt="task3-bind-mount123" src="https://github.com/user-attachments/assets/c2aafd48-f954-4147-8b5a-9c857e6c660f" />

4. Edit the index.html on your host — refresh the browser

<img width="1365" height="725" alt="task3-bind-mount4" src="https://github.com/user-attachments/assets/0f105a0d-704a-4792-9a3b-c3e9e0a0b40b" />

5. Write in your notes: What is the difference between a named volume and a bind mount?

| Feature | Named Volume | Bind Mount |
|------|-------------|-----------|
| Managed by Docker | ✅ Yes | ❌ No (managed by host) |
| Storage location | Docker-controlled path (`/var/lib/docker/volumes/`) | Any directory on host |
| Host path visibility | Hidden from user | Fully visible & accessible |
| Ease of use | Very easy | Needs correct host path |
| Best for | Databases, persistent app data | Live code, config files |
| Portability | High (works across systems) | Low (path differs per host) |
| Risk of accidental change | Low | High (host edits affect container instantly) |
| Performance | Optimized by Docker | Depends on host filesystem |
| Backup & restore | Easy with Docker tools | Manual (host-level) |
| Typical example | Postgres/MySQL data | Nginx `index.html`, source code |

### Task 4: Docker Networking Basics
List all Docker networks on your machine
Inspect the default bridge network
Run two containers on the default bridge — can they ping each other by name?
Run two containers on the default bridge — can they ping each other by IP?

### Task 5: Custom Networks
Create a custom bridge network called my-app-net
Run two containers on my-app-net
Can they ping each other by name now?
Write in your notes: Why does custom networking allow name-based communication but the default bridge doesn't?

### Task 6: Put It Together
Create a custom network
Run a database container (MySQL/Postgres) on that network with a volume for data
Run an app container (use any image) on the same network
Verify the app container can reach the database by container name

