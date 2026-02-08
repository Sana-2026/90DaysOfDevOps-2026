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

Permissions: -rw-rw-r--

User type	            Read	Write	Execute
Owner (ubuntu)	       ✅	    ✅	  ❌
Group (ubuntu)	       ✅	    ✅	  ❌
Others	               ✅	    ❌	  ❌

👉 It’s a normal text file. Anyone can read, only owner & group can edit.


📄 notes.txt
Permissions: -rw-rw-r--

User type	            Read	Write	Execute
Owner (ubuntu)	        ✅	    ✅	  ❌
Group (ubuntu)	        ✅	    ✅	  ❌
Others	                ✅	    ❌	  ❌

👉 It’s a normal text file. Anyone can read, only owner & group can edit.4



