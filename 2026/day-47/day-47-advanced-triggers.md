# Day 47 – Advanced Triggers: PR Events, Cron Schedules & Event-Driven Pipelines
## Task 1: Pull Request Event Types

Create `.github/workflows/pr-lifecycle.yml` that triggers on `pull_request` with **specific activity types**:

1. Trigger on: `opened`, `synchronize`, `reopened`, `closed`
2. Add steps that:
   - Print which event type fired: `${{ github.event.action }}`
   - Print the PR title: `${{ github.event.pull_request.title }}`
   - Print the PR author: `${{ github.event.pull_request.user.login }}`
   - Print the source branch and target branch
3. Add a conditional step that only runs when the PR is **merged** (closed + merged = true)

Test it: create a PR, push an update to it, then merge it. Watch the workflow fire each time with a different event type.

<img width="973" height="610" alt="task1" src="https://github.com/user-attachments/assets/e76cd0b8-4c24-47e7-8afb-ea0613c65009" />


<img width="1339" height="485" alt="task1-a" src="https://github.com/user-attachments/assets/eec6be29-eb03-4e78-a576-a99210927403" />


<img width="1366" height="612" alt="task1-pr-run" src="https://github.com/user-attachments/assets/98f15adb-a261-4dea-af2a-3961225256a5" />


<img width="1366" height="512" alt="task1-pr-run-syncr" src="https://github.com/user-attachments/assets/8a2158b2-7d7b-4a08-8a06-c2ce2c94f92e" />


<img width="1349" height="603" alt="task-1-run-merge-closed" src="https://github.com/user-attachments/assets/b1e39121-788c-4c87-a621-e7aca585dcf7" />


<img width="1366" height="597" alt="task1-reopen" src="https://github.com/user-attachments/assets/69d746f1-1fca-4144-9adf-2e37fe571729" />

---

## Task 2: PR Validation Workflow

Create `.github/workflows/pr-checks.yml` — a real-world PR gate:

1. Trigger on `pull_request` to `main`
2. Add a job `file-size-check` that:
   - Checks out the code
   - Fails if any file in the PR is larger than 1 MB
3. Add a job `branch-name-check` that:
   - Reads the branch name from `${{ github.head_ref }}`
   - Fails if it doesn't follow the pattern `feature/*`, `fix/*`, or `docs/*`
4. Add a job `pr-body-check` that:
   - Reads the PR body: `${{ github.event.pull_request.body }}`
   - Warns (but doesn't fail) if the PR description is empty

**Verify:** Open a PR from a badly named branch — does the check fail?

<img width="1345" height="629" alt="task2" src="https://github.com/user-attachments/assets/c6a9c6c5-14a9-4cf3-b16b-984bea275b2e" />

### Task 3: Scheduled Workflows (Cron Deep Dive)

Create ``.github/workflows/scheduled-tasks.yml``:

Add a ``schedule`` trigger with cron: ``'30 2 * * 1'`` (every Monday at 2:30 AM UTC)
Add another cron entry: ``'0 */6 * * *'`` (every 6 hours)
In the job, print which schedule triggered using ``${{ github.event.schedule }}``
Add a step that acts as a **health check** — curl a URL and check the response code
**Important**: Also add ``workflow_dispatch`` so you can test it manually without waiting for the schedule.

<img width="1318" height="616" alt="task3" src="https://github.com/user-attachments/assets/4777fd77-42c9-48eb-9eac-9a092506c5e5" />

Write in your notes:

+ The cron expression for: every weekday at 9 AM IST ``30 3 * * 1-5``
     + 30 → minute 30
     + 3 → 3 AM UTC
     + * * → every day/month
     + 1-5 → Monday to Friday
    
+ The cron expression for: first day of every month at midnight ``30 18 28-31 * *``
+ Why GitHub says scheduled workflows may be delayed or skipped on inactive repos
 + Not exact timing (best-effort system)
 + Less priority for inactive repos
 + GitHub server load can delay jobs
 + Only runs from default branch
 + Disabled Actions = no schedule run




