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

---
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

#### 2️⃣ `nginx-dev`
👉 This is the **name of the Pod**

#### 3️⃣ `--image=nginx:latest`
👉 Specifies the **container image**

- `nginx` → image name  
- `latest` → tag (latest version)

📦 Kubernetes will pull the image from **Docker Hub**

#### 4️⃣ `-n dev`
👉 Namespace flag

- Creates the Pod inside the **dev namespace**
- Instead of the default namespace

### 📦 What actually happens behind the scenes

- Kubernetes creates a **Pod**
- Inside it → **1 container running nginx**
- Scheduled to a node
- Image pulled (if not already present)

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

---

### Task 3: Create Your First Deployment
A Deployment tells Kubernetes: "I want X replicas of this Pod running at all times." If a Pod crashes, the Deployment controller recreates it automatically.

Create a file nginx-deployment.yaml:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  namespace: dev
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.24
        ports:
        - containerPort: 80
```
Key differences from a standalone Pod:

+ kind: Deployment instead of kind: Pod
+ apiVersion: apps/v1 instead of v1
+ replicas: 3 tells Kubernetes to maintain 3 identical pods
+ selector.matchLabels connects the Deployment to its Pods
+ template is the Pod template — the Deployment creates Pods using this blueprint

**Apply it**:
```
kubectl apply -f nginx-deployment.yaml
```
**Check the result**:
```
kubectl get deployments -n dev
kubectl get pods -n dev
```
You should see 3 pods with names like nginx-deployment-xxxxx-yyyyy.

this one is with error **InvalidImageName** 
<img width="976" height="230" alt="task3" src="https://github.com/user-attachments/assets/341122fb-141f-43d7-ab0d-0fc4aa7bf8bd" />

<img width="1217" height="271" alt="task3-correct" src="https://github.com/user-attachments/assets/fd3f88ba-cbe9-4929-a5f4-0fa722270d34" />

**Verify**: What do the READY, UP-TO-DATE, and AVAILABLE columns mean in the deployment output?

#### 📊 Deployment Columns 

#### 🔁 Think in this order:

👉 **1. UP-TO-DATE → 2. READY → 3. AVAILABLE**



#### 1️⃣ UP-TO-DATE (Updated?)
👉 Are Pods running the **latest version**?

- Shows how many Pods got the **new image/config**
- Used during **rolling updates**

🧠 Memory:
 First update the Pods

#### 2️⃣ READY (Healthy?)
👉 Are Pods **running and ready**?

- Format: `ready/desired`
- Example: `3/3`

🧠 Memory:
Then check if they are healthy

#### 3️⃣ AVAILABLE (Serving?)
👉 Are Pods **serving traffic**?

- Must be ready + stable
- Used by Service to send traffic

🧠 Memory:
 Finally, can users use them?

#### 🎯 One-Line Flow 

👉 **Updated → Healthy → Serving**

## 🔥 Real Example

```text
READY   UP-TO-DATE   AVAILABLE
2/3     3            2
```


### Task 4: Self-Healing — Delete a Pod and Watch It Come Back
This is the key difference between a Deployment and a standalone Pod.

#### List pods
``kubectl get pods -n dev``

#### Delete one of the deployment's pods (use an actual pod name from your output)

``kubectl delete pod <pod-name> -n dev``

#### Immediately check again

``kubectl get pods -n dev``

The Deployment controller detects that only 2 of 3 desired replicas exist and immediately creates a new one. The deleted pod is replaced within seconds.

Verify: Is the replacement pod's name the same as the one you deleted, or different?
---

### Task 5: Scale the Deployment

Change the number of replicas:

#### Scale up to 5
```
kubectl scale deployment nginx-deployment --replicas=5 -n dev
kubectl get pods -n dev
```

#### Scale down to 2
```
kubectl scale deployment nginx-deployment --replicas=2 -n dev
kubectl get pods -n dev
```
Watch how Kubernetes creates or terminates pods to match the desired count.

You can also scale by editing the manifest — change replicas: 4 in your YAML file and run kubectl apply -f nginx-deployment.yaml again.

**Verify**: When you scaled down from 5 to 2, what happened to the extra pods?

<img width="815" height="147" alt="down-scale-pods" src="https://github.com/user-attachments/assets/5278f9a5-ed7a-433f-81f1-39a10423c0fa" />


#### 🔻 Scale Down Behavior

When you scale a Kubernetes Deployment down (e.g., from 5 replicas to 2), the **extra pods are terminated (deleted)** by Kubernetes.

#### Step-by-step:
- Kubernetes compares **desired state (2 replicas)** vs **current state (5 replicas)**
- It identifies **3 extra pods**
- Those extra pods are **gracefully terminated**

---

#### ⚙️ What “graceful termination” means

- Kubernetes sends a **SIGTERM signal** to the containers  
- Gives them time (default **30 seconds**) to shut down cleanly  
- If they don’t stop in time → Kubernetes force kills them (**SIGKILL**)  

---

#### 🧠 Important Notes (DevOps perspective)

- Pods are **ephemeral** → they are not preserved unless backed by storage  
- If using a **Deployment**, pods are interchangeable → any 3 pods can be deleted  
- If using a **StatefulSet**, Kubernetes deletes pods in **reverse order**  
  - Example: `pod-4`, `pod-3`, `pod-2`  

---

#### 📌 One-line Memory Trick

> **Scale down = Kubernetes deletes extra pods to match desired state**

---
### Task 6: Rolling Update

Update the Nginx image version to trigger a rolling update:

``kubectl set image deployment/nginx-deployment nginx=nginx:1.25 -n dev``

Watch the rollout in real time:
```
kubectl rollout status deployment/nginx-deployment -n dev
Kubernetes replaces pods one by one — old pods are terminated only after new ones are healthy. This means zero downtime.
```
<img width="1334" height="450" alt="task6-a" src="https://github.com/user-attachments/assets/9f7823a6-88e2-4e86-a887-fd00b00c482d" />

Check the rollout history:

``kubectl rollout history deployment/nginx-deployment -n dev``

<img width="1249" height="131" alt="task6-b" src="https://github.com/user-attachments/assets/5075985d-da16-48d9-8399-5d2414d65331" />

Now roll back to the previous version:
```
kubectl rollout undo deployment/nginx-deployment -n dev
kubectl rollout status deployment/nginx-deployment -n dev
```
Verify the image is back to the previous version:

``kubectl describe deployment nginx-deployment -n dev | grep Image``

<img width="1300" height="168" alt="task6-c" src="https://github.com/user-attachments/assets/defa7a10-0da2-4046-b312-0fd082ba0570" />

**Verify**: What image version is running after the rollback?
old version nginx: 1.24
---

### Task 7: Clean Up
```
kubectl delete deployment nginx-deployment -n dev
kubectl delete pod nginx-dev -n dev
kubectl delete pod nginx-staging -n staging
kubectl delete namespace dev staging production
```
<img width="1203" height="251" alt="task7" src="https://github.com/user-attachments/assets/375f68d3-78bc-4ae5-b264-e7283278a3bb" />

Deleting a namespace removes everything inside it. Be very careful with this in production.
```
kubectl get namespaces
kubectl get pods -A
```
**Verify**: Are all your resources gone? yes gone

<img width="1283" height="410" alt="task7a" src="https://github.com/user-attachments/assets/fa5f0747-67dc-4f1a-a6bb-e65c111a9214" />

