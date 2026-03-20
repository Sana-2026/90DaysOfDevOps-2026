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

### Task 2: Draw the Kubernetes Architecture

#### 🧠 Control Plane (Master Node)

- **API Server** — the front door to the cluster, every command goes through it  
- **etcd** — the database that stores all cluster state  
- **Scheduler** — decides which node a new pod should run on  
- **Controller Manager** — ensures desired state matches actual state  

#### ⚙️ Worker Node

- **kubelet** — agent on each node that talks to API server and manages pods  
- **kube-proxy** — handles networking rules for pod communication  
- **Container Runtime** — runs containers (containerd, CRI-O)

<img width="2000" height="2295" alt="k8-1" src="https://github.com/user-attachments/assets/a6f0cbf2-c6b9-460c-a697-1ec3e531d6d4" />

#### 🔍 Verify Your Understanding


### 1. What happens when you run kubectl apply -f pod.yaml? Trace the request through each component.

 #### `kubectl apply -f pod.yaml`

#### 1️⃣ kubectl (Client)

- Reads `pod.yaml`
- Converts YAML → JSON
- Sends a REST request to the API Server

**Uses kubeconfig (`~/.kube/config`) for:**
- Cluster endpoint
- Authentication credentials

---

#### 2️⃣ API Server (Gateway of Kubernetes)

- Receives the request
- Performs:
  - Authentication (who are you?)
  - Authorization (are you allowed?)
  - Validation (is the request valid?)

- If valid → accepts the object

---

#### 3️⃣ etcd (State Storage)

- Stores the Pod definition
- Represents the **desired state** of the system

---

#### 4️⃣ Controller Manager (Reconciliation Loop)

- Watches the API Server
- Detects mismatch between desired vs actual state

> "Pod is desired, but not running"

- Triggers actions to fix the state

---

#### 5️⃣ Scheduler (Node Selection)

- Selects the best node based on:
  - CPU / Memory
  - Node health
  - Scheduling constraints

- Assigns the Pod to a node

---

#### 6️⃣ Kubelet (Node Agent)

- Runs on the selected node
- Watches API Server
- Detects assigned Pod
- Ensures containers are running

---

#### 7️⃣ Container Runtime

- Pulls container image (e.g., nginx)
- Starts the container

---

#### 8️⃣ Networking Setup

- Configures networking rules
- Enables communication between Pods and services

---

#### 9️⃣ Status Update

- Kubelet reports status back to API Server
- State is updated in etcd

✔ Pod becomes **Running**

---

#### 🧠 Final Flow (One-Line)
kubectl → API Server → etcd → Controller → Scheduler → Node (Kubelet → Runtime) → Running Pod

### 2. What happens if the API server goes down?

The **API Server** is the central control point of Kubernetes. If it goes down, the cluster behavior changes significantly.

---

#### ❌ 1. Cluster Becomes Unmanageable

- `kubectl` commands stop working:
  - `kubectl get pods`
  - `kubectl apply`
  - `kubectl delete`

👉 Reason: All requests go through the API Server

---

#### ❌ 2. No New Changes Possible

- Cannot create new Pods
- Cannot scale Deployments
- Cannot update configurations

👉 Cluster becomes **read-only (frozen state)**

---

#### ⚠️ 3. Controllers Stop Working

- Controller Manager cannot watch cluster state
- Scheduler cannot assign new Pods

👉 No reconciliation happens

---

#### ⚠️ 4. Self-Healing Stops

- If a Pod crashes → ❌ not restarted
- If a Node fails → ❌ no rescheduling

👉 Desired state is not maintained

---

#### ✅ 5. Running Workloads Continue

- Existing Pods keep running
- Containers do not stop
- Applications may still serve traffic

👉 Because node-level agents (kubelet) continue working locally

---

#### ⚠️ 6. Cluster State Becomes Stale

- Nodes cannot report status
- API Server is unreachable

👉 Observability and monitoring break

---

#### 🧠 Final Summary

👉 **Cluster keeps running, but control is lost**

- Running apps → ✅
- New operations → ❌
- Auto-healing → ❌
- Scheduling → ❌

---

#### 🔥 Production Solution: High Availability (HA)

- Run multiple API Servers
- Use a load balancer in front
- If one fails → others handle requests

---

👉 *“If the API server goes down, existing workloads continue running, but the cluster becomes unmanageable—no scheduling, scaling, or self-healing can occur.”*

### 4. What happens if a worker node goes down?

# 🚨 What Happens If the Kubernetes API Server Goes Down?

The **API Server** is the central control point of Kubernetes. If it goes down, the cluster behavior changes significantly.

---

## ❌ 1. Cluster Becomes Unmanageable

- `kubectl` commands stop working:
  - `kubectl get pods`
  - `kubectl apply`
  - `kubectl delete`

👉 Reason: All requests go through the API Server

---

## ❌ 2. No New Changes Possible

- Cannot create new Pods
- Cannot scale Deployments
- Cannot update configurations

👉 Cluster becomes **read-only (frozen state)**

---

## ⚠️ 3. Controllers Stop Working

- Controller Manager cannot watch cluster state
- Scheduler cannot assign new Pods

👉 No reconciliation happens

---

## ⚠️ 4. Self-Healing Stops

- If a Pod crashes → ❌ not restarted
- If a Node fails → ❌ no rescheduling

👉 Desired state is not maintained

---

## ✅ 5. Running Workloads Continue

- Existing Pods keep running
- Containers do not stop
- Applications may still serve traffic

👉 Because node-level agents (kubelet) continue working locally

---

## ⚠️ 6. Cluster State Becomes Stale

- Nodes cannot report status
- API Server is unreachable

👉 Observability and monitoring break

---

## 🧠 Final Summary

👉 **Cluster keeps running, but control is lost**

- Running apps → ✅
- New operations → ❌
- Auto-healing → ❌
- Scheduling → ❌

---

## 🔥 Production Solution: High Availability (HA)

- Run multiple API Servers
- Use a load balancer in front
- If one fails → others handle requests

---


👉 *“If the API server goes down, existing workloads continue running, but the cluster becomes unmanageable—no scheduling, scaling, or self-healing can occur.”*

### What Happens If a Worker Node Goes Down in Kubernetes?

A worker node runs application workloads (Pods). If it goes down, Kubernetes reacts to maintain the desired state.

---

#### ❌ 1. Node Becomes NotReady

- Kubernetes detects the node failure
- Node status changes to: `NotReady`

👉 Detected via heartbeats from the kubelet

---

#### ⚠️ 2. Pods on That Node Become Unreachable

- All Pods running on that node stop responding
- They are marked as:
  - `Unknown` → initially
  - `Terminating` → eventually

---

#### 🔁 3. Controller Manager Takes Action

- Kubernetes detects mismatch:
  > Desired Pods ≠ Running Pods

- Controllers (like Deployment/ReplicaSet) react:
  - Create replacement Pods

---

#### 🧠 4. Scheduler Reschedules Pods

- New Pods are scheduled on **healthy nodes**
- Ensures application availability

---

#### ⚠️ 5. Delay in Recovery

- Default wait time (~5 minutes) before rescheduling
- Known as **node monitor grace period**

---

#### ❌ 6. Data Loss Risk (If Not Configured)

- If Pods use:
  - `emptyDir` → data is lost ❌
- If using Persistent Volumes → data is safe ✅

---

#### ⚠️ 7. DaemonSet Behavior

- Pods running via DaemonSet on that node are lost
- Recreated automatically on other nodes (if applicable)

---

#### 🧠 Final Summary

👉 **Node fails → Pods fail → Kubernetes recreates them elsewhere**

- Node status → ❌ NotReady  
- Pods on node → ❌ Lost  
- Controllers → 🔁 Recreate  
- Scheduler → 📍 Assign new node  
- App → ✅ Restored (if multi-replica)

---

👉 *“If a worker node goes down, Kubernetes marks it NotReady, stops Pods on it, and reschedules new Pods on healthy nodes to maintain the desired state.”*


### Task 3: Install kubectl

kubectl is the CLI tool you will use to talk to your Kubernetes cluster.

# Linux (amd64)
``
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
``

Verify:
``
kubectl version --client
``
<img width="833" height="107" alt="task3" src="https://github.com/user-attachments/assets/67d47f3e-6de0-4d61-93ea-88dd86059cc9" />

### Task 4: Set Up Your Local Cluster

### kind (Kubernetes in Docker)

#### Create a cluster
kind create cluster --name devops-cluster

<img width="1095" height="391" alt="task4-a" src="https://github.com/user-attachments/assets/296be738-0666-4604-99db-5e070f08e445" />

#### Verify
kubectl cluster-info
kubectl get nodes

<img width="1204" height="267" alt="task4b" src="https://github.com/user-attachments/assets/2a547f7e-3216-40c9-a243-784910db1f90" />


### Why did you choose Kind (Kubernetes IN Docker)?

I chose Kind because it is a lightweight and efficient way to run Kubernetes clusters locally for development and testing.

---

#### ✅ 1. Lightweight & Fast Setup

- Runs Kubernetes clusters inside Docker containers  
- No need for heavy VMs  
- Cluster can be created in seconds  

---

#### ✅ 2. Perfect for Local Development

- Ideal for testing manifests (Pods, Deployments, Services)  
- Easy to create and delete clusters quickly  
- Great for learning and experimentation  

---

#### ✅ 3. CI/CD Friendly

- Commonly used in CI pipelines (like GitHub Actions)  
- Helps test Kubernetes configs automatically  
- Easy to spin up ephemeral clusters  

---

#### ✅ 4. Multi-Node Cluster Support

- Can simulate real production-like environments  
- Supports multi-node clusters locally  

---

#### ✅ 5. Close to Real Kubernetes

- Uses upstream Kubernetes (not heavily modified)  
- Good for understanding real cluster behavior  

---

### Task 5: Explore Your Cluster

Now that your cluster is running, explore it:

#### See cluster info

kubectl cluster-info

#### List all nodes

kubectl get nodes

<img width="1204" height="267" alt="task4b" src="https://github.com/user-attachments/assets/f91bd7a0-6788-4596-b02d-216e25feceee" />

#### Get detailed info about your node

kubectl describe node devops-cluster-control-plane

<img width="1364" height="699" alt="task5-3" src="https://github.com/user-attachments/assets/080b5646-5858-4804-84e3-8dc6742179ea" />

<img width="1347" height="652" alt="task5-3b" src="https://github.com/user-attachments/assets/aa276cac-70fa-4120-b39c-a8b7f2a0c68d" />

👉 kubectl describe node devops-cluster-control-plane shows detailed information about the control-plane node, including its status, resources, labels, and running pods.


#### List all namespaces

kubectl get namespaces

<img width="959" height="200" alt="task5-4" src="https://github.com/user-attachments/assets/f22dc513-211a-4e01-8c22-1588f031c3de" />

#### See ALL pods running in the cluster (across all namespaces)

kubectl get pods -A

<img width="1196" height="297" alt="pod-running" src="https://github.com/user-attachments/assets/a38db639-92df-4ab4-974b-e7f434bbcd27" />







