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
1. Go to Docker Hub and check your pushed image.

<img width="1158" height="468" alt="docker-hub" src="https://github.com/user-attachments/assets/ebd59ffb-c3c0-4c09-948e-bd6e71fc7d3e" />

2. Add a description to the repository
   
3. Explore the tags tab — understand how versioning works

<img width="1365" height="564" alt="task4-1-2-3" src="https://github.com/user-attachments/assets/fa2e92a3-66cc-410c-83a8-525cc4f37294" />

   
5. Pull a specific tag vs latest — what happens

When pulling images from Docker Hub, you can pull either a specific tag or the latest tag.

#### Pulling a Specific Tag

``docker pull username/java-hello:v1``

#### What happens?

+ Docker downloads exactly that version of the image.

+ You always get the same image every time.

+ Useful for production and stable deployments.

Example:

``username/java-hello:v1``

If v1 was built months ago, Docker will still pull that exact image.

#### Pulling the latest Tag

``docker pull username/java-hello:latest``

#### What happens?

+ Docker pulls the image tagged as latest.

+ The latest tag can change whenever someone pushes a new image.

+ You may get different versions over time.

Example:

``username/java-hello:latest``

If a new image is pushed with the latest tag, pulling again will download the updated image.

Comparison Table
| Feature | Specific Tag (v1, v2) | latest Tag |
|-------|----------------|-------------|
| Version stability | Fixed | Can change |
| Reproducibility | High | Low |
| Recommended for production | Yes | No |
| Recommended for testing | Sometimes | Yes |

#### DevOps Best Practice 🚀

Always use specific version tags in production instead of latest.

### Task 5: Image Best Practices

Apply these to one of your images and rebuild:

1. Use a minimal base image (alpine vs ubuntu — compare sizes)
   
2.Don't run as root — add a non-root USER in your Dockerfile

3. Combine RUN commands to reduce layers
   
4. Use specific tags for base images (not latest)

 [Dockerfile](https://github.com/Sana-2026/90DaysOfDevOps-2026/blob/master/2026/day-35/java-app/Dockerfile-optimized-distroless)
 
Check the size before and after.

#### 1️⃣ Before Optimization (Typical Dockerfile)
``
FROM ubuntu:latest

WORKDIR /app

COPY HelloWorld.java .

RUN apt update
RUN apt install -y openjdk-17-jdk

RUN javac HelloWorld.java

CMD ["java","HelloWorld"]
``

#### Problems ❌

+ Uses large base image (Ubuntu)

+ Uses latest tag

+ Multiple RUN layers

+ Runs as root

+ Includes build tools in runtime

#### 2️⃣ Optimized Dockerfile (Applying All Best Practices)
``
# Stage 1: Build
FROM eclipse-temurin:17-jdk-alpine AS builder

WORKDIR /app
COPY HelloWorld.java .

RUN javac HelloWorld.java


# Stage 2: Runtime
FROM eclipse-temurin:17-jre-alpine

WORKDIR /app

# Create non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

COPY --from=builder /app/HelloWorld.class .

USER appuser

CMD ["java","HelloWorld"]
``
#### Advantages of the Optimized Docker Image

+ Smaller size – Minimal base images reduce storage usage.

+ Faster deployments – Smaller images pull and start quicker.

+ Better security – Running as a non-root user reduces risk.

+ Fewer vulnerabilities – Minimal packages mean a smaller attack surface.

+ Consistent builds – Specific image tags ensure reproducible environments.

