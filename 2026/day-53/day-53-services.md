## Day 53 – Kubernetes Services

### ❓ Why Services?

Every Pod gets its own IP address. But there are two problems:

- Pod IPs are **not stable** — when a Pod restarts or gets replaced, it gets a new IP  
- A Deployment runs **multiple Pods** — which IP do you connect to?  

### ✅ Solution: Service

A **Service** solves both problems by providing:

- A **stable IP and DNS name** that never changes  
- **Load balancing** across all Pods that match its selector  

### 🔁 Traffic Flow

[Client] --> [Service (stable IP)] --> [Pod 1]
--> [Pod 2]
--> [Pod 3]

---

### Challenge Tasks
### Task 1: Deploy the Application

First, create a Deployment that you will expose with Services. Create ``app-deployment.yaml``:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
  labels:
    app: web-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web-app
  template:
    metadata:
      labels:
        app: web-app
    spec:
      containers:
      - name: nginx
        image: nginx:1.25
        ports:
        - containerPort: 80
```
```
kubectl apply -f app-deployment.yaml
kubectl get pods -o wide
```
Note the individual Pod IPs. These will change if pods restart — that is the problem Services fix.

**Verify**: Are all 3 pods running? Note down their IP addresses.

