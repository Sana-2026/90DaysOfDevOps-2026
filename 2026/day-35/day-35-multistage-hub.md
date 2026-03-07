# Day 35 – Multi-Stage Builds & Docker Hub

### Challenge Tasks
### Task 1: The Problem with Large Images

1. Write a simple Go, Java, or Node.js app (even a "Hello World" is fine)


2. Create a Dockerfile that builds and runs it in a single stage
   
3. Build the image and check its size
   
Note down the size — you'll compare it later.

Task 2: Multi-Stage Build
Rewrite the Dockerfile using multi-stage build:
Stage 1: Build the app (install dependencies, compile)
Stage 2: Copy only the built artifact into a minimal base image (alpine, distroless, or scratch)
Build the image and check its size again
Compare the two sizes
Write in your notes: Why is the multi-stage image so much smaller?

Task 3: Push to Docker Hub
Create a free account on Docker Hub (if you don't have one)
Log in from your terminal
Tag your image properly: yourusername/image-name:tag
Push it to Docker Hub
Pull it on a different machine (or after removing locally) to verify
Task 4: Docker Hub Repository
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
