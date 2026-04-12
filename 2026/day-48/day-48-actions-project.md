# Day 48 – GitHub Actions Project: End-to-End CI/CD Pipeline

## Challenge Tasks
## Task 1: Set Up the Project Repo
1. Create a new repo called ``github-actions-capstone`` (or use your existing ``github-actions-practice``)
2. Add a simple app — pick any one:
   + A Python Flask/FastAPI app with one endpoint
   + A Node.js Express app with one endpoint
   + Your Dockerized app from Day 36

3. Add a `Dockerfile`` and a basic test (even a script that curls the health endpoint counts)
4. Add a ``README.md`` with a project description

[README](https://github.com/Sana-2026/90DaysOfDevOps-2026/blob/master/2026/day-48/AI-Bankapp/README.md)


### Task 2: Reusable Workflow — Build & Test
Create `.github/workflows/reusable-build-test.yml`:
1. Trigger: `workflow_call`
2. Inputs: `python_version` (or `node_version`), `run_tests` (boolean, default: true)
3. Steps:
   - Check out code
   - Set up the language runtime
   - Install dependencies
   - Run tests (only if `run_tests` is true)
   - Set output: `test_result` with value `passed` or `failed`

This workflow does NOT deploy — it only builds and tests.

[reusable-build-test.yml](https://github.com/Sana-2026/AI-BankApp-DevOps/blob/start/.github/workflows/reusable-build-test.yml)

---

### Task 3: Reusable Workflow — Docker Build & Push

Create `.github/workflows/reusable-docker.yml`:
1. Trigger: `workflow_call`
2. Inputs: `image_name` (string), `tag` (string)
3. Secrets: `docker_username`, `docker_token`
4. Steps:
   - Check out code
   - Log in to Docker Hub
   - Build and push the image with the given tag
   - Set output: `image_url` with the full image path

[reusable-docker.yml](https://github.com/Sana-2026/AI-BankApp-DevOps/blob/start/.github/workflows/reusable-docker.yml)

---


### Task 4: PR Pipeline
Create `.github/workflows/pr-pipeline.yml`:
1. Trigger: `pull_request` to `main` (types: `opened`, `synchronize`)
2. Call the reusable build-test workflow:
   - Run tests: `true`
3. Add a standalone job `pr-comment` that:
   - Runs after the build-test job
   - Prints a summary: "PR checks passed for branch: `<branch>`"
4. Do **NOT** build or push Docker images on PRs

**Verify:** Open a PR — does it run tests only (no Docker push)?

---

