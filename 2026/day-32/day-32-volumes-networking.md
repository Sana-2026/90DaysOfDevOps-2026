# Day 32 – Docker Volumes & Networking

## Challenge Tasks
### Task 1: The Problem

1.Run a Postgres or MySQL container

2.Create some data inside it (a table, a few rows — anything)

<img width="1340" height="720" alt="task1-1-2" src="https://github.com/user-attachments/assets/02eabcd1-5e98-4ff8-815c-043c5cf50961" />

Stop and remove the container

<img width="1345" height="205" alt="task1-part3" src="https://github.com/user-attachments/assets/dddbdba7-e7d4-4152-8626-328eb257246c" />

Run a new one — is your data still there?

<img width="1319" height="522" alt="task1-part4" src="https://github.com/user-attachments/assets/ec91a12b-8597-4235-953a-0276f283f446" />

👉 testdb is missing
👉 Tables and rows are gone

Write what happened and why.

Docker containers are ephemeral (temporary).
When a container is removed, its writable layer is destroyed.
Since no volume was attached, PostgreSQL stored its data inside the container filesystem, which was deleted.


### Task 2: Named Volumes

Create a named volume
Run the same database container, but this time attach the volume to it
Add some data, stop and remove the container
Run a brand new container with the same volume
Is the data still there?
Verify: docker volume ls, docker volume inspect

### Task 3: Bind Mounts
Create a folder on your host machine with an index.html file
Run an Nginx container and bind mount your folder to the Nginx web directory
Access the page in your browser
Edit the index.html on your host — refresh the browser
Write in your notes: What is the difference between a named volume and a bind mount?

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

