
# Day 61 -- Introduction to Terraform and Your First AWS Infrastructure

## Task
You have been deploying containers, writing CI/CD pipelines, and orchestrating workloads on Kubernetes. But who creates the servers, networks, and clusters underneath? Today you start your Infrastructure as Code journey with Terraform -- the tool that lets you define, provision, and manage cloud infrastructure by writing code.

By the end of today, you will have created real AWS resources using nothing but a `.tf` file and a terminal.

---

## Challenge Tasks

### Task 1: Understand Infrastructure as Code
Before touching the terminal, research and write short notes on:

1. What is Infrastructure as Code (IaC)? Why does it matter in DevOps?
   
- **Infrastructure as Code (IaC)** is the practice of **managing and provisioning infrastructure using code instead of manual processes.**
- Infrastructure is defined in **configuration files**.
- IaC tools (e.g., **Terraform**) read these files and create or update the infrastructure automatically.

---

**Why does IaC matter in DevOps?**

Easy way to remember: **ACCRVS**

| Letter | Meaning | Benefit |
|--------|---------|---------|
| **A** | **Automation** | Eliminates manual infrastructure setup. |
| **C** | **Consistency** | Ensures Dev, Test, and Production environments are identical. |
| **C** | **Collaboration** | Teams can review and manage infrastructure code using Git. |
| **R** | **Repeatability** | The same infrastructure can be recreated anytime. |
| **V** | **Version Control** | Tracks infrastructure changes and allows rollbacks. |
| **S** | **Scalability & Speed** | Enables quick provisioning and easy scaling of infrastructure. |

---



 **Infrastructure as Code (IaC)** is the practice of provisioning and managing infrastructure using code instead of manual configuration. It enables automation, consistency, version control, and repeatable deployments. By using tools like Terraform, organizations can create, update, and manage infrastructure efficiently while reducing manual errors and improving deployment speed.

---

 **Key Points to Remember**

- Infrastructure is managed using **code**.
- Uses **configuration files** to define resources.
- **Automates** infrastructure provisioning.
- Ensures **consistent** environments.
- Supports **Git-based version control**.
- Enables **repeatable** deployments.
- Reduces **human errors**.
- Improves **speed** and **scalability**.

---

 **Write infrastructure as code, store it in Git, and deploy it automatically.**

2. What problems does IaC solve compared to manually creating resources in the AWS console?
    
##### Problems with Manual Resource Creation

- ❌ **Time-Consuming** – Creating resources manually takes longer.
- ❌ **Human Errors** – Easy to misconfigure settings or forget steps.
- ❌ **Inconsistent Environments** – Dev, Test, and Production may end up with different configurations.
- ❌ **Difficult to Reproduce** – Recreating the same infrastructure requires repeating manual steps.
- ❌ **No Version Control** – Changes made in the AWS Console are not automatically tracked.
- ❌ **Poor Collaboration** – Team members cannot easily review or approve infrastructure changes.
- ❌ **Hard to Scale** – Managing hundreds of resources manually becomes difficult and error-prone.
- ❌ **Disaster Recovery Challenges** – Rebuilding infrastructure after a failure is slow and unreliable.

---

##### How Infrastructure as Code (IaC) Solves These Problems

| Manual AWS Console | Infrastructure as Code (IaC) |
|--------------------|------------------------------|
| Manual clicks | Infrastructure is created using code |
| Slow provisioning | Automated and faster deployments |
| Human errors | Consistent and repeatable deployments |
| Different environments | Identical environments every time |
| Difficult to recreate | Recreate infrastructure with a single command |
| No version history | Infrastructure code is stored in Git |
| Limited collaboration | Teams can review code using pull requests |
| Hard to scale | Easily create and manage large-scale infrastructure |

---

Manually creating infrastructure in the AWS Console is time-consuming, error-prone, and difficult to reproduce consistently across environments. Infrastructure as Code (IaC) solves these problems by automating infrastructure provisioning through code. It provides consistency, repeatability, version control, collaboration, faster deployments, and easier disaster recovery, making infrastructure management more reliable and scalable.

---

3. How is Terraform different from AWS CloudFormation, Ansible, and Pulumi?
   
## Comparison Table

| Feature | Terraform | AWS CloudFormation | Ansible | Pulumi |
|---------|-----------|--------------------|----------|---------|
| **Purpose** | Infrastructure Provisioning (IaC) | AWS Infrastructure Provisioning | Configuration Management & Automation | Infrastructure Provisioning (IaC) |
| **Cloud Support** | Multi-cloud (AWS, Azure, GCP, etc.) | AWS only | Multi-cloud | Multi-cloud |
| **Language Used** | HCL (HashiCorp Configuration Language) | JSON / YAML | YAML | General-purpose languages (Python, Java, Go, TypeScript, C#) |
| **State Management** | Uses a state file (`terraform.tfstate`) | Managed by AWS | Stateless | Uses a state file (managed by Pulumi) |
| **Best For** | Provisioning cloud infrastructure | Managing AWS infrastructure | Configuring servers after provisioning | Developers who prefer programming languages |

---

# Key Differences

## Terraform
- Uses **HCL**, a simple declarative language.
- Supports **multiple cloud providers**.
- Keeps track of infrastructure using a **state file**.
- Best for provisioning cloud infrastructure.

---

## AWS CloudFormation
- AWS's **native IaC service**.
- Works **only with AWS**.
- Uses **JSON or YAML** templates.
- Best when your infrastructure is entirely on AWS.

---

## Ansible
- Primarily a **Configuration Management** tool.
- Used to install software, configure servers, and automate operational tasks.
- Agentless (uses SSH/WinRM).
- Can provision infrastructure, but its main strength is **configuration after resources are created**.

**Example:**
- Terraform → Creates an EC2 instance.
- Ansible → Installs Nginx, configures the server, and deploys your application.

---

## Pulumi
- Uses **real programming languages** like Python, TypeScript, Java, Go, and C#.
- Supports **multiple cloud providers**.
- Also maintains a **state file**.
- Ideal for developers who want to use familiar programming languages instead of a domain-specific language.

---

##### Easy Way to Remember

| Tool | Think of it as... |
|------|--------------------|
| **Terraform** | Create infrastructure anywhere 🌍 |
| **CloudFormation** | Create infrastructure only on AWS ☁️ |
| **Ansible** | Configure servers after they're created ⚙️ |
| **Pulumi** | Create infrastructure using programming languages 💻 |

---

 **Terraform** is a multi-cloud Infrastructure as Code tool that uses HCL to provision and manage infrastructure. **AWS CloudFormation** is AWS's native IaC service and works only with AWS using JSON or YAML templates. **Ansible** is primarily a configuration management and automation tool used to configure servers after infrastructure is provisioned. **Pulumi** is a multi-cloud IaC tool like Terraform, but it uses general-purpose programming languages such as Python, TypeScript, and Java instead of HCL.

---

##### One-Line Memory Trick

- **Terraform** → **Provision infrastructure anywhere.**
- **CloudFormation** → **Provision infrastructure only on AWS.**
- **Ansible** → **Configure infrastructure.**
- **Pulumi** → **Provision infrastructure using code (Python, TypeScript, Java, etc.).**

4. What does it mean that Terraform is "declarative" and "cloud-agnostic"?



---

### Task 2: Install Terraform and Configure AWS
1. Install Terraform:
```bash
# macOS
brew tap hashicorp/tap
brew install hashicorp/tap/terraform

# Linux (amd64)
wget -O - https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install terraform

# Windows
choco install terraform
```

2. Verify:
```bash
terraform -version
```

3. Install and configure the AWS CLI:
```bash
aws configure
# Enter your Access Key ID, Secret Access Key, default region (e.g., ap-south-1), output format (json)
```

4. Verify AWS access:
```bash
aws sts get-caller-identity
```

You should see your AWS account ID and ARN.

---

### Task 3: Your First Terraform Config -- Create an S3 Bucket
Create a project directory and write your first Terraform config:

```bash
mkdir terraform-basics && cd terraform-basics
```

Create a file called `main.tf` with:
1. A `terraform` block with `required_providers` specifying the `aws` provider
2. A `provider "aws"` block with your region
3. A `resource "aws_s3_bucket"` that creates a bucket with a globally unique name

Run the Terraform lifecycle:
```bash
terraform init      # Download the AWS provider
terraform plan      # Preview what will be created
terraform apply     # Create the bucket (type 'yes' to confirm)
```

Go to the AWS S3 console and verify your bucket exists.

**Document:** What did `terraform init` download? What does the `.terraform/` directory contain?

---

### Task 4: Add an EC2 Instance
In the same `main.tf`, add:
1. A `resource "aws_instance"` using AMI `ami-0f5ee92e2d63afc18` (Amazon Linux 2 in ap-south-1 -- use the correct AMI for your region)
2. Set instance type to `t2.micro`
3. Add a tag: `Name = "TerraWeek-Day1"`

Run:
```bash
terraform plan      # You should see 1 resource to add (bucket already exists)
terraform apply
```

Go to the AWS EC2 console and verify your instance is running with the correct name tag.

**Document:** How does Terraform know the S3 bucket already exists and only the EC2 instance needs to be created?

---

### Task 5: Understand the State File
Terraform tracks everything it creates in a state file. Time to inspect it.

1. Open `terraform.tfstate` in your editor -- read the JSON structure
2. Run these commands and document what each returns:
```bash
terraform show                          # Human-readable view of current state
terraform state list                    # List all resources Terraform manages
terraform state show aws_s3_bucket.<name>   # Detailed view of a specific resource
terraform state show aws_instance.<name>
```

3. Answer these questions in your notes:
   - What information does the state file store about each resource?
   - Why should you never manually edit the state file?
   - Why should the state file not be committed to Git?

---

### Task 6: Modify, Plan, and Destroy
1. Change the EC2 instance tag from `"TerraWeek-Day1"` to `"TerraWeek-Modified"` in your `main.tf`
2. Run `terraform plan` and read the output carefully:
   - What do the `~`, `+`, and `-` symbols mean?
   - Is this an in-place update or a destroy-and-recreate?
3. Apply the change
4. Verify the tag changed in the AWS console
5. Finally, destroy everything:
```bash
terraform destroy
```
6. Verify in the AWS console -- both the S3 bucket and EC2 instance should be gone

---

## Hints
- S3 bucket names must be globally unique -- use something like `terraweek-<yourname>-2026`
- AMI IDs are region-specific -- search "Amazon Linux 2 AMI" in your region's EC2 launch wizard
- `terraform fmt` auto-formats your `.tf` files -- run it before committing
- `terraform validate` checks for syntax errors without connecting to AWS
- The `.terraform/` directory contains downloaded provider plugins
- Add `*.tfstate`, `*.tfstate.backup`, and `.terraform/` to your `.gitignore`

---

## Documentation
Create `day-61-terraform-intro.md` with:
- IaC explanation in your own words (3-4 sentences)
- Screenshot of `terraform apply` creating your S3 bucket and EC2 instance
- Screenshot of the resources in the AWS console
- What each Terraform command does (init, plan, apply, destroy, show, state list)
- What the state file contains and why it matters

---

## Submission
1. Add `day-61-terraform-intro.md` to `2026/day-61/`
2. Commit and push to your fork

---

## Learn in Public
Share on LinkedIn: "Started the TerraWeek Challenge -- installed Terraform, created my first S3 bucket and EC2 instance using code, and destroyed it all with one command. Infrastructure as Code just clicked."

`#90DaysOfDevOps` `#TerraWeek` `#DevOpsKaJosh` `#TrainWithShubham`

Happy Learning!
**TrainWithShubham**
