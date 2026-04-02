# Day 46 – Reusable Workflows & Composite Actions

### Challenge Tasks

### Task 1: Understand workflow_call

**1. What is a reusable workflow?**

A reusable workflow in GitHub Actions is:

👉 A workflow that you write once and can call from other workflows or repositories, just like a function.

**Reusable workflow** = a full CI/CD pipeline you can reuse anywhere

**⚙️ Key Idea**

A reusable workflow:

+ Lives in .github/workflows/
+ Uses on: workflow_call
+ Accepts inputs (like function parameters)
+ Can be used by multiple repos

**Reusable workflow**
```
on:
  workflow_call:
```

**Called from another workflow**

```
jobs:
  use-it:
    uses: owner/repo/.github/workflows/file.yml@main
```


**2. What is the workflow_call trigger?**

👉 workflow_call is a trigger that allows one workflow to be called by another workflow.

**workflow_call** = “This workflow is reusable and can be invoked like a function”

⚙️ **How it works**

Normally, workflows run on events like:

+ push
+ pull_request

But when you use:
```
on:
  workflow_call:
```
👉 You are saying:

“Don’t run automatically — run only when another workflow calls me”

**Reusable workflow**
```
on:
  workflow_call:
```

**Calling workflow**
```
jobs:
  call-job:
    uses: ./.github/workflows/reusable.yml

```

**3. How is calling a reusable workflow different from using a regular action (uses:)?**

#### 🔁 Calling a Reusable Workflow vs Using a Regular Action

#### 🔁 1. Calling a Reusable Workflow

📞 **How you call it:**

```
jobs:
  build:
    uses: owner/repo/.github/workflows/docker.yml@main
```

**What it does:**

+ Runs complete workflow
+ Can have multiple jobs
+ Controls full CI/CD pipeline

#### ⚙️ 2. Using a Regular Action

**How you use it:**
```
steps:
  - uses: actions/checkout@v3

```
**💡 What it does:**

1. Runs single task
2. Used inside a job

**📌 Example tasks:**

+ Checkout code
+ Login to Docker
+ Setup Node.js

#### Comparison

| Feature   | Reusable Workflow       | Action             |
| --------- | ----------------------- | ------------------ |
| Level     | 🔥 Full pipeline (jobs) | ⚙️ Single step     |
| Called in | `jobs.<job>.uses`       | `steps[].uses`     |
| Contains  | Jobs + Steps            | Only steps / logic |
| Use case  | Reuse CI/CD pipelines   | Reuse small tasks  |
| Example   | Build + Test + Deploy   | Checkout, Login    |


 
**4. Where must a reusable workflow file live?**

👉 A reusable workflow must be stored inside:

``.github/workflows/``

If it’s not inside ``.github/workflows/`` → it cannot be called as a reusable workflow

**🔁 Why this matters**

+ GitHub only recognizes workflows from this directory
+ Required for workflow_call to work
+ Other workflows reference this exact path when calling it

---

Task 2: Create Your First Reusable Workflow

Create ``.github/workflows/reusable-build.yml``:

1.Set the trigger to``workflow_call``

2.Add an ``inputs``: section with:
   + ``app_name`` (string, required)
   + ``environment`` (string, required, default: ``staging``)
     
3.Add a ``secrets``: section with:
  + ``docker_token`` (required)

4. Create a job that:
  + Checks out the code
  + Prints Building <app_name> for <environment>
  + Prints Docker token is set: true (never print the actual secret)

**Verify**: This file alone won't run — it needs a caller. That's next.

---


