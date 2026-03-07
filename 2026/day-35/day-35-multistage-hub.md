# Day 35 – Multi-Stage Builds & Docker Hub

### Challenge Tasks
### Task 1: The Problem with Large Images

1. Write a simple Go, Java, or Node.js app (even a "Hello World" is fine)

2. Create a Dockerfile that builds and runs it in a single stage
   
3. Build the image and check its size
   
Note down the size — you'll compare it later.

<img width="1370" height="700" alt="task1" src="https://github.com/user-attachments/assets/72389d5f-dd04-4eb3-a668-25e526b4f00f" />

### Task 2: Multi-Stage Build
1. Rewrite the Dockerfile using multi-stage build:
   
   + Stage 1: Build the app (install dependencies, compile)
   + Stage 2: Copy only the built artifact into a minimal base image (alpine, distroless, or scratch)

2. Build the image and check its size again

   + compare the two sizes

| Build Type | Contains | Approx Image Size |
|-------------|-----------|------------------|
| Single Stage Build | JDK + Compiler + Source Code + Build Tools | 300MB – 600MB |
| Multi-Stage Build | Only Runtime (JRE) + Compiled Artifact | 80MB – 150MB |
| Multi-Stage with Alpine | Minimal Runtime + Compiled Artifact | 40MB – 90MB |
| Multi-Stage with Distroless | Only Application + Minimal Runtime | 30MB – 50MB |

<img width="1370" height="726" alt="task2" src="https://github.com/user-attachments/assets/7eba4515-31d0-49b2-b7c0-c393eef11f43" />

     
3. Write in your notes: Why is the multi-stage image so much smaller?

Multi-stage builds reduce image size by separating the build environment from the runtime environment.

##### 1️⃣ Build tools are not included in the final image

In the first stage, we use a full image with tools like:

+ JDK

+ Compiler (javac)

+ Build dependencies

These are only needed to compile the application, not to run it.

##### 2️⃣ Only the compiled artifact is copied

In the second stage, we copy only the final output:

``HelloWorld.class``

instead of copying:
```
Java source code
Build tools
Temporary files
Package managers
```

This keeps the final image clean and lightweight.

##### 3️⃣ Smaller runtime base image

The runtime stage uses a minimal image such as:

+ Alpine

+ Distroless

+ JRE-only images

These contain just enough to run the application, not to build it.

##### 4️⃣ Reduced attack surface (Security benefit) 🔒

Since build tools and extra packages are removed:

+ fewer vulnerabilities

+ fewer unnecessary binaries

+ more secure production container
   
   

### Task 3: Push to Docker Hub

1. Create a free account on ``Docker Hub`` .

2. Log in from your terminal.
   
3. Tag your image properly: yourusername/image-name:tag
   
4. Push it to Docker Hub
   
5. Pull it on a different machine (or after removing locally) to verify
   
### Task 4: Docker Hub Repository
Go to Docker Hub and check your pushed image
Add a description to the repository
Explore the tags tab — understand how versioning works
Pull a specific tag vs latest — what happens?
Task 5: Image Best Practices
Apply these to one of your images and rebuild:

Use a minimal base image (alpine vs ubuntu — compare sizes)
Don't run as root — add a non-root USER in your Dockerfile
Combine RUN commands to reduce layers
Use specific tags for base images (not latest)
Check the size before and after.

Hints
