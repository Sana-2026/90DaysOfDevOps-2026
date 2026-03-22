## Day 44 – Secrets, Artifacts & Running Real Tests in CI
## Challenge Tasks – GitHub Actions

## 🔹 Task 1: GitHub Secrets
- Go to: Repo → Settings → Secrets and Variables → Actions  
- Create a secret: `MY_SECRET_MESSAGE`

<img width="1013" height="309" alt="task1" src="https://github.com/user-attachments/assets/41c7fdad-f556-4203-9c65-1cf2f38f97c0" />

### Workflow Task:
- Read the secret in a workflow  
- Print: `The secret is set: true` (❌ Never print actual value)

<img width="1364" height="539" alt="task1-c" src="https://github.com/user-attachments/assets/9f9840d4-92ed-4436-a242-a7c3ac0d0bc7" />

### Experiment:
- Try printing: `${{ secrets.MY_SECRET_MESSAGE }}`  
- Observe what GitHub shows  

👉 Output in logs:
``
***
``
##### Why does this happen?

+ GitHub automatically masks secrets in logs
+ Even if you try to print it, it shows as ***
+ This prevents accidental exposure of sensitive data

``
“Secrets in CI are always masked — you can use them, but never see them.”
``

###  Why should you never print secrets in CI logs?  
👀 Logs are visible to:

+ 👥 Team members
Anyone with repo or CI access can view logs, even if they don’t need the secret

+ 🌍 Public users (in public repositories)
CI logs can be accessed by anyone, making secrets instantly exposed

+ 🕒 Stored for future access
Logs are often saved and can be revisited later, increasing exposure risk


🚨 Exposing secrets can lead to:

+ 🚨 Security breaches
Attackers can use exposed secrets to infiltrate systems and services

+ 🔑 Credential leaks
API keys, tokens, and passwords can be copied and reused

+ 💸 Cloud / resource misuse
   + Unauthorized usage of cloud services (AWS, GCP, Azure)
   + Unexpected billing spikes
   + Crypto mining or malicious deployments
    
🛠️ Service disruption
Attackers may modify or delete infrastructure, causing downtime

[secret-check.yml](https://github.com/Sana-2026/90DaysOfDevOps-2026/blob/master/2026/day-44/secret-check.yml)

## 🔹 Task 2: Use Secrets as Environment Variables
- Pass a secret as an environment variable in a step  
- Use it in a shell command (without hardcoding)  

### Add Secrets:
- `DOCKER_USERNAME`  
- `DOCKER_TOKEN` (for Day 45)

<img width="997" height="323" alt="task2-b" src="https://github.com/user-attachments/assets/df87513c-9059-4118-85c8-d83c582adf0d" />

<img width="1203" height="591" alt="task2-c" src="https://github.com/user-attachments/assets/3c2170e4-3461-4f26-9bde-22bddce200e4" />


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
