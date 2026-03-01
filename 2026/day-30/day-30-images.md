## Day 30 – Docker Images & Container Lifecycle

### Challenge Tasks
### Task 1: Docker Images

#### 1. Pull the nginx, ubuntu, and alpine images from Docker Hub

 <img width="922" height="645" alt="pulling-dock-images" src="https://github.com/user-attachments/assets/dedc5c6a-5ae8-44d9-b626-614990a5f9f7" />

#### 1. List all images on your machine — note the sizes
   
<img width="836" height="274" alt="dock-images" src="https://github.com/user-attachments/assets/21daedc0-d12d-4ead-9882-1bc8b1e18fd1" />

#### 1. Compare ubuntu vs alpine — why is one much smaller?

| Feature / Aspect        | Ubuntu Image                          | Alpine Image                         |
|-------------------------|---------------------------------------|--------------------------------------|
| Base Philosophy         | Full-featured Linux OS                | Minimal OS for containers            |
| Typical Image Size      | ~70–120 MB                            | ~5–15 MB                             |
| Disk Usage (Docker)     | High                                  | Very low                             |
| Default Shell           | bash                                  | ash (BusyBox)                        |
| Package Manager         | apt                                   | apk                                  |
| C Library (libc)        | glibc                                 | musl                                 |
| System Utilities        | Full GNU utilities                    | BusyBox (lightweight replacements)  |
| Startup Time            | Slower                                | Faster                               |
| Compatibility           | Very high (most binaries work)        | Limited (glibc binaries may fail)   |
| Learning & Debugging    | Easier                                | Harder (minimal tools)              |
| Security Surface        | Larger                                | Smaller                              |
| Best Use Case           | Learning, debugging, complex apps     | Microservices, CI/CD, production    |
| Popular Tag Example     | ubuntu:latest                         | alpine:latest                        |

#### Content Size  = compressed layer size
#### Disk Usage    = actual space on disk

#### 1. Inspect an image — what information can you see?

   #### Important `docker inspect` Fields – Easy to Remember

#### Id
- **Meaning:** Unique SHA identifier of the image  
- **Purpose:** Identifies the exact image version (immutable, never changes)

#### RepoTags
- **Meaning:** Image name and tag (e.g., `nginx:latest`)  
- **Purpose:** Provides a human-friendly way to reference the image

#### Created
- **Meaning:** Image build timestamp  
- **Purpose:** Helps check whether the image is recent or outdated

#### ExposedPorts
- **Meaning:** Ports declared by the image  
- **Purpose:** Indicates which ports the container is designed to use (not auto-published)

#### Env
- **Meaning:** Default environment variables  
- **Purpose:** Stores application configuration and software versions

#### Entrypoint
- **Meaning:** Main startup script or binary  
- **Purpose:** Ensures the container always starts in a defined way

#### Cmd
- **Meaning:** Default command arguments  
- **Purpose:** Defines what runs inside the container (can be overridden)

#### StopSignal
- **Meaning:** Signal sent when stopping the container  
- **Purpose:** Allows graceful application shutdown

#### Architecture
- **Meaning:** CPU architecture (e.g., amd64)  
- **Purpose:** Confirms hardware compatibility

#### Os
- **Meaning:** Operating system type  
- **Purpose:** Ensures the image runs on the correct OS

#### Size
- **Meaning:** Total image size  
- **Purpose:** Affects pull time and storage usage

#### RootFS (Layers)
- **Meaning:** Read-only filesystem layers  
- **Purpose:** Enables caching, sharing, and faster image downloads

---

#### Memory Flow (Quick Revision)
**Identity → Build Time → Network → Config → Startup → Shutdown → Compatibility → Size → Layers**
   
#### 1. Remove an image you no longer need

   <img width="1353" height="332" alt="dock-image-delete" src="https://github.com/user-attachments/assets/7854d8b0-2b3d-4111-a00c-852584758afd" />

### Task 2: Image Layers

#### 1. Run docker image history nginx — what do you see?
   
<img width="1263" height="401" alt="docker-image-history" src="https://github.com/user-attachments/assets/1c7737f9-1773-4756-a5c1-20a28704201e" />

###### Docker image history shows what command created which layer and how much size it added.

1️⃣ It shows layer-by-layer build history

Every line = one image layer

Layers are created by Dockerfile instructions (FROM, RUN, COPY, etc.)

2️⃣ Big SIZE = real disk usage

Large size rows usually come from:

RUN apt-get install ...

Installing packages

These layers increase image size

3️⃣ 0B size = metadata only

Commands like:

CMD

EXPOSE

ENV

STOPSIGNAL

Do not add files → size stays 0B




#### 1. Each line is a layer. Note how some layers show sizes and
some show 0B ?

| Docker Instruction | Why SIZE is 0B | Easy Way to Remember |
|-------------------|----------------|----------------------|
| CMD | Sets default command only | Run config, no files |
| ENTRYPOINT | Defines how container starts | Startup rule only |
| EXPOSE | Declares port | Info only, no data |
| ENV | Sets environment variables | Variables ≠ storage |
| LABEL | Adds metadata | Just tags |
| STOPSIGNAL | Defines stop signal | Signal config only |
| USER | Sets user | Permission info only |
| WORKDIR | Sets working directory | Path set, no files |

#### 1. Write in your notes: What are layers and why does Docker use them?

#### What are Docker Layers?

- A Docker layer is a read-only filesystem change created by each Dockerfile instruction.

- Every FROM, RUN, COPY, ADD → creates one layer

- Layers are stacked on top of each other

- Final image = collection of layers

#### Docker Layers

| Concept | Explanation | Easy Way to Remember |
|-------|-------------|----------------------|
| Docker Layer | A filesystem snapshot | One step = one layer |
| Layer Type | Read-only | Cannot be changed |
| Created By | Dockerfile instructions | RUN, COPY, ADD |
| Image | Stack of layers | Layers piled together |
| Container | Image + writable layer | One extra top layer |

#### Why Docker Uses Layers?

| Reason | Why It Matters | Real-Life Benefit |
|------|----------------|------------------|
| Reusability | Same layers reused | Saves disk space |
| Faster Builds | Unchanged layers cached | Faster `docker build` |
| Faster Pulls | Pull only missing layers | Less download |
| Version Control | Each change tracked | Easy rollback |
| Efficiency | No duplication | Lightweight images |

#### Read-only vs Writable Layer

| Layer Type | Description | Example |
|-----------|------------|--------|
| Image Layers | Read-only | Installed software |
| Container Layer | Writable | Logs, temp files |

### Task 3: Container Lifecycle

#### Practice the full lifecycle on one container:

1. Create a container (without starting it)
1. Start the container
1. Pause it and check status
1. Unpause it
1. Stop it
1. Restart it
1. Kill it
1. Remove it
   
1. Check docker ps -a after each step — observe the state changes.

<img width="1049" height="711" alt="container-lifecycle" src="https://github.com/user-attachments/assets/187c5c00-f99b-4afe-aebc-08563aadfcc2" />

### Task 4: Working with Running Containers

1. Run an Nginx container in detached mode
1. View its logs
1. View real-time logs (follow mode)

<img width="1077" height="724" alt="conatiner-detach-mode-logs" src="https://github.com/user-attachments/assets/03aae359-0e56-4f5c-81ee-6b034983c9c6" />

1. Exec into the container and look around the filesystem
   
<img width="1050" height="692" alt="docker-exec" src="https://github.com/user-attachments/assets/4c75a7ec-ddd9-4a10-bdb5-feab44a359e8" />

1. Run a single command inside the container without entering it.

<img width="862" height="671" alt="running-cmd-without-entering-container" src="https://github.com/user-attachments/assets/a0dad53b-43ce-41b3-b8a2-101528bfafe6" />

1. Inspect the container — find its IP address, port mappings, and mounts

<img width="1331" height="694" alt="docker-inspect-port" src="https://github.com/user-attachments/assets/79c7c6d6-9e52-451f-bf3a-ebea3232ce4b" />

<img width="1280" height="722" alt="container-inspect-ip" src="https://github.com/user-attachments/assets/58540b72-47fe-4bb7-b0ad-1e15c6b15baa" />

<img width="920" height="727" alt="docker-inspect-mount" src="https://github.com/user-attachments/assets/f39ae6fd-925c-4f1a-97b4-6dbd22b50bbb" />

## Task 5: Cleanup

1. Stop all running containers in one command
1. Remove all stopped containers in one command
1. Remove unused images
1. Check how much disk space Docker is using

<img width="1011" height="706" alt="task5" src="https://github.com/user-attachments/assets/40f915a2-b54c-4dca-9af5-8811a6f96051" />




   
