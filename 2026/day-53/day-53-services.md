# Day 53 – Kubernetes Services

### ❓ Why Services?

Every Pod gets its own IP address. But there are two problems:

- Pod IPs are **not stable** — when a Pod restarts or gets replaced, it gets a new IP  
- A Deployment runs **multiple Pods** — which IP do you connect to?  

### ✅ Solution: Service

A **Service** solves both problems by providing:

- A **stable IP and DNS name** that never changes  
- **Load balancing** across all Pods that match its selector  

### 🔁 Traffic Flow
```
[Client] --> [Service (stable IP)] --> [Pod 1]
                                   --> [Pod 2]
                                   --> [Pod 3]
```
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

**Verify**: Are all 3 pods running? Note down their IP addresses. yes they hv changed

<img width="1344" height="347" alt="task1" src="https://github.com/user-attachments/assets/20425e97-d57b-45d5-840d-607d74defb9f" />

---

### Task 2: ClusterIP Service (Internal Access)

ClusterIP is the default Service type. It gives your Pods a stable internal IP that is only reachable from within the cluster.

Create ``clusterip-service.yaml``:
```
apiVersion: v1
kind: Service
metadata:
  name: web-app-clusterip
spec:
  type: ClusterIP
  selector:
    app: web-app
  ports:
  - port: 80
    targetPort: 80
```

Key fields:

+ ``selector.app: web-app`` — this Service routes traffic to all Pods with the label ``app: web-app``
+ ``port: 80 ``— the port the Service listens on
+ ``targetPort: 80`` — the port on the Pod to forward traffic to
``
kubectl apply -f clusterip-service.yaml
kubectl get services

``
You should see ``web-app-clusterip`` with a CLUSTER-IP address. This IP is stable — it will not change even if Pods restart.

Now test it from inside the cluster:
```
# Run a temporary pod to test connectivity
kubectl run test-client --image=busybox:latest --rm -it --restart=Never -- sh

# Inside the test pod, run:
wget -qO- http://web-app-clusterip
exit
```

You should see the Nginx welcome page. The Service load-balanced your request to one of the 3 Pods.

**Verify**: Does the Service respond? Try running the wget command multiple times — the Service distributes traffic across all healthy Pods

---

