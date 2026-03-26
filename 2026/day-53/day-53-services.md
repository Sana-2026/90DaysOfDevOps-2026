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

<img width="1237" height="524" alt="task1b" src="https://github.com/user-attachments/assets/e2d612ab-d2f7-4eb0-9aea-3a91878ec7dc" />

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

<img width="1352" height="149" alt="task-b" src="https://github.com/user-attachments/assets/8777f7bc-ab17-4a9e-9895-af2068211505" />

web-app-66cb479f59-jl94f   → 10.244.0.167
web-app-66cb479f59-jn9hf   → 10.244.0.166
web-app-66cb479f59-xkndl   → 10.244.0.165
3 running Pods, each with a different IP

1. Deployment is healthy ✅
2. Multiple replicas are running ✅
3. Each Pod has its own IP (important concept)

👉 Kubernetes does:

Request → Service → (one of these 3 Pods)

+ Could go to 10.244.0.165

+ Or 10.244.0.166

+ Or 10.244.0.167
---
### Task 3: Discover Services with DNS

Kubernetes has a built-in DNS server. Every Service gets a DNS entry automatically:

``<service-name>.<namespace>.svc.cluster.local``
Test this:
```
kubectl run dns-test --image=busybox:latest --rm -it --restart=Never -- sh

# Inside the pod:
# Short name (works within the same namespace)
wget -qO- http://web-app-clusterip

# Full DNS name
wget -qO- http://web-app-clusterip.default.svc.cluster.local

<img width="1333" height="664" alt="task3-a" src="https://github.com/user-attachments/assets/ccd22e02-acf8-4d59-a105-f24fe2e104cb" />

# Look up the DNS entry
nslookup web-app-clusterip
exit
```
Both the short name and the full DNS name resolve to the same ClusterIP. In practice, you use the short name when communicating within the same namespace and the full name when reaching across namespaces.

<img width="909" height="282" alt="image" src="https://github.com/user-attachments/assets/25aed58b-fbaa-49f6-9717-14fc765ba18c" />

Verify: What IP does nslookup return? 10.96.60.95
Does it match the CLUSTER-IP from kubectl get services? yes it match

<img width="1333" height="664" alt="task3-a" src="https://github.com/user-attachments/assets/a1bbfd34-0c71-491f-a987-3ac71083062e" />

---

### Task 4: NodePort Service (External Access via Node)
A NodePort Service exposes your application on a port on every node in the cluster. This lets you access the Service from outside the cluster.

Create ``nodeport-service.yaml``:

```
apiVersion: v1
kind: Service
metadata:
  name: web-app-nodeport
spec:
  type: NodePort
  selector:
    app: web-app
  ports:
  - port: 80
    targetPort: 80
    nodePort: 30080
```
+ ``nodePort: 30080`` — the port opened on every node (must be in range 30000-32767)
+ Traffic flow: ``<NodeIP>:30080`` -> Service -> Pod:80

``
kubectl apply -f nodeport-service.yaml
kubectl get services
``
Access the service:
```
# If using Minikube
minikube service web-app-nodeport --url

# If using Kind, get the node IP first
kubectl get nodes -o wide
# Then curl <node-internal-ip>:30080

# If using Docker Desktop
curl http://localhost:30080
```
**Verify**: Can you see the Nginx welcome page from your browser or terminal using the NodePort?


---

