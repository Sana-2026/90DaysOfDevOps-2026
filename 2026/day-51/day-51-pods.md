# Day 51 – Kubernetes Manifests and Your First Pods

### The Anatomy of a Kubernetes Manifest

Every Kubernetes resource is defined using a YAML manifest with four required top-level fields:

apiVersion: v1          # Which API version to use
kind: Pod               # What type of resource
metadata:               # Name, labels, namespace
  name: my-pod
  labels:
    app: my-app
spec:                   # The actual specification (what you want)
  containers:
  - name: my-container
    image: nginx:latest
    ports:
    - containerPort: 80
apiVersion — tells Kubernetes which API group to use. For Pods, it is v1.
kind — the resource type. Today it is Pod. Later you will use Deployment, Service, etc.
metadata — the identity of your resource. name is required. labels are key-value pairs used for organization and selection.
spec — the desired state. For a Pod, this means which containers to run, which images, which ports, etc.

### Challenge Tasks

### Task 1: Create Your First Pod (NginCreate a file called nginx-pod.yaml:

apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    app: nginx
spec:
  containers:
  - name: nginx
    image: nginx:latest
    ports:
    - containerPort: 80
Apply it:

kubectl apply -f nginx-pod.yaml
Verify:

kubectl get pods
kubectl get pods -o wide

<img width="1303" height="251" alt="task1 -a" src="https://github.com/user-attachments/assets/5736398e-aa5c-4687-a9ea-86b0ab8be0a1" />

Wait until the STATUS shows Running. Then explore:

### Detailed info about the pod
kubectl describe pod nginx-pod

<img width="1274" height="708" alt="pod-desc-task1" src="https://github.com/user-attachments/assets/2b46c8f4-b5ba-4599-b7a6-f73d7ac8e52e" />

### 🧠 What `kubectl describe pod` tells you

- **Pod status**  
  (Running / Pending / CrashLoopBackOff)

- **Container details**

- **Image used**

- **IP address**

- **Node where it’s running**

- **Events (MOST IMPORTANT 🔥)**  
  → Shows why something failed

  
### Read the logs
kubectl logs nginx-pod

<img width="1274" height="708" alt="pod-desc-task1" src="https://github.com/user-attachments/assets/5e37011e-8cc9-41f2-b64a-67c3b892a322" />








