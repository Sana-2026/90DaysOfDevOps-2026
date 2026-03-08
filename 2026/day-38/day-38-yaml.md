## Challenge Tasks
### Task 1: Key-Value Pairs

1. Create person.yaml that describes yourself with:

+ name
+ role
+ experience_years
+ learning (a boolean)
[person.yml]()

 Verify: Run cat person.yaml — does it look clean? No tabs?

 <img width="302" height="138" alt="image" src="https://github.com/user-attachments/assets/20e5d11c-814b-413f-afbe-4c7ba5c4f00b" />

+ The YAML structure looks clean

+ No tabs are used (YAML requires spaces for indentation)

+ Keys and values are properly aligned


### Task 2: Lists
Add to person.yaml:

+ tools — a list of 5 DevOps tools you know or are learning
+ hobbies — a list using the inline format [item1, item2]
  
Write in your notes: What are the two ways to write a list in YAML?

### Task 3: Nested Objects
Create server.yaml that describes a server:

+ server with nested keys: name, ip, port
+ database with nested keys: host, name, credentials (nested further: user, password)
  
Verify: Try adding a tab instead of spaces — what happens when you validate it?

### Task 4: Multi-line Strings

In server.yaml, add a startup_script field using:

+ The | block style (preserves newlines)
+ The > fold style (folds into one line)
+ Write in your notes: When would you use | vs >?

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
