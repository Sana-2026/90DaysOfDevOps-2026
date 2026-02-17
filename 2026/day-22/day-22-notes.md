# Day 22 – Introduction to Git: My First Repository

## Task 1: Install and Configure Git

### ✅ Step 1: Verify Git is installed
git --version

✔️ If you see a version → Git is installed
❌ If not → Git is not installed

### ✅ Step 2: Set your Git identity (one-time)
Set your name

git config --global user.name "Your Name"

Set your email

git config --global user.email "your_email@example.com"

### ✅ Step 3: Verify your configuration

git config --global --list

Expected output:

user.name=Your Name
user.email=your_email@example.com


<img width="1225" height="554" alt="Screenshot 2026-02-18 014106" src="https://github.com/user-attachments/assets/bd4376ed-6e78-493c-9797-c8836638476c" />

## Task 2: Create Your Git Project

### 1️⃣ Create a new folder

mkdir devops-git-practice

cd devops-git-practice

### 2️⃣ Initialize it as a Git repository

git init

- Git creates a hidden folder called .git/

- Your folder is now under version control

### 3️⃣ Check repository status

git status

On branch master/main → you’re on the main branch

No commits yet → nothing saved in history

nothing to commit → no files tracked yet

👉 This is a clean, empty repo

### 4️⃣ Explore the hidden .git/ directory

Show hidden files (Git Bash)

ls -la
ls .git

- objects/ → where Git stores file data (blobs, trees, commits)

- refs/ → pointers to commits (branches, HEAD)

- HEAD → tells Git which branch you’re on

- config → repo-specific settings

<img width="1363" height="709" alt="task2" src="https://github.com/user-attachments/assets/ef3210eb-82d1-4d25-9058-3d500f6d4672" />

<img width="1343" height="686" alt="task-2-gitfolder-hooks" src="https://github.com/user-attachments/assets/113b10e2-849e-4324-bd06-015431d9f82d" />

<img width="1052" height="582" alt="task2-gitfolder-objts" src="https://github.com/user-attachments/assets/85f36147-abbc-4acb-b3d4-3a0d3fc65fda" />

## Task 3: Create Your Git Commands Reference

<img width="1001" height="647" alt="task 3" src="https://github.com/user-attachments/assets/9b0de0ab-71fa-48c7-919b-bea90766ca35" />

## Task 4: Stage and Commit

### 1️⃣ Stage your file

git add git-command.md

What this does:

Moves the file from working directory → staging area

### 2️⃣ Check what’s staged
git status

- Changes to be committed → ✅ staged

- Green file name → ready to commit

(Only green files get saved)

### 3️⃣ Commit with a meaningful message

git commit -m "Add Git command notes"

What this does:

Takes a snapshot of staged files

Saves it permanently in Git history

### 4️⃣ View your commit history

What you’ll see:

Commit ID (hash)

Author (your name & email)

Date & commit message

<img width="1059" height="703" alt="task4" src="https://github.com/user-attachments/assets/7ac3bdbe-8b37-48a9-a317-056493d12828" />

## Task 5: Make More Changes and Build History

<img width="1036" height="720" alt="task5-1" src="https://github.com/user-attachments/assets/1a6be78c-9673-4be5-84a0-5a77c35b00cf" />

<img width="1016" height="725" alt="task5-2" src="https://github.com/user-attachments/assets/b61d6c3f-a26d-47ae-aead-8796d6a26f91" />

<img width="733" height="236" alt="task5-3" src="https://github.com/user-attachments/assets/a75b9509-f514-4c2e-9b6b-9751bb2c29e7" />



