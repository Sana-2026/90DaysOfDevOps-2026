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

---
