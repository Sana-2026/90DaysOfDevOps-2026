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

# Where IP, TCP/UDP, HTTP/HTTPS, DNS sit in the stack ?

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
  
  Observations : 
  - System has more than one network interface 
  - 172.31.62.245 Primary private IP of the EC2 instance
  - 172.17.0.1 Docker bridge IP
   
### 2. ip addr show

  Displays all network interfaces on the system along with their MAC addresses, IPv4/IPv6 addresses, interface state (UP/DOWN), MTU, and link status.
  Used to quickly verify network configuration and connectivity.
  
  Observations : 
  
  - Interfaces: lo (localhost), ens5 (primary EC2), docker0 (Docker bridge)

  - Primary IP: ens5 → 172.31.62.245/20, UP, MTU 9001; docker0 → 172.17.0.1/16, DOWN

  - Loopback: 127.0.0.1 / ::1; MAC addresses shown for physical/virtual interfaces

  - The system has a healthy primary network interface, active localhost, and an inactive Docker bridge network
  
  <img width="1366" height="626" alt="ip-addr-show-command" src="https://github.com/user-attachments/assets/900e0fc4-1d7a-477e-848c-02c97bfd4d20" />

## Reachability

### 3. ping <target>

  Tests network connectivity between your system and a remote host by sending ICMP Echo Requests and measuring response time.
  Observations : 

   - Sends 5 test packets to Google

   - Checks if the internet / server is reachable

   - Helps detect packet loss

   - Stops automatically after 5 replies

  <img width="1348" height="702" alt="ping-command" src="https://github.com/user-attachments/assets/cd78d287-5a15-4f0b-8e71-9dcfb5209b75" />

## Path

### 4. traceroute <target> (or tracepath)

   Displays the network path (hops) taken by packets from your system to a destination host, helping identify where delays or failures occur.
   Obsevations :
   
      - Shows the number of hops (routers) between your system and Google

      - Displays delay (latency) at each hop

      - Helps identify where the network is slow or blocked

### 5. tracepath

   Traces the network route (hops) to a destination and shows path MTU and latency, without requiring root privileges.

   <img width="1352" height="507" alt="traceroute" src="https://github.com/user-attachments/assets/fe3482a1-dbea-4c1d-8dbd-5d2f2d8836ff" />

## Ports

### 6. ss -tulpn

   Displays all listening TCP and UDP sockets along with the port numbers and the process (PID/program) using them.
   It is the modern replacement for netstat.
   
  <img width="1374" height="621" alt="ss-tulpn" src="https://github.com/user-attachments/assets/d74cf8ea-81df-4a66-bc3c-e383a78fe30c" />

### 8. netstat -tulpn

    Displays all listening network ports along with the protocol, local address, and the process (PID/program) using each port.

     Observation:
      -Shows which TCP and UDP ports are listening on the system

     - Displays the service name and PID using each port

     - Helps identify running services and open ports

      ss -tulpn, netstat -tulpn used to monitor active services and open network ports.
      
   <img width="1359" height="619" alt="netstat-tulpn" src="https://github.com/user-attachments/assets/63ec9eeb-91dc-47ce-9d21-43f9f4e25be8" />

## Name resolution
  
### 9.dig <domain>
   Queries a DNS server to fetch DNS records for a domain name and helps troubleshoot DNS resolution issues.
   Observation:
      - Displays the resolved IP addresses (A/AAAA records) for google.com

      - Shows DNS response time (Query time)

      - Indicates which DNS server answered the query
   <img width="1341" height="572" alt="dig-google" src="https://github.com/user-attachments/assets/fb33ac17-50cb-444d-b5fb-4754825496eb" />
   
### 10. nslookup <domain>

Queries a DNS server to resolve a domain name into its IP address, mainly used for basic DNS troubleshooting.
Observations:

   - Shows the IP address(es) of google.com

   - Displays the DNS server used for the query

   - Confirms whether DNS resolution is working
      
 

## HTTP check

### 11. curl -I <http/https-url>

Sends an HTTP HEAD request with verbose output to show DNS resolution, connection details, and response headers.
Observations :

   - Displays the resolved IPv4/IPv6 addresses, shows which IP is connected, and prints the HTTP response headers (status code like 301).
    
<img width="1352" height="652" alt="curl-V-I" src="https://github.com/user-attachments/assets/96a95d81-c691-456c-9f5f-b8bee2fc21a9" />

## Connections snapshot

### 12. netstat -an | head
Displays all network connections and listening ports using numeric IP addresses and port numbers.
Observations:
   - Identified multiple ports currently in the LISTEN state
<img width="1349" height="293" alt="netstat-an" src="https://github.com/user-attachments/assets/c2309a4c-6647-447f-9558-f2bc089774ac" />

## Mini Task: Port Probe & Interpret

- Identify one listening port from ss -tulpn
- From the same machine, test it: nc -zv localhost <port>
   
<img width="1078" height="112" alt="nc -zv-localhost" src="https://github.com/user-attachments/assets/557d273f-32c4-441d-9fdf-ffffaea60a87" />
- If NOT reachable 
      Next check: service status (systemctl status ssh) and firewall rules


## Reflection 

#### Which command gives you the fastest signal when something is broken? ping

#### What layer (OSI/TCP-IP) would you inspect next if DNS fails? If HTTP 500 shows up?

If DNS fails

   OSI: Layer 7 – Application

   TCP/IP: Application layer

   👉 DNS  is an application-layer protocol, so we will  inspect:

   DNS server reachability

   Resolver config (/etc/resolv.conf)

   DNS response (dig, nslookup)

If HTTP 500 error appears

   OSI: Layer 7 – Application

   TCP/IP: Application layer

   👉 500 = server-side application error, so we will inspect:

   Web server logs (Nginx/Apache)

   App/service logs

   Backend dependencies (DB, APIs)
   
 👉 DNS failure or HTTP 500 → Application layer first.


#### Two follow-up checks you’d run in a real incident.

Service health: systemctl status <service> or check app logs

Network access: ss -tulpn 









