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

We don’t commit everything to main because:

main should always be stable

New features may break things

Bugs should not affect working code

Branches allow:

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

<img width="747" height="429" alt="q5-switchbranch" src="https://github.com/user-attachments/assets/656ceee2-95e2-435d-b4ed-9988489f4abf" />

### 6.Make a commit on feature-1 that does not exist on main

<img width="1185" height="455" alt="Q6-Task2" src="https://github.com/user-attachments/assets/5daef5cc-4481-402b-9c8d-940fc5b69fcb" />

### 7.Switch back to main — verify that the commit from feature-1 is not there

<img width="1000" height="716" alt="Q7-task2" src="https://github.com/user-attachments/assets/152bf37f-dcb9-4009-a5e7-c6e06eab8694" />

### 8.Delete a branch you no longer need

<img width="950" height="541" alt="Q8-Task2" src="https://github.com/user-attachments/assets/f97f0315-77c1-4a1c-8d76-3b770eba19fb" />

### 9.Add all branching commands to your git-commands.md

done

## Task 3: Push to GitHub

### 1.Create a new repository on GitHub (do NOT initialize it with a README)
### 2.Connect your local devops-git-practice repo to the GitHub remote
### 3.Push your main branch to GitHub
### 4.Push feature-1 branch to GitHub
### 5.Verify both branches are visible on GitHub
### 6.What is the difference between origin and upstream?





