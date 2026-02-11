# Day 14 – Networking Fundamentals & Hands-on Checks

## OSI vs TCP/IP Model

| OSI Model (7 Layers) | TCP/IP Model (4 Layers) | Description |
|---------------------|--------------------------|-------------|
| Application (L7) | Application | User-facing network services |
| Presentation (L6) | Application | Data format, encryption, compression |
| Session (L5) | Application | Session establishment & management |
| Transport (L4) | Transport | End-to-end communication |
| Network (L3) | Internet | Logical addressing & routing |
| Data Link (L2) | Network Access | Framing & MAC addressing |
| Physical (L1) | Network Access | Bits, signals, cables |

# Where IP, TCP/UDP, HTTP/HTTPS, DNS sit in the stack

## 📘 Protocol Placement in OSI & TCP/IP Stack

| Protocol | OSI Layer | TCP/IP Layer | Purpose |
|----------|-----------|--------------|---------|
| IP | Layer 3 - Network | Internet | Logical addressing and routing |
| TCP | Layer 4 - Transport | Transport | Reliable, ordered data delivery |
| UDP | Layer 4 - Transport | Transport | Fast, connectionless delivery |
| HTTP | Layer 7 - Application | Application | Web data transfer |
| HTTPS | Layer 7 - Application | Application | Secure web communication |
| DNS | Layer 7 - Application | Application | Domain name to IP resolution |

## One real example: ping google.com = App layer over ICMP over IP

### Layer 7 (Application):

ping creates an ICMP Echo Request message.

### Layer 6 (Presentation):

Formats the ICMP data (no encryption involved).

### Layer 5 (Session):

Maintains the request–reply sequence for each ping.

### Layer 4 (Transport):

❌ Not used (ICMP does not use TCP or UDP).

### Layer 3 (Network):
Adds IP addressing (Src: 192.168.1.100 → Dst: 142.250.190.14).

### Layer 2 (Data Link):
Adds MAC address of the next hop (local router).

### Layer 1 (Physical):
Transmits bits as electrical signals / radio waves.

# Hands-on Checklist

## Identity

### 1. hostname -I
   
  Displays all assigned IP addresses of the system (excluding loopback), useful for quickly identifying the machine’s current network IPs.
   
### 2. ip addr show

  Displays all network interfaces on the system along with their MAC addresses, IPv4/IPv6 addresses, interface state (UP/DOWN), MTU, and link status.
  Used to quickly verify network configuration and connectivity.

  <img width="1366" height="626" alt="ip-addr-show-command" src="https://github.com/user-attachments/assets/900e0fc4-1d7a-477e-848c-02c97bfd4d20" />

## Reachability

### 3. ping <target>

  Tests network connectivity between your system and a remote host by sending ICMP Echo Requests and measuring response time.

  <img width="1348" height="702" alt="ping-command" src="https://github.com/user-attachments/assets/cd78d287-5a15-4f0b-8e71-9dcfb5209b75" />

## Path

### 4. traceroute <target> (or tracepath)

   Displays the network path (hops) taken by packets from your system to a destination host, helping identify where delays or failures occur.

### 5. tracepath

   Traces the network route (hops) to a destination and shows path MTU and latency, without requiring root privileges.

   <img width="1352" height="507" alt="traceroute" src="https://github.com/user-attachments/assets/fe3482a1-dbea-4c1d-8dbd-5d2f2d8836ff" />

## Ports

### 6. ss -tulpn

   Displays all listening TCP and UDP sockets along with the port numbers and the process (PID/program) using them.
   It is the modern replacement for netstat.
   
### 8. netstat -tulpn

    Displays all listening network ports along with the protocol, local address, and the process (PID/program) using each port.


