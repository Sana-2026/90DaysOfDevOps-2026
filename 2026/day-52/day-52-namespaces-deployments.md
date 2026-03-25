## Day 52 – Kubernetes Namespaces and Deployments

### Challenge Tasks

### Task 1: Explore Default Namespaces
Kubernetes comes with built-in namespaces. List them:
```
kubectl get namespaces
```
You should see at least:

+ ``default`` — where your resources go if you do not specify a namespace
+ ``kube-system`` — Kubernetes internal components (API server, scheduler, etc.)
+ ``kube-public`` — publicly readable resources
+ ``kube-node-lease`` — node heartbeat tracking

<img width="930" height="198" alt="task1-a" src="https://github.com/user-attachments/assets/761b10e6-1364-42b3-b720-d39c8bc19edf" />


Check what is running inside ``kube-system``:
```
kubectl get pods -n kube-system
```
These are the control plane components keeping your cluster alive. Do not touch them.

<img width="983" height="209" alt="task1-b" src="https://github.com/user-attachments/assets/4fd071b9-06cd-4f93-849a-c343f0f1bd6d" />


Verify: How many pods are running in ``kube-system``? 8 Pods are running


### Task 2: Create and Use Custom Namespaces
Create two namespaces — one for a development environment and one for staging:
```
kubectl create namespace dev
kubectl create namespace staging
```
Verify they exist:
```
kubectl get namespaces
```
You can also create a namespace from a manifest:
```
# namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: production
```
  
``kubectl apply -f namespace.yaml``

<img width="1347" height="518" alt="task2-a" src="https://github.com/user-attachments/assets/a7dbf2c8-2f70-49d7-b89e-a17e9621225b" />

Now run a pod in a specific namespace:
```
kubectl run nginx-dev --image=nginx:latest -n dev
kubectl run nginx-staging --image=nginx:latest -n staging
```

<img width="1340" height="575" alt="task2-c" src="https://github.com/user-attachments/assets/72e0d2e6-441a-4dfb-87fd-02713aeacb46" />

### 🚀 kubectl run Command Breakdown

#### 1️⃣ `kubectl run`
👉 Creates a **Pod** (quick way, mostly for testing/debugging)

---

#### 2️⃣ `nginx-dev`
👉 This is the **name of the Pod**


---

#### 3️⃣ `--image=nginx:latest`
👉 Specifies the **container image**

- `nginx` → image name  
- `latest` → tag (latest version)

📦 Kubernetes will pull the image from **Docker Hub**

---

#### 4️⃣ `-n dev`
👉 Namespace flag

- Creates the Pod inside the **dev namespace**
- Instead of the default namespace

---

### 📦 What actually happens behind the scenes

- Kubernetes creates a **Pod**
- Inside it → **1 container running nginx**
- Scheduled to a node
- Image pulled (if not already present)

---

## ✅ Equivalent YAML 

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-dev
  namespace: dev
spec:
  containers:
  - name: nginx
    image: nginx:latest
```

👉 kubectl run = generate + send Pod spec (not store YAML)

So your Pod will be called:

#### List pods across all namespaces:

``kubectl get pods -A``

Notice that kubectl get pods without -n only shows the default namespace. You must specify -n <namespace> or use -A to see everything.

<img width="1160" height="236" alt="task2-d" src="https://github.com/user-attachments/assets/2f12a333-d3be-4949-a970-ad411a014359" />

Verify: Does kubectl get pods show these pods? no it did not show
What about kubectl get pods -A? here all pods are shown

<img width="1366" height="430" alt="task2-e" src="https://github.com/user-attachments/assets/77ea3f8b-df11-4305-b4d7-211fca42c6c5" />

