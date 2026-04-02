# Day 45 – Docker Build & Push in GitHub Actions

### Challenge Tasks
### Task 1: Prepare
Use the app you Dockerized on Day 36 - Used Bank AI app from day 36
Add the Dockerfile to your github-actions-practice repo 
Make sure DOCKER_USERNAME and DOCKER_TOKEN secrets are set from Day 44 added secrets for Bank AI repo

<img width="1021" height="582" alt="task1" src="https://github.com/user-attachments/assets/f5d47e85-fe34-4ebc-b034-66f0c944e50a" />
---

### Task 2: Build the Docker Image in CI
Create ``.github/workflows/docker-publish.yml`` that:

1. Triggers on push to``main``
2. Checks out the code
3. Builds the Docker image and tags it
Verify: Check the build step logs — does the image build successfully?
---

### Task 3: Push to Docker Hub

Add steps to:

1. Log in to Docker Hub using your secrets

2. Tag the image as username/repo:latest and also username/repo:sha-<short-commit-hash>

3. Push both tags
   
Verify: Go to Docker Hub — is your image there with both tags?

<img width="1366" height="620" alt="task2-c" src="https://github.com/user-attachments/assets/effc8d66-813e-44b7-ba85-2d09bdfa1e9f" />

<img width="1358" height="641" alt="task2-d" src="https://github.com/user-attachments/assets/dbe13bfb-d21e-46a2-a96b-7e66a9eb8480" />

<img width="1366" height="657" alt="task2-e" src="https://github.com/user-attachments/assets/ecb5b524-b879-4a10-af22-7254e91e00ea" />

<img width="1350" height="626" alt="task2" src="https://github.com/user-attachments/assets/7c1cee6c-f972-416c-8b20-70f494b3f4da" />

<img width="1340" height="627" alt="task2-b" src="https://github.com/user-attachments/assets/8990fa9d-ae76-4e79-afa4-ff2a95163324" />


[docker-publish.yml](https://github.com/Sana-2026/AI-BankApp-DevOps/tree/start/.github/workflows)

---

Task 4: Only Push on Main

Add a condition so the push step only runs on the main branch — not on feature branches or PRs.

Test it: push to a feature branch and verify the image is built but NOT pushed.

<img width="410" height="166" alt="task4" src="https://github.com/user-attachments/assets/4ab59493-8c25-4a97-96c8-7c6c56198f8d" />

<img width="1325" height="588" alt="task3" src="https://github.com/user-attachments/assets/4885fc92-857d-40d5-a6bb-f338b47ffeb0" />


---
Task 5: Add a Status Badge

1. Get the badge URL for your docker-publish workflow from the Actions tab
2. Add it to your README.md
3. Push — the badge should show green

<img width="971" height="136" alt="task5-a" src="https://github.com/user-attachments/assets/2d3cd6f7-784a-4d9d-b220-4c6490960910" />

<img width="1031" height="430" alt="task5" src="https://github.com/user-attachments/assets/ac035f52-2bdf-42dd-9032-b3c9197f8813" />

---
Task 6: Pull and Run It
1. On your local machine (or a cloud server), pull the image you just pushed
2. Run it
3. Confirm it works

<img width="1350" height="669" alt="task6" src="https://github.com/user-attachments/assets/61cb0b32-f547-4539-81b8-f863d675e0ea" />

Write in your notes: What is the full journey from git push to a running container?
```
YOU                    GITHUB                  DOCKER HUB           SERVER
───                    ──────                  ──────────           ──────
git push
    │
    ▼
code reaches
github
    │
    ▼
GitHub Actions
wakes up
(sees .yml file)
    │
    ▼
Spins up fresh
ubuntu machine
    │
    ▼
Checks out
your code
    │
    ▼
Sets up Java 21
    │
    ▼
mvn clean package
(builds .jar file)
    │
    ▼
docker build
(builds image)
    │
    ▼
Is this main?──No──→ STOP (don't push)
    │
   Yes
    │
    ▼
Login to
Docker Hub ────────────────────▶ authenticated
    │                                  │
    ▼                                  ▼
docker push ───────────────▶ image stored
both tags:                   sana2026/ai-bankapp:latest
latest                       sana2026/ai-bankapp:sha-abc123
sha-abc123
                                       │
                                       │
                             ──────────▼──────────
                             docker pull           │
                             sana2026/ai-bankapp   │
                                       │           │
                                       ▼           │
                             docker run -p 8080    │
                                       │           │
                                       ▼           │
                             container running  ◀──┘
                             on port 8080 🎉

```
