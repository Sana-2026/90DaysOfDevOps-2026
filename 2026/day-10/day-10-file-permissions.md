Day 10 – File Permissions & File Operations 


## Files Created
- devops.txt
- notes.txt
- script.sh

Task 1: Create Files
<img width="1066" height="648" alt="echo-redirection-operators" src="https://github.com/user-attachments/assets/d6e38312-0257-4161-8a6e-15e331631e65" />

<img width="860" height="505" alt="first-scripr-run" src="https://github.com/user-attachments/assets/4ae5e781-9ba5-479c-8310-c4acf7a3ffca" />

Task 2: Read Files

<img width="789" height="412" alt="head-tail-to view-contentsoffile" src="https://github.com/user-attachments/assets/0ebfa9b2-fd5f-465e-86d3-6f60dfc5ce8e" />
<img width="851" height="701" alt="vim-scrippt" src="https://github.com/user-attachments/assets/bd266e80-7e18-432e-81d3-3816e5a5fc19" />


## Permission Changes

Task 3: Understand Permissions


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


Task 4: Modify Permissions

1. Make script.sh executable → run it with ./script.sh
   
<img width="860" height="505" alt="first-scripr-run" src="https://github.com/user-attachments/assets/50c3f604-f1f0-408b-b0fe-dc201c27f664" />


2. Set devops.txt to read-only (remove write for all)
3. Set notes.txt to 640 (owner: rw, group: r, others: none)

<img width="909" height="563" alt="task4-prt2" src="https://github.com/user-attachments/assets/d79ffebb-3f2f-4971-a729-c625f4e82adb" />

4. Create directory project/ with permissions 755
   <img width="909" height="563" alt="task4-prt2" src="https://github.com/user-attachments/assets/7bab6999-79e1-4192-b9c2-f4092a436b02" />

Task 5: Test Permissions 



