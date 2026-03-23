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
```
***
```

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
-  
<img width="1365" height="623" alt="task3" src="https://github.com/user-attachments/assets/2f41183d-b041-4290-881b-77ffbd7aae64" />

### Verify:
- After workflow runs → Go to Actions tab  
- Download the artifact  
- Confirm it is visible and accessible

 <img width="1358" height="631" alt="task3-b" src="https://github.com/user-attachments/assets/afba90c7-a125-4945-8ba8-0dfb70038dc9" />
 
<img width="1366" height="614" alt="task3-c" src="https://github.com/user-attachments/assets/641b4642-956b-4464-91ae-aa1312e32905" />


---

## 🔹 Task 4: Download Artifacts Between Jobs
### Job 1:
- Generate a file  
- Upload it as an artifact
- 
<img width="1306" height="475" alt="task4" src="https://github.com/user-attachments/assets/732cfb3d-37a5-45b1-b5d8-64a6787c94aa" />

### Job 2:
- Download the artifact  
- Print/use its contents
 
<img width="1314" height="583" alt="task4-a" src="https://github.com/user-attachments/assets/b8f6bf46-1519-4ee4-8dae-6f07bb0fa3f7" />

<img width="1365" height="598" alt="task4-c" src="https://github.com/user-attachments/assets/6974e0d1-fca2-4c3d-814c-deaf4f2ebd27" />

### Notes:
- When to use artifacts?
  
  ### 🧪 1. Test Reports
Use artifacts to store test outputs like:
- JUnit reports  
- Coverage reports  
- Logs  

👉 So you can **download and analyze them later**

---

### 📦 2. Build Outputs
When your pipeline creates files like:
- `.jar`, `.war` (Java apps)  
- `.exe` (Windows apps)  
- `.zip` packages  

👉 Store them as artifacts to **use in later jobs or download**

---

### 🔄 3. Sharing Between Jobs
If you have multiple jobs:
- Job 1 builds something  
- Job 2 needs that output  

👉 Use artifacts to **transfer files between jobs**

---

### 🐞 4. Debugging Failures
Save logs, screenshots, or error dumps  

👉 Helps you **debug after the workflow finishes**

---

### 📊 5. Reports & Analysis Files
Store generated:
- Performance reports  
- Security scan results  
- Lint results  

👉 So teams can **review them anytime**

---

## 🧠 One-Line Memory Trick
**Artifacts = Save files for later use (inside or after pipeline)**


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
- 
<img width="1366" height="654" alt="task5" src="https://github.com/user-attachments/assets/caa36742-215d-479c-a8b5-84384c8e2b2b" />

<img width="1366" height="588" alt="task5-b" src="https://github.com/user-attachments/assets/7bc43888-2e7d-4bf6-857d-40b34216268c" />

<img width="1354" height="622" alt="task6" src="https://github.com/user-attachments/assets/1f178c3e-4be4-49a2-b119-e4ccb773e0d8" />

[test-CI.yml](https://github.com/Sana-2026/90DaysOfDevOps-2026/tree/master/2026/day-44)
---

## 🔹 Task 6: Caching
- Use `actions/cache` to cache dependencies  

### Steps:
- Run workflow twice  
- Compare execution time

### First Run
<img width="1279" height="514" alt="task6-time-first" src="https://github.com/user-attachments/assets/6350ecba-8e18-4c6f-a903-a311e71549f0" />

<img width="1357" height="638" alt="task6-first-run" src="https://github.com/user-attachments/assets/0521ecf6-c9a9-4736-8df1-7833c645340e" />

### Second Run

<img width="1343" height="637" alt="task6-secondrun" src="https://github.com/user-attachments/assets/988a5b92-ea4a-4610-93b8-5d1f617a33a9" />


<img width="1357" height="608" alt="task6-cache" src="https://github.com/user-attachments/assets/702fc2fb-851e-4eb8-acda-badcb4098afb" />

[Test-CI-Cache.yml](https://github.com/Sana-2026/90DaysOfDevOps-2026/blob/master/2026/day-44/test-CI-cache)

### Notes:
#### 🔹 What is being cached?

When we use:

cache: 'pip'

👉 GitHub caches:

📦 Downloaded Python packages (used by pip)

📁 Files stored in:

~/.cache/pip
📌 Includes:
+ .whl files (pre-built packages)
+ Source files
+ Dependency metadata
🔹 Where is it stored?

🖥️ Inside the runner (temporary)

/home/runner/.cache/pip

☁️ GitHub Cloud (main storage)

+ Stored outside your repo
+ Managed by GitHub Actions
+ Linked with:
   + OS (ubuntu-latest)
   + Python version
   + requirements.txt

🔄 How caching works (Easy Flow)

1. 🔍 GitHub tries to find cache

2. ❌ If not found → installs dependencies normally

3. 💾 Cache gets saved after job

4. ⚡ Next run → cache is reused (faster)

❗ Important Points
1. ❌ Cache is NOT installed packages

2. ✅ Cache is only downloaded files

3. ❌ Not permanent (can be deleted by GitHub)

4. ✅ Used to speed up future runs

🧠 Easy Memory Trick

“Cache = downloads saved → faster installs later”

⚡ Simple Flow
pip install → download → cache saved → reuse next time
