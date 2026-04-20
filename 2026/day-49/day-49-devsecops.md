## Challenge Tasks

### Task 1: Scan Your Docker Image for Vulnerabilities
Your Docker image might use a base image with known security issues. Let's find out.

Add this step to your main branch pipeline (after Docker build, before deploy):
```yaml
- name: Scan Docker Image for Vulnerabilities
  uses: aquasecurity/trivy-action@master
  with:
    image-ref: 'your-username/your-app:latest'
    format: 'table'
    exit-code: '1'
    severity: 'CRITICAL,HIGH'
```

What this does:
- `trivy` scans your Docker image for known CVEs (Common Vulnerabilities and Exposures)
- `format: 'table'` prints a readable table in the logs
- `exit-code: '1'` means **fail the pipeline** if CRITICAL or HIGH vulnerabilities are found
- If it passes, your image is clean — proceed to push and deploy

Push and check the Actions tab. Read the scan output.

**Verify:** Can you see the vulnerability table in the logs? Did it pass or fail?


<img width="1361" height="694" alt="task1-error-report" src="https://github.com/user-attachments/assets/72e307a6-aec7-4702-b113-481c4432a87e" />

<img width="1357" height="616" alt="task1" src="https://github.com/user-attachments/assets/fcd62a4f-8125-4ba2-ab71-557e05679ca5" />


Write in your notes: What CVEs (if any) were found? What base image are you using?

📝 **DevSecOps Scan Notes**

🔍 CVEs Found:

+ CVE-2025-41232 → Spring Security (authorization bypass)
+ CVE-2026-40477 → Thymeleaf (expression access issue)
+ CVE-2026-40478 → Thymeleaf (expression injection issue)

👉 Total: 3 CRITICAL vulnerabilities


### Task 2: Enable GitHub's Built-in Secret Scanning
GitHub can automatically detect if someone pushes a secret (API key, token, password) to your repo.

1. Go to your repo → Settings → **Code security and analysis**
2. Enable **Secret scanning**
3. If available, also enable **Push protection** — this blocks the push entirely if a secret is detected

That's it — no workflow changes needed. GitHub does this automatically.

Write in your notes:
- What is the difference between secret scanning and push protection?
- What happens if GitHub detects a leaked AWS key in your repo?

 #### 🔐 Secret Scanning vs Push Protection

#### 🔍 Secret Scanning
- Scans your **repository (past & present code)** for leaked secrets  
- Detects:
  - API keys  
  - AWS keys  
  - Tokens  
- Works **after the code is pushed**  
- Sends alerts when a secret is found  

👉 Think: **detect after leak**

---

#### 🚫 Push Protection
- Prevents secrets from being pushed  
- Runs **before the push completes**  
- Blocks the commit if a secret is detected  
- Shows warning and requires action  

👉 Think: **stop before leak**

---

#### ⚖️ Key Difference

| Feature        | Secret Scanning | Push Protection |
|---------------|----------------|----------------|
| When it works | After push     | Before push    |
| Action        | Alerts         | Blocks commit  |
| Purpose       | Detection      | Prevention     |

---

#### 🚨 What happens if GitHub detects a leaked AWS key?

- ⚠️ GitHub flags the secret immediately  
- 📧 Sends alert to repository owner  
- 🔐 May notify AWS  
- ❌ With push protection → push is **blocked**  
- 🧹 Required actions:
  - Remove the key from code  
  - Rotate (regenerate) the AWS key  
  - Commit clean code  

---

#### 🎯 Summary

- Secret Scanning = **detect leaks**  
- Push Protection = **prevent leaks**  
- Always rotate exposed keys 🔑

---

### Task 3: Scan Dependencies for Known Vulnerabilities
If your app uses packages (pip, npm, etc.), those packages might have known vulnerabilities.

Add this to your **PR pipeline** (not the main pipeline):
```yaml
- name: Check Dependencies for Vulnerabilities
  uses: actions/dependency-review-action@v4
  with:
    fail-on-severity: critical
```

This checks any **new** dependencies added in the PR against a vulnerability database. If a dependency has a critical CVE, the PR check fails.

Test it:
1. Open a PR that adds a package to your app
2. Check the Actions tab — did the dependency review run?

**Verify:** Does the dependency review show up as a check on your PR?

<img width="1341" height="630" alt="task3" src="https://github.com/user-attachments/assets/0443a84e-2970-4edf-8351-81d31ff8f5d7" />
---


