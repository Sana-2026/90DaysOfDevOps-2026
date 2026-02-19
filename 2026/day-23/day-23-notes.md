# Day 23 – Git Branching & Working with GitHub

## Task 1: Understanding Branches

### What is a branch in Git?

A branch is a separate path where you can work on changes without affecting the main code.

You copy the project, work freely, and later decide whether to add it back.

Command to see branches

- git branch

Command to create a new branch

- git branch feature-login

Command to switch to that branch
- git checkout feature-login

(or modern way)

- git switch feature-login


### Why do we use branches instead of committing everything to main?

#### We don’t commit everything to main because:

main should always be stable

New features may break things

Bugs should not affect working code

#### Branches allow:

Safe experimentation

Clean and organized work

Easy collaboration

### What is HEAD in Git?

HEAD is a pointer that tells Git:

“This is where you are right now.”

It points to:

The current branch

The latest commit on that branch

### What happens to your files when you switch branches?

When you switch branches:

- Git updates your files automatically

- Files change to match the selected branch

- Uncommitted changes may stop the switch
- 
## Task 2: Branching Commands — Hands-On

### 1. List all branches in your repo

<img width="821" height="150" alt="branch" src="https://github.com/user-attachments/assets/0366639c-4517-46a7-89ab-37db62777c92" />

### 2.Create a new branch called feature-1

<img width="648" height="92" alt="branch-feature-1" src="https://github.com/user-attachments/assets/b1e8bb06-c648-4b45-ac7f-decfb444793c" />

### 3.Switch to feature-1

<img width="747" height="429" alt="q5-switchbranch" src="https://github.com/user-attachments/assets/6b433d9d-2cac-4bd3-86b8-cb31b650a0b8" />

### 4.Create a new branch and switch to it in a single command — call it feature-2

<img width="736" height="74" alt="switch-branch" src="https://github.com/user-attachments/assets/84dfcd98-4c6d-4319-bd77-a66f9a1aa090" />

### 5.Try using git switch to move between branches — how is it different from git checkout?

<img width="747" height="429" alt="q5-switchbranch" src="https://github.com/user-attachments/assets/656ceee2-95e2-435d-b4ed-9988489f4abf"/>

### 6.Make a commit on feature-1 that does not exist on main

<img width="1185" height="455" alt="Q6-Task2" src="https://github.com/user-attachments/assets/5daef5cc-4481-402b-9c8d-940fc5b69fcb"/>

### 7.Switch back to main — verify that the commit from feature-1 is not there

<img width="1000" height="716" alt="Q7-task2" src="https://github.com/user-attachments/assets/152bf37f-dcb9-4009-a5e7-c6e06eab8694"/>

### 8.Delete a branch you no longer need

<img width="950" height="541" alt="Q8-Task2" src="https://github.com/user-attachments/assets/f97f0315-77c1-4a1c-8d76-3b770eba19fb"/>

### 9.Add all branching commands to your git-commands.md

done

## Task 3: Push to GitHub

### 1.Create a new repository on GitHub (do NOT initialize it with a README)

<img width="1343" height="644" alt="task3-q1" src="https://github.com/user-attachments/assets/e45cd934-96d0-4b1d-9fb2-643670e384d6"/>

### 2.Connect your local devops-git-practice repo to the GitHub remote

<img width="986" height="204" alt="connecting-local-repo-to-github" src="https://github.com/user-attachments/assets/917b39cb-713c-49a0-8b88-adadc2c91dc6"/>


### 3.Push your main branch to GitHub

<img width="906" height="720" alt="Push-main -branch-to-GitHub" src="https://github.com/user-attachments/assets/3f73ed84-1f7a-42ee-ae97-9373e5f8c53f"/>

### 4.Push feature-1 branch to GitHub

<img width="998" height="501" alt="push-branch-feature-one" src="https://github.com/user-attachments/assets/25d349fe-9a0d-4707-b62e-06bf613d4a85"/>

### 5.Verify both branches are visible on GitHub

<img width="1348" height="569" alt="2-brnch-pushed" src="https://github.com/user-attachments/assets/f3e05c2d-56ac-47a1-a1f2-a93fc3f1df71"/>

### 6.What is the difference between origin and upstream?

Difference Between origin and upstream
#### 🔹 What is origin?

- origin is the default remote name for your repository

- It usually points to your GitHub repo

- You push your changes to origin

Example

origin → git remote add origin https://github.com/Sana-2026/devops-hands-on.git

#### 🔹 What is upstream?

- upstream points to the original / main repository

- Common when working with forked repositories

- You pull updates from upstream

- You usually do not push to upstream

Example

upstream →  git remote add origin https://github.com/Sana-2026/90DaysOfDevOps


## Task 4: Pull from GitHub

### 1. Make a change to a file directly on GitHub (use the GitHub editor)

<img width="1340" height="588" alt="chnges-in-github" src="https://github.com/user-attachments/assets/bf902985-f11c-4dcf-bdd7-7c6e70f33111" />

### 2. Pull that change to your local repo

<img width="1066" height="722" alt="pull-request" src="https://github.com/user-attachments/assets/800230c2-516c-46ce-95c7-c458fdd0ce1d" />


### 3. Difference Between git fetch and git pull

🔹 git fetch

- Downloads latest changes from the remote repository

- Does NOT change your local branch

- Safe way to check what’s new before merging

  git fetch origin

### What happens

- Remote branches update (e.g., origin/main)

- Your local files stay untouched

- Fetch = see what changed

🔹 git pull

- Downloads changes and merges them into your current branch

- Updates your local files

- Can cause merge conflicts

  git pull origin main


### What happens

- Runs git fetch

- Then runs git merge

- Pull = fetch + merge

## Task 5: Clone vs Fork

### 1. Clone any public repository from GitHub to your local machine

<img width="955" height="633" alt="clone" src="https://github.com/user-attachments/assets/7f1f7e5f-1007-4936-8702-a0d28fb40adf" />

### 2. Fork the same repository on GitHub, then clone your fork

<img width="1336" height="553" alt="fork-repo" src="https://github.com/user-attachments/assets/38edda16-4721-498a-8647-defd21014395" />


### 3. Difference Between clone and fork

🔹 Clone

- Creates a local copy of a repository on your machine

- Does not create a new repo on GitHub

- Used to work on a repo you already own or have access to

    git clone <repo-url>

🔹 Fork

- Creates a new copy of a repository on GitHub under your account

- Original repo remains unchanged

- Used when you don’t have write access to the original repo

📌 Fork is done on GitHub (UI, not terminal)

## Clone vs Fork

| Action | Clone | Fork |
|------|-------|------|
| Where the copy is created | Local machine | GitHub account |
| Creates a new GitHub repository | No | Yes |
| Used when | You have write access | You don’t have write access |
| Typical use case | Team or personal projects | Open-source contributions |
| How it’s done | git clone <repo-url> | Click Fork on GitHub |

### 4. When would you clone vs fork?

#### Use Clone when:
- You own the repository
- You are a collaborator on the project
- You have write access to the repository
- You want to work directly on the same repo

#### Use Fork when:
- You do NOT own the repository
- You do NOT have write access
- You want to contribute to an open-source project
- You plan to submit changes via a Pull Request
  
  ### 5. After forking, how do you keep your fork in sync with the original repo?

✅ Method 1: Using GitHub UI (Sync fork)

On GitHub:

- Go to your forked repository

- Click Sync fork

- Click Update branch

📌 This updates your fork on GitHub only

✅ Method 2: Using Terminal 

  #### Step 1: Clone your fork
git clone https://github.com/your-username/repo.git
cd repo

#### Step 2: Add the original repository as upstream
git remote add upstream https://github.com/original-owner/repo.git

#### Step 3: Fetch latest changes from upstream
git fetch upstream

#### Step 4: Merge upstream changes into your local branch
git merge upstream/main

#### Step 5: Push updated branch to your fork
git push origin main




