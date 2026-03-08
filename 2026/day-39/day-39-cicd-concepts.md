Challenge Tasks
Task 1: The Problem
Think about a team of 5 developers all pushing code to the same repo manually deploying to production.

Write in your notes:

What can go wrong?
What does "it works on my machine" mean and why is it a real problem?
How many times a day can a team safely deploy manually?
Task 2: CI vs CD
Research and write short definitions (2-3 lines each):

Continuous Integration — what happens, how often, what it catches
Continuous Delivery — how it's different from CI, what "delivery" means
Continuous Deployment — how it differs from Delivery, when teams use it
Write one real-world example for each.

Task 3: Pipeline Anatomy
A pipeline has these parts — write what each one does:

Trigger — what starts the pipeline
Stage — a logical phase (build, test, deploy)
Job — a unit of work inside a stage
Step — a single command or action inside a job
Runner — the machine that executes the job
Artifact — output produced by a job
Task 4: Draw a Pipeline
Draw a CI/CD pipeline for this scenario:

A developer pushes code to GitHub. The app is tested, built into a Docker image, and deployed to a staging server.

Include at least 3 stages. Hand-drawn and photographed is perfectly fine.

Task 5: Explore in the Wild
Open any popular open-source repo on GitHub (Kubernetes, React, FastAPI — pick one you know)
Find their .github/workflows/ folder
Open one workflow YAML file
Write in your notes:
What triggers it?
How many jobs does it have?
What does it do? (best guess)

