## Mindset & Plan (Revisit):
Goals remain the same—adjusting the approach by prioritizing daily hands-on practice and real-world troubleshooting over theory. 💪

## Processes & services
### 1️⃣ ps aux

      - Observed all running processes with their PID, CPU, and memory usage
      - Helped identify which processes are consuming more resources
      
### 2️⃣ systemctl status nginx

      - Checked whether the Nginx service is active (running)
      - Verified service uptime and recent start time

  
### 3️⃣ journalctl -u nginx

     -  Viewed recent logs related only to the Nginx service
     -  Helpful for debugging startup issues and errors
     
## File skills:
  Practiced appending text using echo >>, verified permissions with ls -l, and updated access rights using chmod to ensure proper execution and ownership control. 

## Cheat sheet refresh

Here are 5 Day-03 commands I’d reach for first during an incident 👇

1. ls -l → Quickly check files, permissions, and ownership

2. cat  → Fast log and config inspection

3. tail -f → Watch logs in real time while troubleshooting

4. ps aux → Identify high CPU/memory–consuming processes

5. df -h → Check disk space issues (very common incident cause)

👉 These give instant visibility into files, logs, processes, and disk health—the basics of first-response troubleshooting. 🚨

## Mini Self-Check

### 1. Which 3 commands save you the most time right now, and why?
      - ls -l → instantly see files, permissions, ownership

      - ps aux → quickly spot problematic processes

      - tail -f → live log monitoring during issues
        
### 2. How do you check if a service is healthy? List the exact 2–3 commands you’d run first.
        - systemctl status <service>

        - journalctl -u <service> --since today

        - ps aux | grep <service>

### 3. How do you safely change ownership and permissions without breaking access?

        - Check first: ls -l

        - Change carefully: chown user:group file and chmod (avoid 777)

        - Verify again with ls -l
        
### 4. What will you focus on improving in the next 3 days?

    More real-world troubleshooting and log analysis practice 🚀


### Key takeaway:

Strong Linux fundamentals = faster troubleshooting, safer changes, and more confidence during real incidents. 💡🚀

   

