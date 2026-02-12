# Day 09  Linux User & Group Management Challenge

## Users & Groups Created
- Users: tokyo, berlin, professor, nairobi
- Groups: developers, admins, project-team
<img width="1142" height="425" alt="task1-3user-created" src="https://github.com/user-attachments/assets/a0cfe018-ab09-4e8a-ab94-6bf89ea77707" />
<img width="819" height="305" alt="groups-created" src="https://github.com/user-attachments/assets/32f0a486-e3c6-4411-8ad3-d2c117b24f16" />

<img width="1201" height="96" alt="task5-user-created" src="https://github.com/user-attachments/assets/fc06e8bf-3558-40c3-bb65-162da3cc4e50" />

## Group Assignments
[List who is in which groups]
<img width="1057" height="386" alt="assigned-groups-to -user" src="https://github.com/user-attachments/assets/3cec2d73-137d-4250-a405-5f8de09410a4" />

## Directories Created
[List directories with permissions]
<img width="1045" height="407" alt="task4" src="https://github.com/user-attachments/assets/a1455a03-2b7f-406d-8ec3-3022021ae606" />
<img width="1335" height="564" alt="task5-comp" src="https://github.com/user-attachments/assets/6271935b-a682-4ae0-a5fa-83fc189104df" />

## Commands Used

sudo useradd -m tokyo

sudo useradd -m berlin

sudo useradd -m professor

cat /etc/passwd

getent group developers

getent group admins

sudo usermod -aG developers,admins berlin

sudo usermod -aG developers tokyo

sudo usermod -aG admins professor

id tokyo

id berlin

id professor

sudo mkdir /opt/dev-project

sudo -u tokyo touch /opt/dev-project/tokyo.txt

sudo -u berlin touch /opt/dev-project/berlin.txt

sudo chown :developers /opt/dev-project  

sudo chmod 775 /opt/dev-project

sudo -u tokyo touch /opt/dev-project/tokyo.txt

sudo -u berlin touch /opt/dev-project/berlin.txt

sudo groupadd project-team

sudo usermod -aG project-team nairobi

sudo usermod -aG project-team tokyo

sudo mkdir /opt/team-workspace

ls -ld /opt/team-workspace

sudo -u nairobi touch /opt/team-workspace/nairobi.txt

ls -l /opt/team-workspace

sudo chgrp project-team /opt/team-workspace

sudo chmod 775 /opt/team-workspace

## What I Learned
1️⃣ User & group management in Linux

 Learned how to create users with home directories, create custom groups, and safely add users to multiple groups without breaking existing access.

2️⃣ Group-based permissions for collaboration

Practiced setting group ownership (chown / chgrp) and permissions (chmod 775) to build shared workspaces where teams can collaborate securely.

3️⃣ Verify like a real sysadmin

I didn’t just configure —  verified using id, /etc/passwd, /etc/group, and real permission tests (sudo -u user touch file).
