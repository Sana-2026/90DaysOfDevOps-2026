# 🛠️ Incident Drill Runbook — SSH Service (Linux)

Target service: ssh
Goal: Quick system sanity + SSH health check

## 1️⃣ Environment Basics

<img width="1350" height="351" alt="commands" src="https://github.com/user-attachments/assets/5a04d98c-d2f0-4b02-8e0f-276d9656a54c" />

Observation: Kernel and architecture look standard for Ubuntu EC2.


## 2️⃣ Filesystem Sanity check

<img width="1077" height="193" alt="filesystemsanity-chk" src="https://github.com/user-attachments/assets/da18363d-e4c4-4fb2-92a7-6ed1365351bd" />

Observation: Disk is writable; basic FS operations work.

## 3️⃣ CPU / Memory checks

<img width="1351" height="705" alt="top" src="https://github.com/user-attachments/assets/d936a301-672a-4221-af15-dbe54ae4450e" />
<img width="1348" height="709" alt="htop" src="https://github.com/user-attachments/assets/b81647e9-160c-43f8-b85b-08f200dc3652" />

Observation: Memory usage normal; no pressure.

## 4️⃣ Disk / I/O check

<img width="1018" height="470" alt="disk commands" src="https://github.com/user-attachments/assets/8d9e1327-9238-4778-aff3-7011acbaa59a" />

Observation: Logs are reasonable in size.


## 5️⃣ Network check

<img width="1342" height="708" alt="network-command" src="https://github.com/user-attachments/assets/1a1de792-0a1d-407d-a8c6-acda0ebe1da1" />

<img width="1289" height="297" alt="curl-network-command" src="https://github.com/user-attachments/assets/0261b16a-c3b9-45a9-a094-ae1e046f1198" />

## 6️⃣ Logs (SSH) check

<img width="1351" height="513" alt="logs-ssh-command" src="https://github.com/user-attachments/assets/00f2488e-ee3c-48ae-abf8-7542ab1c2d21" />

Observation: Successful SSH logins; no recent errors.

## 🚨 Summary

System healthy

SSH service running and listening

No CPU, memory, disk, or log red flags
