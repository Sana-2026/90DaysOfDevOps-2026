
## Day 25 – Git Reset vs Revert & Branching Strategies

## Challenge Tasks

### Task 1: Git Reset — Hands-On

#### 1. Make 3 commits in your practice repo (commit A, B, C)

<img width="1000" height="687" alt="Task1-ques1" src="https://github.com/user-attachments/assets/dc4613a4-abbf-45c4-8224-949f065d1e95" />

<img width="554" height="87" alt="task1-ques1-part2" src="https://github.com/user-attachments/assets/f752bd72-558f-41eb-813c-53a718a08977" />

#### 2. Use git reset --soft to go back one commit — what happens to the changes?

<img width="592" height="179" alt="task1-ques2-part1" src="https://github.com/user-attachments/assets/554ceba6-1fb4-491f-bc29-936a6d9f0184" />

<img width="561" height="359" alt="task1-ques2-part2" src="https://github.com/user-attachments/assets/0f2a8756-4392-4a4a-88d9-bf63ef4e6f5e" />

Before running git reset command repository contains three commits in sequence:

Commit A → Commit B → Commit C (HEAD, main)

#### What Happens when git reset --soft HEAD~1 is executed:

Commits        : A → B (HEAD)

* HEAD moves from Commit C → Commit B

* Branch main also points to Commit B

* Commit C is removed from commit history

* Changes from Commit C are:

    - Preserved

    - Kept in the staging area

#### Reset command moves only the commit pointer

      Does NOT modify:

    - Working directory files

    - Staging area contents


#### Use Cases

*  Editing or fixing the last commit message

*  Squashing commits before pushing

*  Cleaning up commit history before opening a PR

*  Recommitting changes in a better logical structure


#### git reset --mixed HEAD~1 — Before vs After

##### Before Reset

- HEAD points to the latest commit (Commit C)

- Commit history includes A → B → C

- Working directory is clean

- Staging area is empty

    A → B → C (HEAD)
    Working directory : clean
    Staging area      : empty


##### After Reset

- HEAD moves back to Commit B

- Commit C is removed from history

- Changes from Commit C remain in the working directory

- Staging area is cleared (changes are unstaged)

    A → B (HEAD)
    Working directory : modified (changes from C)
    Staging area      : empty


  ##### Use Cases (git reset --mixed)

* Uncommitting changes while keeping them in the working directory

* Reviewing and re-staging changes before committing again

* Splitting a single commit into multiple logical commits

* Fixing commits made on the wrong branch before pushing

#### 4. Re-commit, then use git reset --hard to go back one commit — what happens this time?

<img width="840" height="707" alt="task1-q4" src="https://github.com/user-attachments/assets/7e71a78f-7ed5-46b0-b043-aa8c4116473b" />

#### What Happens Internally

* HEAD moves from Commit C → Commit B

* Branch main also moves to Commit B

* Commit C is removed from commit history

* All changes from Commit C are permanently discarded

* Working directory and staging area are reset to exactly match Commit B
  
5a) What is the difference between --soft, --mixed, and --hard?

* --soft → Undo the commit, keep changes staged

* --mixed → Undo the commit, keep changes unstaged

* --hard → Undo the commit and delete all changes
  
### 5b) Which one is destructive and why?

git reset --hard` is destructive because it permanently discards local changes.
  It removes the commit from history
  - It deletes all changes from both:
  - the staging area
  - the working directory
  - Once done, the lost changes cannot be recovered easily 
### 5c) When would you use each one?

### `git reset --soft`
- When you want to **edit or fix the last commit message**
- When you want to **squash commits** before pushing
- When you want to **recommit changes without unstaging them**

👉 Best when you want to rewrite history but keep changes ready to commit.

---

### `git reset --mixed` (default)
- When you want to **undo a commit but review changes again**
- When you want to **re-stage files selectively**
- When you committed on the **wrong branch** and want to fix it

👉 Best when you want control over what gets staged next.

---

### `git reset --hard`
- When you want to **discard local changes completely**
- When your working tree is **broken and you want a clean state**
- When undoing **local, unpushed commits only**

👉 Best when you want to reset everything and start clean.

---

### 🧠 Quick memory rule
> **Soft = staged • Mixed = unstaged • Hard = gone**

### 5d) Should you ever use git reset on commits that are already pushed?

No, you should not :
`git reset` **rewrites commit history**
- Pushed commits may already be:
  - pulled by teammates
  - used in CI/CD pipelines
- Resetting them causes:
  - history mismatch
  - merge conflicts
  - broken collaboration

👉 This can force others to deal with **confusing errors and lost work**.

---

### 🔑 Key Difference: --soft vs --mixed vs --hard

| Reset Mode            | Commit History      | Staging Area              | Working Directory            | Data Loss Risk | Common Use Case                            |
| --------------------- | ------------------- | ------------------------- | ---------------------------- | -------------- | ------------------------------------------ |
| `--soft`              | Last commit removed | Changes remain **staged** | Files unchanged              | 🟢 Low         | Edit commit message, squash commits        |
| `--mixed` *(default)* | Last commit removed | Staging area **cleared**  | Files unchanged              | 🟡 Medium      | Uncommit changes for review and re-staging |
| `--hard`              | Last commit removed | Cleared                   | Files reset to target commit | 🔴 High        | Discard local changes completely           |











