# Day 49 – DevSecOps: Add Security to Your CI/CD Pipeline

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

- 🔴 Total Critical CVEs: **8 → reduced to 3 after fixes** later to zero
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

<img width="1341" height="630" alt="task3" src="https://github.com/user-attachments/assets/822e372b-2c7e-43e1-a78e-de584110312e" />

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

### 🚀 DevSecOps Enhancement – Docker Pipeline

### 🔐 What we added
- Integrated **Trivy vulnerability scanning** into Docker workflow  
- Configured scan to **fail pipeline on CRITICAL CVEs** (`exit-code: 1`)  
- Generated **SARIF security reports** from scan results  
- Uploaded reports to **GitHub Security tab (Code Scanning Alerts)**  
- **Pinned all GitHub Actions to commit SHAs** for supply chain security  


---

### 🔧 What we changed
- Updated Docker workflow to include **security scan before push**
- Modified pipeline flow to **block image push if vulnerabilities found**
- Ensured **Trivy runs after build and before push**

---

### ⚙️ Updated Pipeline Flow

Build Docker Image
→ Trivy Scan (fail on CRITICAL)
→ Upload SARIF Report
→ Push Docker Image (only if scan passes)

### 🧠 Key Concepts

- **CVE (Common Vulnerabilities and Exposures)**  
  → Publicly disclosed security vulnerabilities with unique IDs (e.g., CVE-2026-22732)  
  → Helps identify, track, and fix known security issues in dependencies and images  

- **Trivy**  
  → Open-source security scanner for:
    - Container images  
    - OS packages (Alpine, Debian, etc.)  
    - Application dependencies (Java, Node, Python)  
  → Detects vulnerabilities, misconfigurations, and secrets  
  → Can enforce security using `exit-code` to fail pipelines  

- **SARIF (Static Analysis Results Interchange Format)**  
  → Standard JSON format for security scan results  
  → Enables integration with GitHub **Code Scanning (Security tab)**  
  → Makes vulnerabilities visible, trackable, and auditable  

- **Pinned Actions (Commit SHA)**  
  → Locks GitHub Actions to a fixed commit instead of mutable tags (`@v4`, `@latest`)  
  → Prevents **supply chain attacks** where action code could be altered  
  → Ensures reproducible and secure CI/CD runs  

- **$GITHUB_OUTPUT**  
  → Mechanism to pass data between steps/jobs in GitHub Actions  
  → Used to expose values like `image_url` for downstream jobs (deploy, notify, etc.)  

- **Shift Left Security**  
  → Security is applied early in the development lifecycle (CI stage)  
  → Reduces risk, cost, and effort compared to fixing issues in production  

- **Fail-Fast Principle**  
  → Pipeline stops immediately when critical vulnerabilities are detected  
  → Prevents insecure artifacts from progressing further (build → push → deploy)  

- **DevSecOps**  
  → Integration of **Security into DevOps pipelines**  
  → Automates vulnerability detection, enforcement, and visibility  
  → Ensures security is continuous, not a one-time activity  

### ✅ Why this is important
- 🚫 Prevents vulnerable Docker images from being pushed  
- 🔐 Secures CI/CD pipeline from malicious action updates  
- 👀 Provides visibility in GitHub **Security tab**  
- ⚡ Automates security checks (no manual effort required)  

---

### 🎯 Outcome
- Built a **secure Docker CI/CD pipeline**  
- Implemented **DevSecOps best practices**  
- Ensured **security is enforced automatically**  

### 🔐 OIDC (Keyless Authentication) – DevSecOps Upgrade

### 🚀 What is OIDC?
**OIDC (OpenID Connect)** allows GitHub Actions to authenticate with cloud providers  
(**AWS, GCP, Azure**) **without storing secrets**.

Instead of using long-lived credentials (like API keys), it uses:
→ **short-lived, temporary tokens**

---

### ⚙️ How it works
1. GitHub workflow requests a token
2. GitHub issues an **OIDC token**
3. Cloud provider verifies the token
4. Temporary credentials are granted (limited time + permissions)

---

### 🔄 Flow
GitHub Action
→ Request OIDC token
→ Cloud Provider validates
→ Temporary access granted
→ Perform deployment


---

### 🔐 Why OIDC is better
- ❌ No hardcoded secrets in repo
- ⏳ Tokens expire automatically
- 🔒 Reduced risk of credential leaks
- 🎯 Fine-grained access control (IAM roles)
- 🛡️ Industry-standard secure authentication

---

### ⚠️ Problem with traditional approach

Store AWS keys in GitHub Secrets
→ If leaked → Full access compromised

---

### ✅ OIDC Solution

No stored secrets
→ Temporary access only
→ Automatically expires

---

### 🧠 Key Concepts
- **Federated Identity** → Trust between GitHub & cloud provider  
- **IAM Role (AWS)** → Defines what actions are allowed  
- **Trust Policy** → Allows GitHub to assume the role  
- **Short-lived tokens** → Valid only for a limited time  

---

### 🎯 Outcome
- Eliminated need for long-lived credentials  
- Improved pipeline security significantly  
- Enabled **production-grade authentication mechanism**  

---

### 🏆 Why this matters (Real World)
- Used in **enterprise CI/CD pipelines**
- Required for **secure cloud deployments**
- Core concept in **DevSecOps & Zero Trust security**

---

### 🚀 Final Takeaway
👉 OIDC = **Secure, keyless, temporary authentication for CI/CD pipelines**
