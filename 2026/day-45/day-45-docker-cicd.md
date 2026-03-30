# Day 45 – Docker Build & Push in GitHub Actions

### Challenge Tasks
### Task 1: Prepare
Use the app you Dockerized on Day 36 - Used Bank AI app from day 36
Add the Dockerfile to your github-actions-practice repo 
Make sure DOCKER_USERNAME and DOCKER_TOKEN secrets are set from Day 44 added secrets for Bank AI repo

<img width="1021" height="582" alt="task1" src="https://github.com/user-attachments/assets/f5d47e85-fe34-4ebc-b034-66f0c944e50a" />

### Task 2: Build the Docker Image in CI
Create ``.github/workflows/docker-publish.yml`` that:

1. Triggers on push to``main``
2. Checks out the code
3. Builds the Docker image and tags it
Verify: Check the build step logs — does the image build successfully?

### Task 3: Push to Docker Hub
Add steps to:

Log in to Docker Hub using your secrets
Tag the image as username/repo:latest and also username/repo:sha-<short-commit-hash>
Push both tags
Verify: Go to Docker Hub — is your image there with both tags?

<img width="1366" height="620" alt="task2-c" src="https://github.com/user-attachments/assets/effc8d66-813e-44b7-ba85-2d09bdfa1e9f" />

<img width="1358" height="641" alt="task2-d" src="https://github.com/user-attachments/assets/dbe13bfb-d21e-46a2-a96b-7e66a9eb8480" />

<img width="1366" height="657" alt="task2-e" src="https://github.com/user-attachments/assets/ecb5b524-b879-4a10-af22-7254e91e00ea" />

<img width="1350" height="626" alt="task2" src="https://github.com/user-attachments/assets/7c1cee6c-f972-416c-8b20-70f494b3f4da" />

<img width="1340" height="627" alt="task2-b" src="https://github.com/user-attachments/assets/8990fa9d-ae76-4e79-afa4-ff2a95163324" />


[docker-publish.yml](https://github.com/Sana-2026/AI-BankApp-DevOps/tree/start/.github/workflows)
