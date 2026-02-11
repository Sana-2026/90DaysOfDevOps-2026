# Day 15 – Networking Concepts: DNS, IP, Subnets & Ports

## Task 1: DNS – How Names Become IPs

1️⃣ User enters a domain name (e.g., google.com)

2️⃣ System checks local DNS cache first

3️⃣ If not found, request goes to a DNS resolver

4️⃣ Resolver queries DNS hierarchy (Root → TLD → Authoritative)

5️⃣ Authoritative DNS server returns the resolved IP address (IPv4/IPv6) of the target server


### What are these record types? 

| Record Type | One-Line Description |
|------------|----------------------|
| A          | Maps a domain name to an IPv4 address. |
| AAAA       | Maps a domain name to an IPv6 address. |
| CNAME      | Creates an alias pointing one domain to another domain. |
| MX         | Specifies the mail server responsible for receiving emails for a domain. |
| NS         | Defines the authoritative name servers for a domain. |


###  dig google.com — identifying the A record and TTL from the output

<img width="1026" height="614" alt="task-1" src="https://github.com/user-attachments/assets/adece665-e90f-45f5-88cf-ac6fd47383d1" />

- A record IP: 142.250.73.142

- TTL: 266 seconds

- 266 → TTL (how long DNS cache keeps this record)

- A → IPv4 record

- 142.250.73.142 → returned IP address

## Task 2: IP Addressing

### IPv4 Address Overview

| Aspect | Description | Example |
|--------|-------------|---------|
| Definition | A unique 32-bit numerical identifier assigned to a device on a network | 192.168.1.10 |
| IP Version | Internet Protocol version 4 | IPv4 |
| Address Length | 32 bits total | 4 × 8 bits |
| Format | Dotted decimal notation | A.B.C.D |
| Number of Octets | 4 octets | 192 · 168 · 1 · 10 |
| Range per Octet | 0 to 255 | 0–255 |
| Total Possible Addresses | ~4.3 billion | 2³² |

### IPv4 Address Structure

| Component | Description | Example |
|-----------|-------------|---------|
| Octet 1 | First 8 bits of the address | 192 |
| Octet 2 | Second 8 bits of the address | 168 |
| Octet 3 | Third 8 bits of the address | 1 |
| Octet 4 | Fourth 8 bits of the address | 10 |
| Binary Representation | Each octet converted to binary | 11000000.10101000.00000001.00001010 |


### Difference between public and private IPs?

| Aspect | Public IP Address | Private IP Address |
|------|------------------|-------------------|
| Definition | IP address accessible over the internet | IP address used within a private network |
| Scope | Globally unique | Unique only within a local network |
| Internet Access | Directly reachable from the internet | Not directly reachable from the internet |
| Assigned By | ISP (Internet Service Provider) | Network administrator / Router |
| Usage | Identify devices on the public internet | Identify devices inside LAN |
| NAT Required | Not required | Required to access the internet |
| Security | More exposed to attacks | More secure (hidden behind NAT) |
| Cost | May be chargeable by ISP | Free to use |
| Examples | 8.8.8.8, 1.1.1.1 | 192.168.1.10, 10.0.0.5 |
| Common Use Cases | Web servers, public services | Home, office, internal systems |


### What are the private IP ranges?


| Class | IP Range | CIDR Notation | Number of Addresses | Common Use |
|------|----------|---------------|---------------------|------------|
| Class A | 10.0.0.0 – 10.255.255.255 | 10.0.0.0/8 | ~16 million | Large private networks |
| Class B | 172.16.0.0 – 172.31.255.255 | 172.16.0.0/12 | ~1 million | Medium-sized networks |
| Class C | 192.168.0.0 – 192.168.255.255 | 192.168.0.0/16 | ~65,536 | Home / small office networks |


### ip addr show — identifying which of the IPs are private

<img width="1348" height="474" alt="ip-addr-show" src="https://github.com/user-attachments/assets/21d65c31-b2c8-4c77-abad-6905295907d2" />

## Task 3: CIDR & Subnetting

### What does /24 mean in 192.168.1.0/24?

The first 24 bits of the IP address are used for the network portion,
and the remaining 8 bits are for host addresses.

Lets Break it down : 

- Pv4 address = 32 bits

- /24 → 24 bits = Network

- Remaining 8 bits = Hosts

### How many usable hosts in a /24? A /16? A /28?

| CIDR | Total IPs | Usable Hosts | Host Bits | Subnet Mask |
|------|-----------|--------------|-----------|-------------|
| /16 | 65,536 | 65,534 | 16 | 255.255.0.0 |
| /24 | 256 | 254 | 8 | 255.255.255.0 |
| /28 | 16 | 14 | 4 | 255.255.255.240 |

Formula to calculate  Usable hosts = 2^(host bits) − 2
Examples :

/16 → 32 − 16 = 16 host bits → 2¹⁶ − 2 = 65,534

/24 → 32 − 24 = 8 host bits → 2⁸ − 2 = 254


### why do we subnet?

Subnetting is the process of dividing a large network into smaller, more manageable networks, because a single large network becomes inefficient, less secure, and difficult to manage

### Reference Table

| CIDR | Subnet Mask | Total IPs | Usable Hosts |
|------|-------------|-----------|--------------|
| /24 | 255.255.255.0 | 256 | 254 |
| /16 | 255.255.0.0 | 65,536 | 65,534 |
| /28 | 255.255.255.240 | 16 | 14 |


## Task 4: Ports – The Doors to Services

### What is a port? Why do we need them?

A port is a logical number (0–65535) used to identify a specific application or service on a device.
👉 IP = machine, Port = application
Example: 192.168.1.10:80

Why do we need ports?

Allow multiple services to run on the same IP

Ensure data reaches the correct application

Enable client–server communication

Help with security & access control (firewalls, security groups)

### Common ports:

| Port | Service |
|------|---------|
| 22 | SSH |
| 80 | HTTP |
| 443 | HTTPS |
| 53 | DNS |
| 3306 | MySQL |
| 6379 | Redis |
| 27017 | MongoDB |


### Matching listening ports

Command: ss -tulpn
Example: 22 → SSH, 80 → HTTP

<img width="1353" height="675" alt="ss-tulpn" src="https://github.com/user-attachments/assets/46169856-0cbe-4dcc-8156-c3079816a31e" />


## Task 5: Putting It Together

curl http://myapp.com:8080 — networking concepts involved

- DNS resolves myapp.com to an IP address

- HTTP (application layer) runs over TCP

- TCP connects to port 8080 on the server using IP routing

App can’t reach database at 10.0.1.50:3306 — what to check first

- Network connectivity and routing to the private IP ping 10.0.1.50

- Firewall / security group rules allowing TCP 3306

- Database service running and listening on port 3306

## Key Learnings

### - IPv4 & Subnetting: 

IP addresses identify devices, subnetting divides large networks into smaller, manageable networks, improving efficiency, security, and traffic control.

### - Ports & Services:

Ports let multiple applications share the same IP, ensuring traffic reaches the correct service (e.g., HTTP 80, SSH 22, MySQL 3306).

### - Practical Networking Checks: 

Connectivity issues involve DNS resolution, IP reachability, port accessibility, and service status — all verified using commands like ping, telnet/nc, and ss/netstat.


