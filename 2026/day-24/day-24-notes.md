
## Task 1: Git Merge — Hands-On

1. Create a new branch feature-login from main, add a couple of commits to it
<img width="1077" height="719" alt="New-feature-login-branch-created" src="https://github.com/user-attachments/assets/cf96b993-7fe3-4e7d-8a7d-4aed7f11d9ce" />

<img width="1054" height="728" alt="commit-on-feature-login-branch" src="https://github.com/user-attachments/assets/376cf33a-3199-4ea0-bf93-1b5fee77fcca" />

<img width="1041" height="721" alt="commit-passd-feature-login" src="https://github.com/user-attachments/assets/08419fbb-50da-46a5-a831-d362b2d52271" />

2. Switch back to main and merge feature-login into main

<img width="818" height="265" alt="Task1-2q" src="https://github.com/user-attachments/assets/0c32b29f-05a2-4c30-bb73-182b9e92e2ac" />

3. Observe the merge — did Git do a fast-forward merge or a merge commit?
   
   * Git did a fast-forward merge
     
   * The main branch had not changed after the feature branch was created

   * All new commits existed only on the feature branch

   * There was no divergence between main and the feature branch

   * So Git didn’t need to “merge” histories.

   * Instead, Git simply moved the main pointer forward to the latest commit of the feature branch


4. Now create another branch feature-signup, add commits to it — but also add a commit to main before merging

<img width="1074" height="700" alt="task1-q4" src="https://github.com/user-attachments/assets/225a1c21-9d22-443d-aad5-ab869f6fb035" />

<img width="738" height="315" alt="task1-q4-part2" src="https://github.com/user-attachments/assets/e648b0c5-7b33-4584-9f19-29ea4d2b4f3c" />

5. Merge feature-signup into main — what happens this time?
  * A merge conflict happens when the same file is modified in more than one branch and Git cannot decide which change to keep.

<img width="798" height="179" alt="task1-q5-merge-conflict" src="https://github.com/user-attachments/assets/d3485836-46e5-494f-8d6d-f47072df0745" />

<img width="809" height="213" alt="task1-q5-status-merge-conflict" src="https://github.com/user-attachments/assets/7210a7e1-00b1-4da3-83a5-6ee75c5b5275" />

<img width="773" height="409" alt="task1-q5-part3" src="https://github.com/user-attachments/assets/aa1cea8d-8d5a-48b1-8295-f5853c7ca260" />

* Resolved the merge conflict and checked the logs.
  
<img width="925" height="575" alt="task1-q5-resolvedconflict" src="https://github.com/user-attachments/assets/9fa674ea-d89c-427b-88e3-0a7fd40f1b72" />


 ### 6.a) What is a fast-forward merge?

* Happens when main has not moved ahead

* Git simply moves the branch pointer forward

* No merge commit is created

🧠 Memory hook:

Fast-forward = no divergence, just move the pointer

### 6.b)  When does Git create a merge commit?

* Git creates a merge commit when:

* Both branches have new commits

* Histories have diverged

* A fast-forward is not possible

🧠 Memory hook:

Diverged history → merge commit needed

### 6.c)  What is a merge conflict?

* Happens when same file + same lines changed in both branches

* Git cannot decide which change to keep

* You must manually resolve it

🧠 Memory hook:

Conflict = Git is confused, human decides



## Task 2: Git Rebase — Hands-On

1. Create a branch feature-dashboard from main, add 2-3 commits

<img width="1362" height="696" alt="task2-q1" src="https://github.com/user-attachments/assets/c79d80fb-661c-4670-9bdb-b89357d08527" />
<img width="1351" height="550" alt="task2-q1-part2" src="https://github.com/user-attachments/assets/12e63228-4f7c-4954-9896-39e06879e818" />

2. While on main, add a new commit (so main moves ahead)

<img width="1346" height="697" alt="task-2-rebase-ques2" src="https://github.com/user-attachments/assets/de8fc2cd-4b0c-4640-b83a-bb1839e0445a" />

3. Switch to feature-dashboard and rebase it onto main
   
<img width="1222" height="723" alt="task2-rebase-q3" src="https://github.com/user-attachments/assets/eadc88cb-a5d9-4d6d-be33-5f941191fecc" />

<img width="932" height="650" alt="task2-rebase-q3-part2" src="https://github.com/user-attachments/assets/e4ad094b-07e2-4841-8cdb-69e9ac3e9f45" />

<img width="899" height="484" alt="task-2-rebase-ques2-part3" src="https://github.com/user-attachments/assets/d02a3808-a81d-460e-bedc-edb83ddbdc5f" />

<img width="1039" height="674" alt="task-2-rebase-ques2-part4" src="https://github.com/user-attachments/assets/9638e01e-6ced-4b92-8307-6522fba69f2e" />

<img width="842" height="534" alt="task-2-rebase-ques2-part5" src="https://github.com/user-attachments/assets/ecb0d8d4-9193-442b-96f3-ae0ef210c5aa" />

4. Observe your git log --oneline --graph --all — how does the history look compared to a merge?
   

### Understanding git log --oneline --graph --decorate --all

#### 1️⃣ Commit line structure

commit-id (branch pointers) commit message

Example:

1d4ae98 (HEAD -> feature-dashboard) Resolved conflicts in dashboard

- Commit ID → unique identifier

- HEAD → where you are right now

- Branch name → which branch points to this commit

- Message → what changed

#### 2️⃣ Branch pointers (inside brackets)

HEAD -> feature-dashboard → currently on feature-dashboard

(main) → main branch latest commit

(feature-login) → feature-login branch tip

(origin/main) → remote GitHub main branch

#### 3️⃣ Graph symbols (MOST IMPORTANT)

(*) commit
  
|   same branch history

|\

| * branch split

|/

(*) merged history

(*) → a commit

| → straight history

/ \ → branch split or merge

#### 4️⃣ Rebase 
* 258ccb9 Improved UI of dashboard
* 993a448 Added user stats widget
* 48f7d2b Added dashboard for users

* These commits were replayed one by one during git rebase

* triggered multiple conflicts

#### 5️⃣ Merge commit 

4c633ea Merge branch 'feature-signup'

* This is a merge commit

#### 6️⃣ Stash entries (special)

(refs/stash) WIP on feature-dashboard

* Saved uncommitted work

* Used to temporarily park changes

#### 7️⃣ Rules to remember

- HEAD → where I am

- Branch name → pointer to a commit

- Merge commit → two histories joined

- Rebase → commits rewritten & replayed

- Stash → hidden work, not committed

- Colors → terminal-dependent, NOT Git logic


### What does rebase actually do to your commits?

* Rebase replays your commits on top of another branch

* Old commits are deleted

* New commits with new commit IDs are created

🧠 Memory Hook :

Rebase = copy → replay → replace commits

### How is the history different from a merge?

* Merge → keeps original history + adds a merge commit

* Rebase → rewrites history into a straight line

🧠 Memory Hook :

Merge = real history
Rebase = clean history




### Why should you never rebase pushed & shared commits?

* Rebase changes commit IDs

* Teammates still have the old commits

* Causes duplicate commits & conflicts

* Breaks team history

🧠 Memory hook:

❌ Never rebase commits that others may already have



### When would you use rebase vs merge?
#### Use rebase when:

* Working on your local feature branch

* Updating your branch with latest main

* Want clean, linear history

* No one else is using your branch

#### Use merge when:

* Code is already pushed

* Working with a team

* Merging feature → main

* You want safe, traceable history

🧠 Memory hook :

Rebase before push, Merge after push


## 🔀 Rebase vs Merge

| Feature | `git merge` | `git rebase` |
|-------|-------------|--------------|
| What it does | Combines two branches | Replays commits on top of another branch |
| Commit history | Preserved | Rewritten |
| Merge commit | ✅ Yes (for non fast-forward) | ❌ No |
| Commit hashes | Remain the same | Change |
| History shape | Branching graph | Linear / straight line |
| Conflict handling | Once per merge | Possibly once per commit |
| Safe for shared branches | ✅ Yes | ❌ No |
| Common usage | Merging feature → main | Updating feature branch with main |
| Industry preference | Safer, more explicit | Cleaner, more readable history |
| Risk level | Low | Medium (if misused) |

## Task 3: Squash Commit vs Merge Commit

### What does squash merging do?
- Combines **all commits from a feature branch into a single commit**
- That one commit is added to the target branch (usually `main`)
- Individual commits from the feature branch are **not preserved** in `main`

🧠 **Memory hook**:  
> Squash = many commits → one clean commit

---

### When to use squash merge vs regular merge?

#### Use **squash merge** when:

- Feature branch has **messy or WIP commits**
- You want a **clean and simple main branch history**
- Commit-by-commit history is not important
- Small features or solo work

#### Use **regular merge** when:

- Commit history **matters**
- You want to track **how changes evolved**
- Working in a **team**
- Large or complex features

🧠 **Memory hook**:  

> Clean history → squash  
> Detailed history → merge

---
## 🔀 Merge vs Squash
| Feature | Normal Merge (`git merge`) | Squash Merge (`git merge --squash`) |
|-------|----------------------------|-------------------------------------|
| Keeps all commits | ✅ Yes | ❌ No |
| Creates merge commit | ✅ Yes | ❌ No |
| Preserves branch history | ✅ Yes | ❌ No |
| Commit history | Detailed | Clean & compact |
| Easy to understand history | ❌ Can be messy | ✅ Very clean |
| Rollback changes | ❌ Hard (many commits) | ✅ Easy (single commit) |
| Common usage | Long-running branches, open-source | Feature branches, PRs |
| Used in GitHub PRs | ⚠️ Sometimes | ✅ Very common |

### What is the trade-off of squashing?

- ❌ Lose small commit details
- ❌ Hard to see how work evolved
- ❌ Cannot undo tiny changes separately
- ✅ Gain a clean, simple history

🧠 **Memory hook**:  
> Squash keeps the **result**, not the **journey**

## Task 4: Git Stash — Hands-On


### Difference between `git stash apply` and `git stash pop`

### `git stash apply`
- Applies the stashed changes
- **Keeps** the stash in stash list
- You can reuse the same stash again

🧠 **Memory hook**:  
> Apply = use it, keep it

---

### `git stash pop`
- Applies the stashed changes
- **Removes** the stash from stash list
- One-time use

🧠 **Memory hook**:  
> Pop = use it, drop it

---

## When would you use stash in real-world workflow?
- You are working on a feature
- Suddenly need to **switch branches**
- Your changes are **not ready to commit**
- You stash the work, fix something urgent, then come back

🧠 **Memory hook**:  
> Stash = temporary save, not a commit

---

## Task 5: Cherry Picking


###  What does `git cherry-pick` do?
- Takes **one specific commit** from another branch
- Applies it to your **current branch**
- Creates a **new commit with a new commit ID**

🧠 **Memory hook**:  
> Cherry-pick = pick one commit you like

---

### When would you use cherry-pick in a real project?
- A **bug fix** exists in another branch
- You need **only that fix**, not the full branch
- Hotfix needs to go to **main / release branch**
- Backporting a fix to an older version

🧠 **Memory hook**:  
> One needed commit → cherry-pick

---

###  What can go wrong with cherry-picking?
- ❌ Can cause **conflicts** if code differs
- ❌ Creates **duplicate commits** (same change, different IDs)
- ❌ History can become confusing if overused

🧠 **Memory hook**:  
> Cherry-pick is powerful, but don’t overuse it

---





