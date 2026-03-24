# Day 51 – Kubernetes Manifests and Your First Pods

### The Anatomy of a Kubernetes Manifest

Every Kubernetes resource is defined using a YAML manifest with four required top-level fields:

```
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

```
### Challenge Tasks

### Task 1: Create Your First Pod (Nginx Create a file called nginx-pod.yaml:
```
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
```
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

### Get a shell inside the container
kubectl exec -it nginx-pod -- /bin/bash

### Inside the container, run:
curl localhost:80
exit

<img width="990" height="510" alt="pod-exec-task1" src="https://github.com/user-attachments/assets/565e950a-98e4-47a9-9de4-5223ef62f216" />

<img width="1366" height="720" alt="nginx-welc-from pod-task1" src="https://github.com/user-attachments/assets/da8358d0-92ec-4821-8b0b-ec54eb6aeab9" />

### Task 2: Create a Custom Pod (BusyBox)

Write a new manifest busybox-pod.yaml from scratch (do not copy-paste the nginx one):
```
apiVersion: v1
kind: Pod
metadata:
  name: busybox-pod
  labels:
    app: busybox
    environment: dev
spec:
  containers:
  - name: busybox
    image: busybox:latest
    command: ["sh", "-c", "echo Hello from BusyBox && sleep 3600"]
```
Apply and verify:

```
kubectl apply -f busybox-pod.yaml
kubectl get pods
kubectl logs busybox-pod
```

Notice the command field — BusyBox does not run a long-lived server like Nginx. Without a command that keeps it running, the container would exit immediately and the pod would go into CrashLoopBackOff.

Verify: Can you see "Hello from BusyBox" in the logs?

<img width="1186" height="672" alt="task2" src="https://github.com/user-attachments/assets/c1ad40fc-682a-4e94-8089-05033459bcd2" />


### Task 3: Imperative vs Declarative
You have been using the declarative approach (writing YAML, then kubectl apply). Kubernetes also supports imperative commands:

### Create a pod without a YAML file
```
kubectl run redis-pod --image=redis:latest
```
### Check it
```
kubectl get pods
Now extract the YAML that Kubernetes generated:

kubectl get pod redis-pod -o yaml
```
Compare this output with your hand-written manifests. Notice how much extra metadata Kubernetes adds automatically (status, timestamps, uid, resource version).

You can also use dry-run to generate YAML without creating anything:
```
kubectl run test-pod --image=nginx --dry-run=client -o yaml
```
This is a powerful trick — use it to quickly scaffold a manifest, then customize it.

Verify: Save the dry-run output to a file and compare its structure with your nginx-pod.yaml. What fields are the same? What is different?





