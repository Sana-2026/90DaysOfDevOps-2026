## Day 43 – Jobs, Steps, Env Vars & Conditionals

### GitHub Actions Challenge Tasks

### Task 1: Multi-Job Workflow

Create `.github/workflows/multi-job.yml` with **3 jobs**:

- **build** — prints `"Building the app"`
- **test** — prints `"Running tests"`
- **deploy** — prints `"Deploying"`

### Requirements

- Make **test** run **only after build succeeds**
- Make **deploy** run **only after test succeeds**

**Verify:**  
Check the workflow graph in the **Actions** tab — does it show the dependency chain? yes it shows

---

<img width="1359" height="455" alt="task1" src="https://github.com/user-attachments/assets/d928c565-fc1e-4840-8cc2-3fd634ef7e2b" />



### Task 2: Environment Variables

In a **new workflow**, use environment variables at **3 levels**:

- **Workflow level** — `APP_NAME: myapp`
- **Job level** — `ENVIRONMENT: staging`
- **Step level** — `VERSION: 1.0.0`

Print all three in a **single step** and verify each is accessible.

<img width="1355" height="595" alt="task2-a" src="https://github.com/user-attachments/assets/32b19086-db81-4f16-a40f-652e0c0445bb" />


Then use a **GitHub context variable** to print:

- the **commit SHA**
- the **actor** (who triggered the run)

<img width="1343" height="497" alt="task2-b" src="https://github.com/user-attachments/assets/4940d26b-54ad-4a63-bb13-5330d8cf1281" />

---

### Task 3: Job Outputs

- Create a job that **sets an output** — for example, **today’s date as a string**
- Create a second job that **reads that output and prints it**
- Pass the value using `outputs:` and `needs.<job>.outputs.<name>`
- 
<img width="1346" height="497" alt="task3-a" src="https://github.com/user-attachments/assets/1087cb74-debc-4d22-ad6e-d2f04ac1f76c" />

<img width="1338" height="451" alt="task3-b" src="https://github.com/user-attachments/assets/2c35b64f-b392-4bb9-85b5-abae586d7bf6" />


**Write in your notes:**  
Why would you pass outputs between jobs?

> **To share data from one job to another in a workflow.**

---

#### 🧠 One-line memory

> **“One job produces → another job uses.”**

---

#### 🔥 Why it’s needed

- Jobs run **separately (isolated)**
- They **don’t share data automatically**
- Outputs act as a **bridge between jobs**

---

#### 📦 Simple examples

- Pass **build version** → use in deploy  
- Pass **Docker image tag** → push to registry  
- Pass **test result/status** → decide deployment  
- Pass **generated date/ID** → reuse later  

---

### Task 4: Conditionals

In a workflow, add:

- A **step** that only runs when the branch is `main`
- A **step** that only runs when the previous step failed
- A **job** that only runs on `push` events, not on pull requests
- A **step** with `continue-on-error: true`

<img width="1362" height="641" alt="task4-partb" src="https://github.com/user-attachments/assets/154d6986-039a-482a-8b4f-b2e334d30118" />

**Write in your notes:**  
What does `continue-on-error: true` do?

> **It allows a step to fail without stopping the workflow.**

---

#### 🧠 One-line memory

> **“Fail the step → but don’t fail the job.”**

---

#### 🔍 Normal behavior (without it)

```yaml
- name: Step
  run: exit 1


---
```
✅ With continue-on-error: true
- name: Step
  run: exit 1
  continue-on-error: true

👉 Now:

+ ❌ Step fails

+ ✅ Job continues

+ ✅ Next steps still run

🧃 Simple analogy

“Even if this step breaks, keep going.”

📦 When to use it

+ Non-critical checks

 + Optional steps (lint, warnings)

+ Experiments / debugging


### Task 5: Putting It Together

Create `.github/workflows/smart-pipeline.yml` that:

- Triggers on **push** to **any branch**
- Has a **lint** job and a **test** job running in parallel
- Has a **summary** job that runs after both
- Prints whether it is:
  - a **main branch push**, or
  - a **feature branch push**
- Prints the **commit message**
