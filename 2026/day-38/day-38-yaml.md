## Challenge Tasks
### Task 1: Key-Value Pairs

1. Create person.yaml that describes yourself with:

+ name
+ role
+ experience_years
+ learning (a boolean)
  
[person.yml](https://github.com/Sana-2026/90DaysOfDevOps-2026/blob/master/2026/day-38/person.yml)

 Verify: Run cat person.yaml — does it look clean? No tabs?

 <img width="302" height="138" alt="image" src="https://github.com/user-attachments/assets/20e5d11c-814b-413f-afbe-4c7ba5c4f00b" />

+ The YAML structure looks clean

+ No tabs are used (YAML requires spaces for indentation)

+ Keys and values are properly aligned


### Task 2: Lists
Add to person.yaml:

+ tools — a list of 5 DevOps tools you know or are learning
+ hobbies — a list using the inline format [item1, item2]
  
[person.yml](https://github.com/Sana-2026/90DaysOfDevOps-2026/blob/master/2026/day-38/person.yml)


What are the two ways to write a list in YAML?

**Two ways to write a list in YAML**

1️⃣ **Block style (dash format)**  
➡ Each item starts with `-`

```yaml
tools:
  - Docker
  - Kubernetes
  - Jenkins
2️⃣ Inline style (bracket format)
➡ Items written inside [ ] separated by commas

tools: [Docker, Kubernetes, Jenkins]
```

### Task 3: Nested Objects
Create server.yaml that describes a server:

+ server with nested keys: name, ip, port
+ database with nested keys: host, name, credentials (nested further: user, password)

[server.yml](https://github.com/Sana-2026/90DaysOfDevOps-2026/new/master/2026/day-38)

Verify: Try adding a tab instead of spaces — what happens when you validate it?

<img width="363" height="419" alt="task3" src="https://github.com/user-attachments/assets/7690bc84-e177-4988-8afd-97c166735ca5" />

### Task 4: Multi-line Strings

In server.yaml, add a startup_script field using:

+ The | block style (preserves newlines)
+ The > fold style (folds into one line)

[server.yml](https://github.com/Sana-2026/90DaysOfDevOps-2026/new/master/2026/day-38)


**When to use `|` vs `>` in YAML ?**

➡ **`|` (Literal block style)**  
Use when **line breaks must be preserved exactly**, such as for **scripts, commands, or configuration files**.

➡ **`>` (Folded style)**  
Use when you want **multiple lines to be treated as a single line**, useful for **long text, messages, or descriptions**.

### Task 5: Validate Your YAML

+ Install yamllint or use an online validator
+ Validate both your YAML files
+ Intentionally break the indentation — what error do you get?
+ Fix it and validate again

### Task 6: Spot the Difference

Read both blocks and write what's wrong with the second one:

# Block 1 - correct
name: devops
tools:
  - docker
  - kubernetes
# Block 2 - broken
name: devops
tools:
- docker
  - kubernetes
