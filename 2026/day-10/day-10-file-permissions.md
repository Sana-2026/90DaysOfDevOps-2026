# Day 10 – File Permissions & File Operations 


## Files Created
- devops.txt
- notes.txt
- script.sh

### Task 1: Create Files

<img width="1066" height="648" alt="echo-redirection-operators" src="https://github.com/user-attachments/assets/d6e38312-0257-4161-8a6e-15e331631e65" />

<img width="860" height="505" alt="first-scripr-run" src="https://github.com/user-attachments/assets/4ae5e781-9ba5-479c-8310-c4acf7a3ffca" />

Task 2: Read Files

<img width="789" height="412" alt="head-tail-to view-contentsoffile" src="https://github.com/user-attachments/assets/0ebfa9b2-fd5f-465e-86d3-6f60dfc5ce8e" />

<img width="851" height="701" alt="vim-scrippt" src="https://github.com/user-attachments/assets/bd266e80-7e18-432e-81d3-3816e5a5fc19" />


## Permission Changes

### Task 3: Understand Permissions


ubuntu@ip-172-31-62-245:~/Day10$ ls -l
total 8

-rw-rw-r-- 1 ubuntu ubuntu   0 Feb  7 19:15 devops.txt

-rw-rw-r-- 1 ubuntu ubuntu  71 Feb  8 13:06 notes.txt

-rwxrwxr-x 1 ubuntu ubuntu 139 Feb  8 13:17 script.sh

📄 devops.txt

Its permissions are -rw-rw-r--.
This means the owner (ubuntu) can read and write the file.
Users in the ubuntu group can also read and write it.
Everyone else on the system can only read the file and cannot modify or execute it.
It’s a normal text file, so execution is not allowed for anyone.

📄 notes.txt

This file also has permissions -rw-rw-r--.
The owner and the group both have permission to read and write the file.
Other users can read the file but cannot change it or run it.
This is typical and correct for notes or configuration text files.

📜 script.sh

The permissions are -rwxrwxr-x.
The owner can read, write, and execute the script.
The group can also read, write, and execute it.
Other users are allowed to read and execute the script but cannot modify it.
Because the execute permission is set, this file can be run as a program.


### Task 4: Modify Permissions

1. Make script.sh executable → run it with ./script.sh
   
<img width="860" height="505" alt="first-scripr-run" src="https://github.com/user-attachments/assets/50c3f604-f1f0-408b-b0fe-dc201c27f664" />


2. Set devops.txt to read-only (remove write for all)
   
3. Set notes.txt to 640 (owner: rw, group: r, others: none)

<img width="795" height="427" alt="task4" src="https://github.com/user-attachments/assets/0e4dd44f-f538-4ba1-b40e-9da5dc9ec5a4" />


4. Create directory project/ with permissions 755

<img width="909" height="563" alt="task4-prt2" src="https://github.com/user-attachments/assets/7bab6999-79e1-4192-b9c2-f4092a436b02" />

### Task 5: Test Permissions 

   1. Try writing to a read-only file - what happens?
   2. Try executing a file without execute permission
      
<img width="1153" height="427" alt="task5" src="https://github.com/user-attachments/assets/bac65605-57f7-4370-bad6-ffc92f19dbb1" />



## Commands Used

📝 File & Script Practice
   echo "This is my first note" > notes.txt
   cat > notes.txt
   vim script.sh
   chmod +x script.sh
   ./script.sh
   ls -l

📄 Viewing File Content

   head -n 5 /etc/passwd
   head -10 /etc/passwd

📁 Making directory and changing permission

   mkdir project && chmod 755 project
   mkdir -m 755 project

## What I Learned


1️⃣ Different ways to create and read files in Linux
I practiced creating files using touch, cat, echo, and vim, and learned how to view file contents using cat, head, tail, and read-only mode in vim.

2️⃣ How Linux file permissions actually work
I understood the permission format rwxrwxrwx, how it maps to owner, group, and others, and how numeric values (4, 2, 1) translate into real access control.

3️⃣ Modifying permissions changes system behavior
By using chmod, I saw how making a script executable allows it to run, and how removing write or execute permissions immediately restricts actions like editing or running files.

4️⃣ Errors are part of learning permissions
Testing access helped me understand permission-denied errors when writing to read-only files or executing files without execute permission, which reflects real-world Linux security behavior.

