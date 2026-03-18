## Kubernetes Challenge Tasks 🚀

### Task 1: Recall the Kubernetes Story

#### 1. Why was Kubernetes created? What problem does it solve that Docker alone cannot?


####  Docker made it easy to:

- Package applications into containers  
- Run them consistently anywhere  

But when companies started running **hundreds or thousands of containers**, things got messy.

👉 That’s where Kubernetes came in.

---

### ⚙️ Kubernetes Purpose

- **Kubernetes** was designed to efficiently manage large-scale containerized applications.

---

#### ❌ Limitations of Docker

#### ✅ Docker can:
- Run containers ✔️  
- Build images ✔️  

#### ❌ But Docker cannot manage containers at scale:

- No automatic scaling (increase/decrease containers based on load)  
- No self-healing (restart failed containers automatically across machines)  
- No built-in load balancing  
- No easy way to manage containers across multiple servers  
- Manual deployment & updates become painful  

---

### 🧠 Key Takeaway

👉 **Docker = Runs containers**  
👉 **Kubernetes = Manages containers at scale**

#### 2. Who created Kubernetes and what was it inspired by?

 Kubernetes was created by Google in 2014, based on its years of experience running containers at scale.

👉 It was inspired by Borg, Google’s internal container management system, which could schedule workloads, auto-scale applications, and handle failures across thousands of machines.

👉 To make this technology available to everyone, Google open-sourced Kubernetes and later donated it to the Cloud Native Computing Foundation (CNCF), which now maintains and evolves it.

 Kubernetes was created by Google, inspired by its internal system Borg, and is now maintained by CNCF as an open-source project.

- What does the name "Kubernetes" mean?
  
The name Kubernetes comes from the Greek word “kybernētēs”, which means “helmsman” or “ship pilot.” 🚢

👉 It reflects Kubernetes’ role in steering and managing containers, just like a pilot controls a ship.

💡 Fun fact:

The abbreviation K8s comes from replacing the 8 letters between K and s in Kubernetes.
 


---

## Task 2: Draw the Kubernetes Architecture

### 🧠 Control Plane (Master Node)

- **API Server** — the front door to the cluster, every command goes through it  
- **etcd** — the database that stores all cluster state  
- **Scheduler** — decides which node a new pod should run on  
- **Controller Manager** — ensures desired state matches actual state  

### ⚙️ Worker Node

- **kubelet** — agent on each node that talks to API server and manages pods  
- **kube-proxy** — handles networking rules for pod communication  
- **Container Runtime** — runs containers (containerd, CRI-O)

<img width="2000" height="2295" alt="k8-1" src="https://github.com/user-attachments/assets/a6f0cbf2-c6b9-460c-a697-1ec3e531d6d4" />

### 🔍 Verify Your Understanding

- What happens when you run:  
  ```bash
  kubectl apply -f pod.yaml
