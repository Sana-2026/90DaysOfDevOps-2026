## Day 41 – Triggers & Matrix Builds

### Challenge Tasks

### Task 1: Trigger on Pull Request

1. Create .github/workflows/pr-check.yml

 2.Trigger it only when a pull request is opened or updated against main

3. Add a step that prints: PR check running for branch: <branch name>

4. Create a new branch, push a commit, and open a PR
   
5. Watch the workflow run automatically
   
Verify: Does it show up on the PR page?

<img width="1356" height="382" alt="task1" src="https://github.com/user-attachments/assets/e7710bf0-6ef2-432b-a992-6d0c094ece68" />

<img width="1346" height="636" alt="task-1-partb" src="https://github.com/user-attachments/assets/51d7521e-2669-49c9-8dd3-675b63c0e036" />

<img width="1363" height="646" alt="task-1-partc" src="https://github.com/user-attachments/assets/3b44eba2-5cab-47e6-bb93-4c3546d333db" />

<img width="1366" height="615" alt="task-1-partd" src="https://github.com/user-attachments/assets/cc9beef1-97b1-4528-b848-2012560d3c0e" />

<img width="1366" height="473" alt="new-commit-PR-workflow" src="https://github.com/user-attachments/assets/7c46e130-57d5-420a-bc62-6ac52850b804" />

### Task 2: Scheduled Trigger

1. Add a schedule: trigger to any workflow using cron syntax
   
 - Added in pr-check workflow
   
2. Set it to run every day at midnight UTC

``schedule:
    - cron: "0 0 * * *"   # Runs every day at midnight UTC
    ``

What the cron expression means
+ Run at 00:00 (midnight)
+ Every day
+ UTC time

```
0 0 * * *
│ │ │ │ │
│ │ │ │ └── Day of week
│ │ │ └──── Month
│ │ └────── Day of month
│ └──────── Hour
└────────── Minute

<img width="1366" height="465" alt="task2" src="https://github.com/user-attachments/assets/033326c8-bdb2-48fa-87c5-232c6022e509" />


```

[.github-actions/workflows/pr-check.yml](https://github.com/Sana-2026/github-actions-practice/blob/main/.github/workflows/pr-check.yml)

4. Write in your notes: What is the cron expression for every Monday at 9 AM?
 `` 0 9 * * 1``

Meaning:

Minute → 0
Hour → 9
Day of month → *
Month → *
Day of week → 1 (Monday)

### ✅ Examples to Remember

| Schedule | Cron |
|----------|------|
| Daily at midnight | `0 0 * * *` |
| Daily at 6 AM | `0 6 * * *` |
| Every Monday 9 AM | `0 9 * * 1` |
| Every 5 minutes | `*/5 * * * *` |

### Task 3: Manual Trigger

1. Create .github/workflows/manual.yml with a workflow_dispatch: trigger

2. Add an input that asks for an environment name (staging/production)
   
3. Print the input value in a step
   
4. Go to the Actions tab → find the workflow → click Run workflow
   
    Verify: Can you trigger it manually and see your input printed?
    - Yes i can

<img width="1350" height="597" alt="task3-part a" src="https://github.com/user-attachments/assets/e62a3dfd-5f4d-455f-93f3-d2c50bb3e2e9" />

<img width="1324" height="605" alt="task3-part-b" src="https://github.com/user-attachments/assets/4ff31b13-ec04-45f9-bd7f-1daa26b9b7a9" />

<img width="1331" height="609" alt="task3-partc" src="https://github.com/user-attachments/assets/57991305-ad4c-45f1-ac7f-3858f0510628" />

### Task 4: Matrix Builds

1. Create .github/workflows/matrix.yml that:

2. Uses a matrix strategy to run the same job across:
   
3. Python versions: 3.10, 3.11, 3.12
   
4. Each job installs Python and prints the version
  
5. Watch all 3 run in parallel

<img width="1356" height="614" alt="task4-part1" src="https://github.com/user-attachments/assets/26e1685f-5e26-49b8-8c73-b50d8cf7b530" />

<img width="1343" height="616" alt="task4-2" src="https://github.com/user-attachments/assets/7a5fb178-12eb-4519-b7c2-3683f5194f05" />

<img width="1323" height="639" alt="task4-3" src="https://github.com/user-attachments/assets/63ce1ae5-795b-4b9c-95a3-1298c1210c0f" />

<img width="1336" height="618" alt="task4-4" src="https://github.com/user-attachments/assets/465f2b7f-183d-4300-a0e4-e439a6be5611" />

6.Then extend the matrix to also include 2 operating systems — how many total jobs run now?

<img width="1332" height="556" alt="task4-5" src="https://github.com/user-attachments/assets/935b6ff7-8370-4727-a1b3-58e41dc3fbd4" />

<img width="1332" height="556" alt="task4-6" src="https://github.com/user-attachments/assets/5fd53006-c194-46bf-a6bd-7d936b99609e" />


## GitHub Actions Matrix Workflow Issue

### Problem

After creating the GitHub Actions matrix workflow, the job failed with the following error:
The version '3.1' with architecture 'x64' was not found for Ubuntu 24.04.


### Why This Happened

In the matrix configuration, the Python versions were written like this:

```yaml
python-version: [3.10, 3.11, 3.12]

YAML interprets numbers like 3.10 as floating-point values.

So YAML converts:

Written Version	YAML Interprets As
3.10	3.1
3.11	3.11
3.12	3.12

Because of this, GitHub Actions tried to install Python 3.1, which does not exist.

Steps to Fix the Issue

#### 1. Open the workflow file
.github/workflows/matrix.yml

#### 2. Update the matrix versions

Wrap the Python versions in quotes so YAML treats them as strings.

❌ Incorrect

python-version: [3.10, 3.11, 3.12]

✅ Correct

python-version: ["3.10", "3.11", "3.12"]

#### 3. Save the file and commit the fix

- git add .
- git commit -m "Fix Python matrix version parsing issue"
- git push

#### 4. Verify the workflow

+ Go to GitHub Repository

+ Click Actions

+ Open the workflow run

+ Confirm that jobs run for:

+ Python 3.10

+ Python 3.11

+ Python 3.12

+ All jobs should now run successfully in parallel.

#### Key Takeaway

When defining version numbers in YAML matrices, always wrap them in quotes:

### Task 5: Exclude & Fail-Fast

1. In your matrix, exclude one specific combination (e.g., Python 3.10 on Windows)

<img width="1356" height="614" alt="task4-part1" src="https://github.com/user-attachments/assets/2c6da76e-4435-4690-a633-3219af2c4fe0" />

<img width="1343" height="616" alt="task4-2" src="https://github.com/user-attachments/assets/54fd7f79-1498-4631-a404-dc0ac1339605" />

<img width="1323" height="639" alt="task4-3" src="https://github.com/user-attachments/assets/4bfbabc9-d967-4556-83b4-cf0dfc7edc58" />

<img width="1336" height="618" alt="task4-4" src="https://github.com/user-attachments/assets/be913067-ddf3-45a0-b301-02738093feb5" />

<img width="1332" height="556" alt="task4-5" src="https://github.com/user-attachments/assets/84b66ebb-29b3-42ff-907d-a9864ca9ff9c" />


<img width="1332" height="556" alt="task4-6" src="https://github.com/user-attachments/assets/22996b47-8bb2-43e6-a27a-30b4c0d4ebbe" />


2. Set fail-fast: false — trigger a failure in one job and observe what happens to the rest

3. Write in your notes: What does fail-fast: true (the default) do vs false?

<img width="1314" height="631" alt="task5-2" src="https://github.com/user-attachments/assets/4e5d52a5-2fcb-4174-80a4-7736a8b63c17" />

## Task: Fail-Fast Behavior Observation

A failure condition was added for **Python 3.12** in the matrix workflow.

```yaml
- name: Fail only for Python 3.12
  if: matrix.python-version == '3.12'
  run: exit 1

#### Matrix Configuration

+ Operating Systems: ubuntu-latest, windows-latest

+ Python Versions: 3.10, 3.11, 3.12

+ fail-fast: false

+ Total Jobs

3 Python versions × 2 OS = 6 jobs


#### Observation

+ When the job running Python 3.12 fails:

+ Only the jobs with Python 3.12 fail.

+ The remaining jobs (3.10 and 3.11) continue running and complete successfully.

+ GitHub Actions does not cancel the remaining jobs because fail-fast is set to false.

#### Key Learning
``fail-fast: true (Default)``

If one job fails, the remaining jobs in the matrix are cancelled.

``fail-fast: false``

Even if a job fails, all other jobs continue running until completion.

