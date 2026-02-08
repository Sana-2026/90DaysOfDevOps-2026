Day 11 – File Ownership Challenge (chown & chgrp)

## Files & Directories Created

<img width="925" height="698" alt="files-dir" src="https://github.com/user-attachments/assets/4bcbd1c5-b591-4f39-ae57-a1af395460d2" />

## Ownership Changes
Task 1: Understanding Ownership
<img width="894" height="578" alt="task1" src="https://github.com/user-attachments/assets/e326bccb-3f6d-4644-84e5-4e964861158c" />


Owner → The user who created or owns the file and controls it fully.

Group → A collection of users allowed to access the file for teamwork.

👉 Owner = single user
👉 Group = multiple users


Task 2: Basic chown Operations 

<img width="992" height="316" alt="task2" src="https://github.com/user-attachments/assets/0d0be3b3-1260-4134-9bb8-ed373c674e0a" />


Task 3: Basic chgrp Operations

<img width="775" height="337" alt="task3-part2" src="https://github.com/user-attachments/assets/fb7a63df-a698-44a8-99eb-237b01a4076b" />

<img width="775" height="337" alt="task3-part2" src="https://github.com/user-attachments/assets/5a1c90f2-d32f-4738-9dfc-004f8d0a2bfc" />

Task 4: Combined Owner & Group Change

<img width="1095" height="541" alt="task4" src="https://github.com/user-attachments/assets/63c428d9-5a90-4700-9a90-99c774274548" />

Task 5: Recursive Ownership

<img width="1043" height="690" alt="task5" src="https://github.com/user-attachments/assets/8cc1b22e-cf62-4d72-8e82-a21ca97ccf74" />

<img width="1023" height="421" alt="task5-part2" src="https://github.com/user-attachments/assets/f15e6a6d-2667-4384-b8eb-82de4e171e07" />

Task 6: Practice Challenge

<img width="946" height="678" alt="task6" src="https://github.com/user-attachments/assets/f5a5f00d-9b28-495c-b563-e9e17884694e" />

<img width="1114" height="669" alt="task6-part2" src="https://github.com/user-attachments/assets/5748560a-6aa9-42f8-8696-21918406213c" />



## Commands Used

### View ownership
ls -l filename
ls -l heist-project

### Change owner only
sudo chown newowner filename
sudo chown berlin devops-file.txt

### Change group only
sudo chgrp newgroup filename
sudo chgrp professor:heist-team project-config.yaml

### Change both owner and group
sudo chown owner:group filename
sudo chown nairobi:vault-team bank-heist/escape-plan.txt

### Recursive change (directories)
sudo chown -R owner:group directory/
sudo chown -R professor:planners heist-project/


### Change only group with chown
sudo chown :groupname filename
sudo chown :heist-team team-notes.txt



## What I learned 👇

- Difference between user (owner) and group ownership

- How to change file owner using chown

- How to change file group using chgrp

- Applying ownership changes recursively for directories

- Verifying ownership using ls -l


