# Kubernetes Challenge Tasks 🚀

## Task 1: Recall the Kubernetes Story

Before touching a terminal, write down from memory:

- Why was Kubernetes created? What problem does it solve that Docker alone cannot?
- Who created Kubernetes and what was it inspired by?
- What does the name "Kubernetes" mean?

> ⚠️ Do not look anything up yet.  
Write what you remember from the session, then verify against the official docs.

---

## Task 2: Draw the Kubernetes Architecture

From memory, draw or describe the Kubernetes architecture.

### 🧠 Control Plane (Master Node)

- **API Server** — the front door to the cluster, every command goes through it  
- **etcd** — the database that stores all cluster state  
- **Scheduler** — decides which node a new pod should run on  
- **Controller Manager** — ensures desired state matches actual state  

### ⚙️ Worker Node

- **kubelet** — agent on each node that talks to API server and manages pods  
- **kube-proxy** — handles networking rules for pod communication  
- **Container Runtime** — runs containers (containerd, CRI-O)

### 🔍 Verify Your Understanding

- What happens when you run:  
  ```bash
  kubectl apply -f pod.yaml
