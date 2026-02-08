# Day 03 Linux File System & Navigation — Essential Commands

## Navigation Basics

pwd — Show current working directory

ls — List directory contents

ls -l — List files with permissions, owner, size

ls -a — Show hidden files

cd /path — Change directory

cd .. — Move one level up

cd ~ — Go to home directory

cd - — Switch to previous directory


## Directory Operations

mkdir dir — Create a directory

mkdir -p a/b/c — Create nested directories

rmdir dir — Delete empty directory

tree — Display directory structure (visual)


## File Operations 

touch file — Create empty file

cp file dest — Copy file

cp -r dir dest — Copy directory recursively

mv file dest — Move or rename file

rm file — Delete file

rm -r dir — Delete directory recursively


##  Viewing File Contents

cat file — View file content

less file — Scroll large files safely

head file — First 10 lines

tail file — Last 10 lines

tail -f logfile — Live log monitoring 🔥


## Linux Process Management — Essential Commands

ps — Show processes of current shell

ps -e — Show all running processes

ps aux — Detailed view (CPU, memory, user, PID) 


## Real-time Monitoring

top — Live process monitoring (CPU, RAM)

htop — Interactive & user-friendly top (recommended)


## Process Control 

kill PID — Gracefully stop a process (SIGTERM)

kill -9 PID — Force kill (SIGKILL) ⚠️


## Linux Networking Troubleshooting


ip a — Check IP address & interface status

ip link — Check network interfaces state

ping 8.8.8.8 — Test internet connectivity

ping google.com — Test DNS resolution

nslookup google.com — Query DNS resolution

dig google.com — Detailed DNS response (TTL, records)

traceroute google.com — Track packet path

tracepath google.com — Traceroute without root

ss -tulnp — Check listening ports & services ⭐

netstat -tulnp — Legacy port listing

lsof -i :80 — Who is using port 80?

curl http://localhost:8080 — Test HTTP response

curl -I google.com — Check headers only

## Why This Matters for DevOps
Real production issues are solved at the command line.

The faster you can inspect logs and network issues, the faster you can:

Restore service
Reduce downtime
Gain trust as an operator

