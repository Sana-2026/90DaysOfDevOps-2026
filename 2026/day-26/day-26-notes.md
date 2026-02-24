
## Day 26 – GitHub CLI: Manage GitHub from Your Terminal

### Challenge Tasks
#### Task 1: Install and Authenticate

 #### 1. Install the GitHub CLI on your machine
 #### 2. Authenticate with your GitHub account
 #### 3. Verify you're logged in and check which account is active.

<img width="1330" height="393" alt="Github-cli-install" src="https://github.com/user-attachments/assets/71e2e7bd-deda-4a42-98b8-050fd1df2cbd" />

<img width="1189" height="538" alt="task1-ques2-3" src="https://github.com/user-attachments/assets/3c51e171-bc57-492b-9591-e4af73e4ba54" />

#### 4. What authentication methods does gh support?

#### GitHub CLI Authentication Methods

| Method                          | What it is / How it works               | When to use / Key point                 |
| ------------------------------- | --------------------------------------- | --------------------------------------- |
| **Web Login (OAuth)**           | Login via browser or device code        | Easy, recommended for normal CLI use    |
| **Personal Access Token (PAT)** | Supply a token manually or via env var  | Scripts, CI/CD, automation              |
| **SSH Key**                     | Use existing SSH key for Git operations | Push/pull/clone Git repos               |
| **GitHub App / SSO**            | Enterprise login via SAML or app tokens | Required in corporate/enterprise setups |


## Task 2: Working with Repositories

### 1. Create a new GitHub repo directly from the terminal — make it public with a README

<img width="1155" height="546" alt="task2-ques1" src="https://github.com/user-attachments/assets/2fb9c005-870c-45b9-b1cc-1943bf0d6559" />

### 2. Clone a repo using gh instead of git clone

<img width="980" height="193" alt="task2-ques2" src="https://github.com/user-attachments/assets/0376d8f9-001a-4108-89c5-6a415371e508" />

### 3. View details of one of your repos from the terminal

<img width="1330" height="656" alt="task2-ques3" src="https://github.com/user-attachments/assets/7021ce04-ed8e-4ec3-a84e-735824f7095b" />

<img width="1327" height="418" alt="task2-ques3-part2" src="https://github.com/user-attachments/assets/74cac140-9895-4f55-9d6e-333d12d8aba8" />

### 4. List all your repositories.

<img width="1330" height="391" alt="task2-question4" src="https://github.com/user-attachments/assets/05be0e6f-0df6-45aa-b568-8cfd4e039a0d" />

### 5. Open a repo in your browser directly from the terminal

<img width="828" height="122" alt="task2-ques5-part1" src="https://github.com/user-attachments/assets/86e642a9-4c50-4852-951e-d45e7263dacb" />

<img width="1345" height="557" alt="task2-ques5" src="https://github.com/user-attachments/assets/840e7255-8e88-4827-81c5-df5454aec00c" />

<img width="929" height="73" alt="task2-ques5-repo-not-cloned-inlocal" src="https://github.com/user-attachments/assets/4c0f82e1-5b4f-465d-8ec0-369a797b7436" />

<img width="1357" height="583" alt="task2-ques5-wen-repo-is-not-cloned-local" src="https://github.com/user-attachments/assets/73b757f7-f4cd-4426-8497-1f1f1747d0e8" />

### 6. Delete the test repo you created (be careful!)
<img width="1342" height="159" alt="task2-ques6-part1" src="https://github.com/user-attachments/assets/13911997-fc0c-4a2b-a367-e7b271f86223" />

<img width="884" height="521" alt="task1-q6-part2" src="https://github.com/user-attachments/assets/51b56e71-6bbc-41f4-96d3-74b77108397c" />

<img width="789" height="114" alt="task1-ques6-part3" src="https://github.com/user-attachments/assets/adaa64a1-34a1-49c8-aad7-0035f6624a59" />

<img width="1366" height="389" alt="task1-q6-part4" src="https://github.com/user-attachments/assets/6843ca95-f2d2-442b-9360-614f0dacb9cf" />


## Task 3: Issues

### 1. Create an issue on one of your repos from the terminal — give it a title, body, and a label

<img width="1044" height="656" alt="task3-q1-part1" src="https://github.com/user-attachments/assets/e9efe156-fbd2-438a-99f8-1b34b36ffc2e" />

<img width="959" height="303" alt="task3-q1-part2" src="https://github.com/user-attachments/assets/18a41c43-e093-4dd9-9092-4661bf9a0757" />

<img width="1364" height="608" alt="task3-q1-part3" src="https://github.com/user-attachments/assets/aefab277-c2ed-48ee-ae44-8dd09f82f3b4" />

### 2. List all open issues on that repo

<img width="828" height="162" alt="task3-ques2" src="https://github.com/user-attachments/assets/6b175fff-4a07-4f2e-ab38-4bdd093a5525" />

### 3. View a specific issue by its number

<img width="900" height="239" alt="task3-ques3" src="https://github.com/user-attachments/assets/41ef98dc-e257-4389-a06a-8eff6364dde7" />

### 4. Close an issue from the terminal

<img width="1277" height="86" alt="task3-ques4" src="https://github.com/user-attachments/assets/585de6ad-5cfc-4f55-a81e-effbb8b91740" />

### 5a. How could you use gh issue in a script or automation?

#### Using gh issue in Scripts & Automation

### Using `gh issue` in Scripts & Automation

| Task | Command | Purpose |
|-----|--------|---------|
| Authenticate (non-interactive) | `export GH_TOKEN=<PAT>` | Allows gh to run inside scripts / CI |
| Create an issue | `gh issue create --title "Bug" --body "Build failed" --label bug` | Auto-create issues |
| List issues | `gh issue list` | Fetch open issues |
| List issues (JSON) | `gh issue list --json number,title` | Script-friendly output |
| Close an issue | `gh issue close 5` | Auto-close issues |
| Close with comment | `gh issue close 5 --comment "Fixed"` | Close + add context |

### ✅ Typical Automation Use Cases

- CI/CD failure → create GitHub issue
- Auto-close issues after deployment
- Bulk issue management via scripts

## Task 4: Pull Requests

### 1. Create a branch, make a change, push it, and create a pull request entirely from the terminal

<img width="1045" height="623" alt="task4-ques1-part1" src="https://github.com/user-attachments/assets/ec6f1835-aff7-4f21-b20b-f60c5c195cb5" />

<img width="1045" height="356" alt="task4-ques1-part2" src="https://github.com/user-attachments/assets/7bd4056c-d4f7-4122-80ac-fc8574778681" />

### 2. List all open PRs on a repo

<img width="1360" height="447" alt="task4-ques2" src="https://github.com/user-attachments/assets/349f3c68-b271-4999-9615-a4bdfeddd318" />

### 3. View the details of your PR — check its status, reviewers, and checks

<img width="1295" height="382" alt="task4-ques3" src="https://github.com/user-attachments/assets/48d58ae9-bd74-447d-a06b-45f03a800637" />

### 4. Merge your PR from the terminal

<img width="1121" height="307" alt="task4-ques4" src="https://github.com/user-attachments/assets/c750d4a1-4427-4978-b182-d1c807aa840a" />

### 5. What merge methods does gh pr merge support?

### Merge Methods Supported by `gh pr merge`

| Merge Method | Command Flag | What it does | When to use |
|-------------|-------------|--------------|-------------|
| Merge Commit | `--merge` | Creates a merge commit and keeps all commits | Preserve full commit history |
| Squash Merge | `--squash` | Squashes all PR commits into one | Clean, linear history |
| Rebase Merge | `--rebase` | Replays commits on top of base branch | Linear history without merge commit |

### 6. How would you review someone else's PR using gh?

#### Review a Pull Request Using gh

```bash
gh pr list

2️⃣ View the PR details
gh pr view <PR_NUMBER>

Shows:

Title & description

Commits & files changed

Reviewers & status

3️⃣ Check changed files (diff)

gh pr diff <PR_NUMBER>

4️⃣ Review the PR (approve / request changes / comment)
gh pr review <PR_NUMBER>

You will be prompted to choose:

Approve

Request changes

Comment

5️⃣ Review with comment (non-interactive)

gh pr review <PR_NUMBER> --approve --comment "Looks good to me"

```bash

## Task 5: GitHub Actions & Workflows (Preview)

### 1. List the workflow runs on any public repo that uses GitHub Actions

### 2. View the status of a specific workflow run

<img width="1288" height="671" alt="task5-ques1" src="https://github.com/user-attachments/assets/21fd8bef-bd3a-4b70-b3f5-6835c1dcb8c7" />

#### 3. Answer in your notes: How could gh run and gh workflow be useful in a CI/CD pipeline?

| Command | How it helps | CI/CD Use Case |
|--------|--------------|----------------|
| `gh workflow list` | Lists all GitHub Actions workflows | Discover available CI/CD pipelines |
| `gh workflow run` | Manually triggers a workflow | Re-run builds or deployments |
| `gh run list` | Lists workflow runs | Monitor pipeline executions |
| `gh run view` | Shows run status, logs, and results | Debug failed CI/CD jobs |
| `gh run download` | Downloads artifacts from runs | Retrieve build outputs |
