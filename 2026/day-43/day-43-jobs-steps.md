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
Check the workflow graph in the **Actions** tab — does it show the dependency chain?

---

### Task 2: Environment Variables

In a **new workflow**, use environment variables at **3 levels**:

- **Workflow level** — `APP_NAME: myapp`
- **Job level** — `ENVIRONMENT: staging`
- **Step level** — `VERSION: 1.0.0`

Print all three in a **single step** and verify each is accessible.

Then use a **GitHub context variable** to print:

- the **commit SHA**
- the **actor** (who triggered the run)

---

### Task 3: Job Outputs

- Create a job that **sets an output** — for example, **today’s date as a string**
- Create a second job that **reads that output and prints it**
- Pass the value using `outputs:` and `needs.<job>.outputs.<name>`

**Write in your notes:**  
Why would you pass outputs between jobs?

---

### Task 4: Conditionals

In a workflow, add:

- A **step** that only runs when the branch is `main`
- A **step** that only runs when the previous step failed
- A **job** that only runs on `push` events, not on pull requests
- A **step** with `continue-on-error: true`

**Write in your notes:**  
What does `continue-on-error: true` do?

---

### Task 5: Putting It Together

Create `.github/workflows/smart-pipeline.yml` that:

- Triggers on **push** to **any branch**
- Has a **lint** job and a **test** job running in parallel
- Has a **summary** job that runs after both
- Prints whether it is:
  - a **main branch push**, or
  - a **feature branch push**
- Prints the **commit message**
