## Day 30 – Docker Images & Container Lifecycle

### Challenge Tasks
### Task 1: Docker Images

1. Pull the nginx, ubuntu, and alpine images from Docker Hub

 <img width="922" height="645" alt="pulling-dock-images" src="https://github.com/user-attachments/assets/dedc5c6a-5ae8-44d9-b626-614990a5f9f7" />

1. List all images on your machine — note the sizes
   
<img width="836" height="274" alt="dock-images" src="https://github.com/user-attachments/assets/21daedc0-d12d-4ead-9882-1bc8b1e18fd1" />

1. Compare ubuntu vs alpine — why is one much smaller?
   
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
   
