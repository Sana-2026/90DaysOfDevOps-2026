# Inspection & Troubleshooting ssh Service- Step-by-Step for DevOps Beginners

## Step 1: Check if the service is running

systemctl status ssh

👉 Tells you:

Is it running or failed

Service name

Last few logs


## Step 2: Check service logs

journalctl -u ssh -n 20

👉 Shows last 20 logs


## Step 3:See how the service is started

systemctl cat ssh

👉 Shows:

Start command

Config file location

## Step 4: Check if service starts on boot

systemctl is-enabled ssh

👉 Output:

enabled → starts automatically

disabled → manual start

## Step 5 : Confirm process is running

pgrep -a ssh

👉 Confirms the actual process exists

🔍 Step 6: Restart the service

systemctl restart ssh


🧠 DevOps Service Inspection Flow

Status → Logs → Config → Process → Restart
