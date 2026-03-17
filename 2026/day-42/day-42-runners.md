## Day 42 – Runners: GitHub-Hosted & Self-Hosted

### Task 1: GitHub-Hosted Runners

1. Create a workflow with 3 jobs, each on a different OS:
+ ubuntu-latest
+ windows-latest
+ macos-latest
  
2. In each job, print:
+ The OS name
+ The runner's hostname
+ The current user running the job
Watch all 3 run in parallel

<img width="1338" height="469" alt="task2-parta" src="https://github.com/user-attachments/assets/92763a06-cfd1-4428-b793-1113255e7695" />

<img width="1366" height="634" alt="task2" src="https://github.com/user-attachments/assets/733f66bc-b23a-4051-9744-ebe02d20111c" />

3. Write in your notes: What is a GitHub-hosted runner? Who manages it

A GitHub-hosted runner is a virtual machine (VM) provided by GitHub that automatically runs your workflows in GitHub Actions.

When a workflow is triggered (for example on push or pull_request), GitHub starts a temporary VM with the required operating system (Linux, Windows, or macOS) and executes the workflow steps.

Key points:

+ Pre-configured with common tools (Git, Docker, languages, etc.)

+ Automatically created when a workflow starts

+ Deleted after the job finishes

 + No manual infrastructure setup required

Who manages it? ⚙️

The infrastructure for GitHub-hosted runners is fully managed by GitHub.

That means GitHub handles:

+ Server provisioning

+ OS installation

+ Security updates

+ Maintenance

+ Scaling of runners

Developers only write the workflow YAML, and GitHub takes care of running it.

### Task 2: Explore What's Pre-installed
1. On the ubuntu-latest runner, run a step that prints:
+ Docker version
+ Python version
+ Node version
+ Git version

Look up the GitHub docs for the full list of pre-installed software on ubuntu-latest

### Pre-installed Software on `ubuntu-latest` (GitHub-hosted runner)

| Category | Examples of Pre-installed Tools |
|--------|----------------------------------|
| **Programming Languages & Runtimes** | Python, Node.js, Java, Go, Ruby, .NET, PHP, Swift, Kotlin, Julia |
| **DevOps & Container Tools** | Docker, Docker Compose, kubectl, Kind, Terraform, Pulumi |
| **Package Managers** | npm, yarn, pip, Maven, Gradle, Homebrew, Composer, Bundler |
| **Cloud CLI Tools** | AWS CLI, Google Cloud CLI, Azure CLI, OpenShift CLI |
| **Development Utilities** | Git, curl, wget, jq, make, gcc, clang |
| **Browsers for Testing** | Google Chrome, Firefox, Microsoft Edge, ChromeDriver, WebDriver |

**Note:**  
GitHub-hosted runners come with many pre-installed tools so workflows can run builds, tests, and deployments **without needing manual setup or installation**.


<img width="1338" height="621" alt="task2" src="https://github.com/user-attachments/assets/e91e84b9-edc3-484c-9af2-c1deb97bc53f" />

<img width="1366" height="610" alt="task2-partb" src="https://github.com/user-attachments/assets/ccdbb7e0-8a30-4b10-904b-d1be030067eb" />


2. Write in your notes: Why does it matter that runners come with tools pre-installed?

In [GitHub Actions](https://github.com/features/actions), 

GitHub-hosted runners already include common development tools like **Docker, Python, Node.js, and Git**.

### Key Reasons

#### Faster workflow execution 🚀
Tools are already available, so the workflow does not waste time installing them.

#### Simpler CI/CD configuration 🧩
You can directly run commands without writing extra installation steps.

#### Consistency across runs 🔁
Every runner starts with the same environment, reducing **“works on my machine”** issues.

#### Less infrastructure management 🛠️
The environment is maintained by **GitHub**, so developers can focus only on the workflow logic.

### Task 3: Set Up a Self-Hosted Runner

1. Go to your GitHub repo → Settings → Actions → Runners → New self-hosted runner
   
2. Choose Linux as the OS
  
3. Follow the instructions to download and configure the runner on:
 
+ Your local machine, OR
+ A cloud VM (EC2, Utho, or any VPS)
+ Start the runner — verify it shows as Idle in GitHub

Verify: Your runner appears in the Runners list with a green dot.

<img width="1364" height="705" alt="task3" src="https://github.com/user-attachments/assets/e345deac-3038-4a75-9ee5-980b69205475" />

### Task 4: Use Your Self-Hosted Runner

1. Create .github/workflows/self-hosted.yml

2. Set runs-on: self-hosted

3.Add steps that:
 + Print the hostname of the machine (it should be YOUR machine/VM)
 + Print the working directory
 + Create a file and verify it exists on your machine after the run
   
4. Trigger it and watch it run on your own hardware
   
Verify: Check your machine — is the file there?

<img width="1364" height="728" alt="Image" src="https://github.com/user-attachments/assets/333c1be7-602c-4e1d-9448-d2478bf11a3a" />

<img width="1357" height="620" alt="Image" src="https://github.com/user-attachments/assets/a108c3e8-26a3-4776-80fc-d22df15acefb" />

<img width="1364" height="127" alt="Image" src="https://github.com/user-attachments/assets/bd65d406-f5b7-4f44-afad-8a9c7dd73ea7" />

### Task 5: Labels

1. Add a label to your self-hosted runner (e.g., my-linux-runner)
2. Update your workflow to use runs-on: [self-hosted, my-linux-runner]

<img width="1355" height="722" alt="task5" src="https://github.com/user-attachments/assets/94f00065-e036-4ddb-96af-31cafb8d5d55" />

<img width="1335" height="411" alt="task5-b" src="https://github.com/user-attachments/assets/77ddfd33-e55d-4b41-8627-a7ceea8e9959" />

<img width="872" height="267" alt="task5-c" src="https://github.com/user-attachments/assets/07f55e8a-2e62-48dc-b213-7da1133963d8" />

3. Trigger it — does it still pick up the job?
Write in your notes: Why are labels useful when you have multiple self-hosted runners?

Because labels help GitHub choose the correct runner based on machine type, purpose, or environment. They make sure a workflow runs on the exact self-hosted machine you want.

## Task 6: GitHub-Hosted vs Self-Hosted

| Feature | GitHub-Hosted | Self-Hosted |
|---|---|---|
| **Who manages it?** | GitHub manages and maintains the runner | You manage and maintain the runner |
| **Cost** | Free minutes are limited, then paid based on usage | No GitHub runner-minute cost, but you pay for your own machine/server |
| **Pre-installed tools** | Comes with many pre-installed tools like Git, Docker, Python, Node.js, etc. | Depends on what **you** install and maintain |
| **Good for** | Quick setup, simple CI/CD, learning, small to medium projects | Custom environments, private network access, special hardware, full control |
| **Security concern** | Less infrastructure to manage, but code runs on GitHub-managed machines | You are responsible for securing the machine, updates, secrets, and access control |















