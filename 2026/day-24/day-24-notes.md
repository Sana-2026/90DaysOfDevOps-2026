
## Task 1: Git Merge — Hands-On

 ### What is a fast-forward merge?

* Happens when main has not moved ahead

* Git simply moves the branch pointer forward

* No merge commit is created

🧠 Memory hook:

Fast-forward = no divergence, just move the pointer

### When does Git create a merge commit?

* Git creates a merge commit when:

* Both branches have new commits

* Histories have diverged

* A fast-forward is not possible

🧠 Memory hook:

Diverged history → merge commit needed

###  What is a merge conflict?

* Happens when same file + same lines changed in both branches

* Git cannot decide which change to keep

* You must manually resolve it

🧠 Memory hook:

Conflict = Git is confused, human decides



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

## Task 2: Git Rebase — Hands-On

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


#### What does rebase actually do to your commits?

* Rebase replays your commits on top of another branch

* Old commits are deleted

* New commits with new commit IDs are created

🧠 Memory Hook :

Rebase = copy → replay → replace commits

#### How is the history different from a merge?

* Merge → keeps original history + adds a merge commit

* Rebase → rewrites history into a straight line

🧠 Memory Hook :

Merge = real history
Rebase = clean history




#### Why should you never rebase pushed & shared commits?

* Rebase changes commit IDs

* Teammates still have the old commits

* Causes duplicate commits & conflicts

* Breaks team history

🧠 Memory hook:

❌ Never rebase commits that others may already have



#### When would you use rebase vs merge?
##### Use rebase when:

* Working on your local feature branch

* Updating your branch with latest main

* Want clean, linear history

* No one else is using your branch

##### Use merge when:

* Code is already pushed

* Working with a team

* Merging feature → main

* You want safe, traceable history

🧠 Memory hook :

Rebase before push, Merge after push


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

### What is the trade-off of squashing?

- ❌ Loses individual commit history
- ❌ Harder to trace or revert a specific change later
- ❌ Less context for debugging

🧠 **Memory hook**:  
> Squash = clean history, less detail




