# 🚀 Challenge Tasks – GitHub Actions

## 🔹 Task 1: GitHub Secrets
- Go to: Repo → Settings → Secrets and Variables → Actions  
- Create a secret: `MY_SECRET_MESSAGE`  

### Workflow Task:
- Read the secret in a workflow  
- Print: `The secret is set: true` (❌ Never print actual value)  

### Experiment:
- Try printing: `${{ secrets.MY_SECRET_MESSAGE }}`  
- Observe what GitHub shows  

### Notes:
- Why should you never print secrets in CI logs?  
  - Secrets can be exposed publicly in logs  
  - Risk of security breaches and unauthorized access  

---

## 🔹 Task 2: Use Secrets as Environment Variables
- Pass a secret as an environment variable in a step  
- Use it in a shell command (without hardcoding)  

### Add Secrets:
- `DOCKER_USERNAME`  
- `DOCKER_TOKEN` (for Day 45)  

---

## 🔹 Task 3: Upload Artifacts
- Create a step that generates a file (e.g., log/test report)  

### Use:
- `actions/upload-artifact`  

### Verify:
- After workflow runs → Go to Actions tab  
- Download the artifact  
- Confirm it is visible and accessible  

---

## 🔹 Task 4: Download Artifacts Between Jobs
### Job 1:
- Generate a file  
- Upload it as an artifact  

### Job 2:
- Download the artifact  
- Print/use its contents  

### Notes:
- When to use artifacts?
  - Sharing files between jobs  
  - Storing build outputs or test reports  

---

## 🔹 Task 5: Run Real Tests in CI
- Add any script (Python/Shell) to repo  

### Workflow Steps:
- Checkout code  
- Install dependencies  
- Run the script  

### Expected Behavior:
- If script fails → Pipeline ❌ (red)  
- If script passes → Pipeline ✅ (green)  

### Practice:
- Intentionally break the script → see failure  
- Fix it → see success  

---

## 🔹 Task 6: Caching
- Use `actions/cache` to cache dependencies  

### Steps:
- Run workflow twice  
- Compare execution time  

### Notes:
- What is cached?
  - Dependencies (e.g., pip packages, node_modules)  
- Where is it stored?
  - GitHub’s cache storage (remote, tied to repo & key)  
