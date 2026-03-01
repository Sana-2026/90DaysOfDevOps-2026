## Day 30 – Docker Images & Container Lifecycle

### Challenge Tasks
### Task 1: Docker Images

1. Pull the nginx, ubuntu, and alpine images from Docker Hub

 <img width="922" height="645" alt="pulling-dock-images" src="https://github.com/user-attachments/assets/dedc5c6a-5ae8-44d9-b626-614990a5f9f7" />

1. List all images on your machine — note the sizes
   
<img width="836" height="274" alt="dock-images" src="https://github.com/user-attachments/assets/21daedc0-d12d-4ead-9882-1bc8b1e18fd1" />

1. Compare ubuntu vs alpine — why is one much smaller?

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

1. Inspect an image — what information can you see?

   ## Important `docker inspect` Fields – Easy to Remember

### Id
- **Meaning:** Unique SHA identifier of the image  
- **Purpose:** Identifies the exact image version (immutable, never changes)

### RepoTags
- **Meaning:** Image name and tag (e.g., `nginx:latest`)  
- **Purpose:** Provides a human-friendly way to reference the image

### Created
- **Meaning:** Image build timestamp  
- **Purpose:** Helps check whether the image is recent or outdated

### ExposedPorts
- **Meaning:** Ports declared by the image  
- **Purpose:** Indicates which ports the container is designed to use (not auto-published)

### Env
- **Meaning:** Default environment variables  
- **Purpose:** Stores application configuration and software versions

### Entrypoint
- **Meaning:** Main startup script or binary  
- **Purpose:** Ensures the container always starts in a defined way

### Cmd
- **Meaning:** Default command arguments  
- **Purpose:** Defines what runs inside the container (can be overridden)

### StopSignal
- **Meaning:** Signal sent when stopping the container  
- **Purpose:** Allows graceful application shutdown

### Architecture
- **Meaning:** CPU architecture (e.g., amd64)  
- **Purpose:** Confirms hardware compatibility

### Os
- **Meaning:** Operating system type  
- **Purpose:** Ensures the image runs on the correct OS

### Size
- **Meaning:** Total image size  
- **Purpose:** Affects pull time and storage usage

### RootFS (Layers)
- **Meaning:** Read-only filesystem layers  
- **Purpose:** Enables caching, sharing, and faster image downloads

---

### Memory Flow (Quick Revision)
**Identity → Build Time → Network → Config → Startup → Shutdown → Compatibility → Size → Layers**
   
1. Remove an image you no longer need

   <img width="1353" height="332" alt="dock-image-delete" src="https://github.com/user-attachments/assets/7854d8b0-2b3d-4111-a00c-852584758afd" />

### Task 2: Image Layers

1. Run docker image history nginx — what do you see?
   
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




1. Each line is a layer. Note how some layers show sizes and
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

1. Write in your notes: What are layers and why does Docker use them?

What are Docker Layers?

- A Docker layer is a read-only filesystem change created by each Dockerfile instruction.

- Every FROM, RUN, COPY, ADD → creates one layer

- Layers are stacked on top of each other

- Final image = collection of layers

### Docker Layers

| Concept | Explanation | Easy Way to Remember |
|-------|-------------|----------------------|
| Docker Layer | A filesystem snapshot | One step = one layer |
| Layer Type | Read-only | Cannot be changed |
| Created By | Dockerfile instructions | RUN, COPY, ADD |
| Image | Stack of layers | Layers piled together |
| Container | Image + writable layer | One extra top layer |

### Why Docker Uses Layers?

| Reason | Why It Matters | Real-Life Benefit |
|------|----------------|------------------|
| Reusability | Same layers reused | Saves disk space |
| Faster Builds | Unchanged layers cached | Faster `docker build` |
| Faster Pulls | Pull only missing layers | Less download |
| Version Control | Each change tracked | Easy rollback |
| Efficiency | No duplication | Lightweight images |

### Read-only vs Writable Layer

| Layer Type | Description | Example |
|-----------|------------|--------|
| Image Layers | Read-only | Installed software |
| Container Layer | Writable | Logs, temp files |

   
