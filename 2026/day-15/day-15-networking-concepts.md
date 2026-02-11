# Day 15 – Networking Concepts: DNS, IP, Subnets & Ports

## Task 1: DNS – How Names Become IPs

1️⃣ User enters a domain name (e.g., google.com)

2️⃣ System checks local DNS cache first

3️⃣ If not found, request goes to a DNS resolver

4️⃣ Resolver queries DNS hierarchy (Root → TLD → Authoritative)

5️⃣ Authoritative DNS server returns the resolved IP address (IPv4/IPv6) of the target server


## What are these record types? 

| Record Type | One-Line Description |
|------------|----------------------|
| A          | Maps a domain name to an IPv4 address. |
| AAAA       | Maps a domain name to an IPv6 address. |
| CNAME      | Creates an alias pointing one domain to another domain. |
| MX         | Specifies the mail server responsible for receiving emails for a domain. |
| NS         | Defines the authoritative name servers for a domain. |



A record IP: 142.250.73.142

TTL: 266 seconds

266 → TTL (how long DNS cache keeps this record)

A → IPv4 record

142.250.73.142 → returned IP address






