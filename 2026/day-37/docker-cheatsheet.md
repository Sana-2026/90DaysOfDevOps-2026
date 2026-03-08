# Docker Cheat Sheet 🐳

A quick reference guide for commonly used Docker commands, organized by category.

---

# Container Commands

| Command | Description |
|-------|-------------|
| `docker run IMAGE` | Create and start a container from an image |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers (running + stopped) |
| `docker stop CONTAINER` | Stop a running container |
| `docker rm CONTAINER` | Remove a container |
| `docker exec -it CONTAINER COMMAND` | Run a command inside a running container |
| `docker logs CONTAINER` | View container logs |

---

# Image Commands

| Command | Description |
|-------|-------------|
| `docker build -t IMAGE_NAME .` | Build an image from a Dockerfile |
| `docker pull IMAGE` | Download an image from Docker Hub |
| `docker push IMAGE` | Upload an image to a registry |
| `docker tag SOURCE_IMAGE TARGET_IMAGE` | Tag an image for a repository |
| `docker images` | List local images |
| `docker rmi IMAGE` | Remove an image |

---

# Volume Commands

| Command | Description |
|-------|-------------|
| `docker volume create VOLUME_NAME` | Create a volume |
| `docker volume ls` | List volumes |
| `docker volume inspect VOLUME_NAME` | Show volume details |
| `docker volume rm VOLUME_NAME` | Remove a volume |

---

# Network Commands

| Command | Description |
|-------|-------------|
| `docker network create NETWORK_NAME` | Create a network |
| `docker network ls` | List networks |
| `docker network inspect NETWORK_NAME` | Show network details |
| `docker network connect NETWORK_NAME CONTAINER` | Connect container to a network |

---

# Docker Compose Commands

| Command | Description |
|-------|-------------|
| `docker compose up` | Start services defined in compose file |
| `docker compose down` | Stop and remove services |
| `docker compose ps` | List running compose services |
| `docker compose logs` | View logs of services |
| `docker compose build` | Build services defined in compose file |

---

# Cleanup Commands

| Command | Description |
|-------|-------------|
| `docker system prune` | Remove unused containers, networks, and images |
| `docker system prune -a` | Remove all unused images and containers |
| `docker volume prune` | Remove unused volumes |
| `docker network prune` | Remove unused networks |
| `docker system df` | Show Docker disk usage |

---

🚀 **Tip:** Use `--help` with any command for more details.  
Example: `docker run --help`
