
## What is DevSecOps?

Think of it like this:

**Without DevSecOps:**
> You build the app → deploy it → a security team finds a vulnerability weeks later → you scramble to fix it

**With DevSecOps:**
> You open a PR → the pipeline automatically checks for vulnerabilities → you fix it before it ever gets merged

**That's it.** DevSecOps = adding security checks to the pipeline you already have. Not a separate process — just a few extra steps.

---

## Key Principles (Keep These in Mind)

1. **Catch problems early** — A vulnerability found in a PR takes 5 minutes to fix. The same vulnerability found in production takes days.

2. **Automate the checks** — Don't rely on someone remembering to check. Let the pipeline do it every time.

3. **Block on critical issues** — If a scan finds a serious vulnerability, the pipeline should fail — just like a failing test.

4. **Never put secrets in code** — Use GitHub Secrets (you learned this on Day 44). No `.env` files, no hardcoded API keys.

5. **Give only the access needed** — Your workflow doesn't need write access to everything. Limit permissions.

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
## 🚨 CVEs Identified (Day 49 - Security Scan)

| Library                          | CVE ID          | Severity  | Description                                                                 | Fixed Version        |
|----------------------------------|-----------------|-----------|----------------------------------------|---------------------|
| tomcat-embed-core                | CVE-2025-24813  | CRITICAL  | Potential RCE / info disclosure via partial PUT                            | 10.1.35+            |
| tomcat-embed-core                | CVE-2026-29145  | CRITICAL  | Authentication bypass (CLIENT_CERT misconfiguration)                       | 10.1.53+            |
| spring-security-core             | CVE-2025-41232  | CRITICAL  | Authorization bypass in method security                                    | 6.4.6+              |
| spring-security-web              | CVE-2026-22732  | CRITICAL  | Security policy bypass & information disclosure                            | 6.5.9+              |
| thymeleaf                        | CVE-2026-40477  | CRITICAL  | Improper access control in expressions                                     | 3.1.4.RELEASE+      |
| thymeleaf                        | CVE-2026-40478  | CRITICAL  | Expression injection / improper neutralization                             | 3.1.4.RELEASE+      |
| thymeleaf-spring6                | CVE-2026-40477  | CRITICAL  | Same vulnerability via Spring integration                                  | 3.1.4.RELEASE+      |
| thymeleaf-spring6                | CVE-2026-40478  | CRITICAL  | Same vulnerability via Spring integration                                  | 3.1.4.RELEASE+      |

---

## 📊 Summary

- 🔴 Total Critical CVEs: **8 → reduced to 3 after fixes**
- 🛠️ Action Taken:
  - Upgraded dependencies via `dependencyManagement`
  - Rebuilt JAR
  - Re-ran Trivy scan

---

## 🧠 Key Learning

> Vulnerabilities often come from **transitive dependencies**, not just direct ones.

👉 Fix = Upgrade dependency versions or override using `dependencyManagement`


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


### Task 4: Add Permissions to Your Workflows
By default, workflows get broad permissions. Lock them down.

Add this block near the top of your workflow files (after `on:`):
```yaml
permissions:
  contents: read
```

If a workflow needs to comment on PRs, add:
```yaml
permissions:
  contents: read
  pull-requests: write
```

Update at least 2 of your existing workflow files with a `permissions` block.

Write in your notes: Why is it a good practice to limit workflow permissions? What could go wrong if a compromised action has write access to your repo?


#### 🔐 Why is it a good practice to limit workflow permissions?

Limiting workflow permissions follows the **Principle of Least Privilege**.

This means:
- Give only the **minimum access required**
- Reduce the risk if something goes wrong

#### ✅ Benefits:
- Prevents unauthorized changes to the repository
- Reduces impact of security breaches
- Keeps CI/CD pipelines more secure and controlled
- Avoids accidental deletions or modifications

---

#### ⚠️ What could go wrong if a compromised action has write access?

If a GitHub Action is compromised and has **write access**, it can:

- ❌ Modify or delete your source code
- ❌ Push malicious code into your repository
- ❌ Inject backdoors or vulnerabilities
- ❌ Leak sensitive data (API keys, tokens)
- ❌ Trigger unauthorized deployments
- ❌ Tamper with CI/CD pipelines

---

## 🧠 Key takeaway

> Always use **read-only permissions by default** and only add write access when absolutely necessary.

🔑 Secure pipelines = Safer applications

---

### Task 5: See the Full Secure Pipeline
Look at what your pipeline does now:

```
PR opened
  → build & test
  → dependency vulnerability check     ← NEW (Day 49)
  → PR checks pass or fail

Merge to main
  → build & test
  → Docker build
  → Trivy image scan (fail on CRITICAL) ← NEW (Day 49)
  → Docker push (only if scan passes)
  → deploy

Always active
  → GitHub secret scanning              ← NEW (Day 49)
  → push protection for secrets         ← NEW (Day 49)
```

Draw this diagram in your notes. You just built a **DevSecOps pipeline** — security is now part of your automation, not an afterthought.

<img width="1536" height="1024" alt="devsecops" src="https://github.com/user-attachments/assets/da1271cf-8f0a-44ba-9bd7-2fe360c75268" />

---

## Brownie Points (Optional — For the Curious)

### Pin Actions to Commit SHAs
Tags like `@v4` can be moved by the action author. For extra security, pin to the exact commit:
```yaml
# Instead of this:
uses: actions/checkout@v4

# Use this:
uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
```
This protects against supply chain attacks where a tag is silently changed.

### Upload Scan Results to GitHub Security Tab
Add SARIF output to Trivy and upload it — your scan results will appear in the repo's **Security** tab:
```yaml
- uses: aquasecurity/trivy-action@master
  with:
    image-ref: 'your-username/your-app:latest'
    format: 'sarif'
    output: 'trivy-results.sarif'
- uses: github/codeql-action/upload-sarif@v3
  with:
    sarif_file: 'trivy-results.sarif'
```

### Learn About OIDC (Keyless Authentication)
Instead of storing cloud credentials as long-lived secrets, GitHub Actions can use OIDC to get short-lived tokens automatically. Research: "GitHub Actions OIDC" — it's how production pipelines authenticate to AWS, GCP, and Azure without storing any keys.




