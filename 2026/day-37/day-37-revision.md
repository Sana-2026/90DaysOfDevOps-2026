## Day 37 – Docker Revision & Cheat Sheet

### Self-Assessment Checklist
Mark yourself honestly — can do, shaky, or haven't done:

[ can do] Run a container from Docker Hub (interactive + detached)
[ can do] List, stop, remove containers and images
[ shaky] Explain image layers and how caching works
[ can do] Write a Dockerfile from scratch with FROM, RUN, COPY, WORKDIR, CMD
[ can do ] Explain CMD vs ENTRYPOINT
[can do ] Build and tag a custom image
[ Shaky ] Create and use named volumes
[ shaky ] Use bind mounts
[ shaky ] Create custom networks and connect containers
[ can do] Write a docker-compose.yml for a multi-container app
[can do ] Use environment variables and .env files in Compose
[ can do] Write a multi-stage Dockerfile
[ can do] Push an image to Docker Hub
[ can do] Use healthchecks and depends_on

Quick-Fire Questions
Answer from memory, then verify:
## Docker Interview Quick Revision (One-Line Answers)

**1. What is the difference between an image and a container?**  
➡ A **Docker image** is a read-only blueprint/template, while a **container** is a running instance of that image.

**2. What happens to data inside a container when you remove it?**  
➡ Data inside a container is **lost when the container is removed unless it is stored in volumes or bind mounts**.

**3. How do two containers on the same custom network communicate?**  
➡ Containers on the same custom network **communicate using container names as hostnames via Docker’s internal DNS**.

**4. What does `docker compose down -v` do differently from `docker compose down`?**  
➡ `docker compose down -v` **removes containers, networks, and volumes**, while `docker compose down` **removes only containers and networks**.

**5. Why are multi-stage builds useful?**  
➡ **Multi-stage builds reduce the final image size by copying only the required artifacts from build stages to the final image.**

**6. What is the difference between `COPY` and `ADD`?**  
➡ `COPY` **simply copies files from host to image**, while `ADD` **can also extract archives and download files from URLs**.

**7. What does `-p 8080:80` mean?**  
➡ It **maps port 8080 on the host machine to port 80 inside the container**.

**8. How do you check how much disk space Docker is using?**  
➡ Use the command **`docker system df`** to check Docker disk usage.




Build Your Docker Cheat Sheet

Create docker-cheatsheet.md organized by category:

Container commands — run, ps, stop, rm, exec, logs
Image commands — build, pull, push, tag, ls, rm
Volume commands — create, ls, inspect, rm
Network commands — create, ls, inspect, connect
Compose commands — up, down, ps, logs, build
Cleanup commands — prune, system df

Dockerfile instructions — FROM, RUN, COPY, WORKDIR, EXPOSE, CMD, ENTRYPOINT

Cheatsheet

Revisit Weak Spots

Pick 2 topics you marked as shaky and redo the hands-on tasks from that day.

Explain image layers and how caching works
Gained a clear understanding of Docker image layers and how caching works.

Explain CMD vs ENTRYPOINT
Understood the difference between CMD and ENTRYPOINT, where ENTRYPOINT defines the main executable and CMD provides default arguments that can be overridden at runtime.

