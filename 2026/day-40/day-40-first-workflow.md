## Day 40 – Your First GitHub Actions Workflow

### Challenge Tasks

### Task 1: Set Up

1. Create a new public GitHub repository called github-actions-practice.

2. Clone it locally
   
3.Create the folder structure: .github/workflows/

<img width="1017" height="437" alt="git-action-practice" src="https://github.com/user-attachments/assets/c9141e45-8d9b-478b-8094-443dbeb4b427" />

<img width="985" height="602" alt="task1" src="https://github.com/user-attachments/assets/e71081fc-0b1a-4455-8b0a-e0d3ce2321d5" />

<img width="1305" height="509" alt="task1-2" src="https://github.com/user-attachments/assets/68f7981f-7c2a-489b-8943-b34f7da76a7c" />

### Task 2: Hello Workflow

Create .github/workflows/hello.yml with a workflow that:

1. Triggers on every push
2. Has one job called greet
3. Runs on ubuntu-latest
4. Has two steps:
    + Step 1: Check out the code using actions/checkout
    + Step 2: Print Hello from GitHub Actions!

Push it. Go to the Actions tab on GitHub and watch it run.

Verify: Is it green? Click into the job and read every step.

Yes it is green workflow was succesfull.

<img width="1287" height="603" alt="task-2-part1" src="https://github.com/user-attachments/assets/22de0338-f09e-43b5-a546-4be9f0a9edc3" />

<img width="1264" height="600" alt="task2" src="https://github.com/user-attachments/assets/855f9eec-d8d7-4c65-8335-17850ca59644" />


### Task 3: Understand the Anatomy

####  GitHub Actions Workflow Key Concepts

| Key | Purpose |
|-----|--------|
| `on:` | Defines the event that triggers the workflow (e.g., push, pull_request, schedule). |
| `jobs:` | A workflow is made up of one or more jobs. Jobs run in parallel by default. |
| `runs-on:` | Specifies the operating system/environment where the job will run (e.g., ubuntu-latest, windows-latest). |
| `steps:` | A job contains a sequence of steps that execute commands or actions. |
| `uses:` | Used to run a pre-built action from the GitHub Marketplace (e.g., actions/checkout). |
| `run:` | Executes a shell command directly in the runner environment. |
| `name:` (step) | Gives a readable name to a step so it is easy to understand in the Actions logs. |

Workflow Execution Flow
```
Event (push)
      ↓
Workflow Triggered
      ↓
Job Runs (greet)
      ↓
Runner Created (ubuntu-latest)
      ↓
Steps Executed
```

### Task 4: Add More Steps
Update hello.yml to also:

1. Print the current date and time
2. Print the name of the branch that triggered the run (hint: GitHub provides this as a variable)
3. List the files in the repo
4. Print the runner's operating system
5. Push again — watch the new run.

Task 5: Break It On Purpose
Add a step that runs a command that will fail (e.g., exit 1 or a misspelled command)
Push and observe what happens in the Actions tab
Fix it and push again
Write in your notes: What does a failed pipeline look like? How do you read the error?
