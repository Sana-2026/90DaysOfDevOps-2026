# Day 08 – Cloud Server Setup: Docker, Nginx & Web DeploymentDay 

## ✅ Commands Used

- ssh -i your-key.pem ubuntu@<your-instance-ip>

- sudo apt update

- sudo apt install nginx -y

- sudo systemctl start nginx

- sudo systemctl status nginx
  
- scp -i your-key.pem ubuntu@<your-instance-ip>:~/nginx-logs.txt 
  
## ⚠️ Challenges Faced

- Website not loading on public IP → Fixed by opening port 80 in the security group
- Hit permission denied while reading logs → Used sudo to access log files
- Encountered a permission denied error while extracting logs. Resolved it by updating file ownership from root →ubuntu before using SCP.

 

## 🎯 What I Learned:

- Deployed a live Nginx web server on AWS EC2 ☁️

- Accessed the instance securely using SSH key-based authentication 🔑

- Configured security groups to allow SSH (22) and HTTP (80) traffic

- Verified web server access via the EC2 public IP 🌐

- Collected Nginx logs on the instance and transferred them to my local system 💾

## 📌 Steps Followed :-

Step 1: Create a Cloud Instance and security group settings :
Instance Creation:

<img width="1152" height="576" alt="aws-instance-creation-1" src="https://github.com/user-attachments/assets/d59f61b3-ecf0-49ae-abb9-d83e5a8b5f83" />4
<img width="1152" height="571" alt="aws-instance-creation-2" src="https://github.com/user-attachments/assets/a10b68ee-e9ce-4000-8f09-e6128359d481" />
<img width="1147" height="569" alt="aws-instance-key-pair-creation" src="https://github.com/user-attachments/assets/da7344de-9125-41b8-8b41-6328c1e4710b" />

Security group settings:

<img width="1165" height="580" alt="aws-security-group-settings" src="https://github.com/user-attachments/assets/91ae0f41-d258-41bb-a1a3-06b21d445c3d" />
<img width="1364" height="496" alt="security-group-inboundrules" src="https://github.com/user-attachments/assets/91897879-48cc-4cec-9ef1-6edb164101ed" />
<img width="1354" height="511" alt="aws-addinbound-rule" src="https://github.com/user-attachments/assets/d7fd3925-0c8e-42b2-8102-fe57d1debfcd" />

Step 2: Connect via SSH
<img width="1348" height="220" alt="ssh-day8" src="https://github.com/user-attachments/assets/14d54dfd-301c-47ce-85d2-5b23186358da" />
<img width="1064" height="709" alt="ssh-welcome-day8" src="https://github.com/user-attachments/assets/27301fc7-07d8-41f4-9bfa-7abb021e4871" />

Step 3 :  Install Docker & Nginx 

1) Update System
   
<img width="1345" height="527" alt="sudo-apt-update-day7" src="https://github.com/user-attachments/assets/5f359e77-230e-48e8-9f83-7267b0ff125f" />

2)Install Nginx

<img width="1342" height="618" alt="sudo-apt-install-inginx" src="https://github.com/user-attachments/assets/f5b46ffc-28e8-4569-9eb1-058179e375b1" />

3) Verify Nginx is running:

<img width="1345" height="568" alt="systemctl-status-nginx-day7" src="https://github.com/user-attachments/assets/cc861abb-aba8-4ba9-9008-e91b1681d965" />

<img width="985" height="140" alt="systemctl-is-enabled-day7" src="https://github.com/user-attachments/assets/bb1a419e-85a9-4fd9-9eb5-65346cd22f67" />


Step 4 :Test Web Access

Open browser and visit: http://<your-instance-ip>

<img width="994" height="657" alt="welcome-nginx" src="https://github.com/user-attachments/assets/ad1e6c90-c17a-4a7e-915a-83a12c5b57c9" />

Step 5 : Extract Nginx Logs 

1️⃣ View logs on the server

sudo tail -n 20 /var/log/nginx/access.log

2️⃣ Extract logs into a file

sudo cp /var/log/nginx/access.log /home/ubuntu/nginx-logs.txt

<img width="1088" height="117" alt="copy-logs-local" src="https://github.com/user-attachments/assets/91b6f943-1869-4e75-95b2-c30bbab3d545" />

3️⃣ Download logs to your local system

 scp -i batch-10-superkey.pem ubuntu@ec2-44-246-242-10.us-west-2.compute.amazonaws.com:~/nginx-logs.txt .
 
<img width="918" height="91" alt="permissiondenied-while-down-logs" src="https://github.com/user-attachments/assets/ca499254-eba8-4c9e-8d5f-e182154c275b" />

To fix the permission issue for log files run below command

sudo chown ubuntu:ubuntu /home/ubuntu/nginx-logs.txt

<img width="932" height="224" alt="chg-own-log-files" src="https://github.com/user-attachments/assets/b8d57a61-b3b5-4d4b-a21b-a671449493a3" />

or to fix the permission issue we can directly create the file as ubuntu using following command

sudo -u ubuntu cp /var/log/nginx/access.log /home/ubuntu/nginx-logs.txt

snapshot of Logs on local machine
<img width="1341" height="393" alt="nginx-logs-local" src="https://github.com/user-attachments/assets/8edab40a-53be-46b9-b9e9-db8cd840ac95" />







