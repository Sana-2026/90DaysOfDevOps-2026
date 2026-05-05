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

<img width="1343" height="670" alt="task3-a" src="https://github.com/user-attachments/assets/aca8e186-e83b-45f9-9df8-82cdc3c5288b" />

<img width="1117" height="696" alt="task3-b" src="https://github.com/user-attachments/assets/59301b71-4175-4d31-90f6-f218c69087f1" />

<img width="1085" height="509" alt="task3-c" src="https://github.com/user-attachments/assets/0d8c181f-3d55-4961-b83d-260ed3ce594c" />

You can also use dry-run to generate YAML without creating anything:
```
kubectl run test-pod --image=nginx --dry-run=client -o yaml
```

<img width="1366" height="294" alt="task3-last" src="https://github.com/user-attachments/assets/5b7c16af-162e-46db-a7a1-c4bba4e8f07e" />

This is a powerful trick — use it to quickly scaffold a manifest, then customize it.

Verify: Save the dry-run output to a file and compare its structure with your nginx-pod.yaml. What fields are the same? What is different?


✅ What is SAME in both YAMLs

- apiVersion: v1
- kind: Pod
- metadata.name (pod name exists in both)
- metadata.labels (both use labels)
- spec.containers (both define containers)
- container image (nginx in both)
- container name (present in both)

❌ What is DIFFERENT

- Label key:
  run: test-pod (generated) vs app: nginx (manual)

- Ports:
  ❌ Not present in generated YAML
  ✅ Present in nginx-pod.yaml (containerPort: 80)

- Extra fields (only in generated YAML):
  - creationTimestamp: null
  - status: {}
  - dnsPolicy: ClusterFirst
  - restartPolicy: Always
  - resources: {}

- Indentation/cleanliness:
  Generated → verbose & auto-filled
  Manual → clean & minimal
  
🔥 Final Verification Insight

+ Generated YAML = system view (includes defaults)
+ Manual YAML = user intent (only what you define)
+ Kubernetes adds many fields automatically
+ You don’t need to write everything
+ Minimal YAML is easier to maintain



### Task 4: Validate Before Applying
Before applying a manifest, you can validate it:

### Check if the YAML is valid without actually creating the resource
kubectl apply -f nginx-pod.yaml --dry-run=client

### ✔️ If YAML is valid:
<img width="1224" height="77" alt="task4-a" src="https://github.com/user-attachments/assets/e776cab0-2a56-4499-a016-eecddba25eae" />

### ❌ If YAML has an error (e.g., missing image):

<img width="1084" height="83" alt="task4-d" src="https://github.com/user-attachments/assets/88a90309-39ba-4974-ba76-af88c936ce09" />

#### What this does
+ Checks syntax + basic schema validation
+ Runs locally on your machine (no API server call)
+ Does NOT create the Pod



### Validate against the cluster's API (server-side validation)
kubectl apply -f nginx-pod.yaml --dry-run=server

<img width="1075" height="59" alt="task4-b" src="https://github.com/user-attachments/assets/3f5c8a67-904f-4c45-8e9e-2387b2e1c87d" />

Now intentionally break your YAML (remove the image field or add an invalid field) and run dry-run again. See what error you get.

<img width="1084" height="83" alt="task4-d" src="https://github.com/user-attachments/assets/88a90309-39ba-4974-ba76-af88c936ce09" />

Verify: What error does Kubernetes give when the image field is missing?

```
error: error validating "nginx-pod.yaml": error validating data: 
[ValidationError(Pod.spec.containers[0]): missing required field "image"]
```

### Task 5: Pod Labels and Filtering
Labels are how Kubernetes organizes and selects resources. You added labels in your manifests — now use them:

### List all pods with their labels
```
kubectl get pods --show-labels
```

<img width="887" height="115" alt="task5-a" src="https://github.com/user-attachments/assets/4edbe2c7-a010-48bd-88fd-e6716dc45727" />

### Filter pods by label
```
kubectl get pods -l app=nginx
kubectl get pods -l environment=dev
```

<img width="1012" height="141" alt="task5-b" src="https://github.com/user-attachments/assets/3c719ca2-c7f4-457d-940d-3ca82b51daad" />


### Add a label to an existing pod
kubectl label pod nginx-pod environment=production

### Verify
kubectl get pods --show-labels

<img width="1126" height="271" alt="task5-c" src="https://github.com/user-attachments/assets/f7631b4a-8fa4-4e83-b111-3429580a30c8" />

### Remove a label
kubectl label pod nginx-pod environment-
Write a manifest for a third pod with at least 3 labels (app, environment, team). Apply it and practice filtering.

<img width="1045" height="153" alt="task5-last" src="https://github.com/user-attachments/assets/4ee5db9a-0c62-42ad-9bee-a09e1670e3e9" />

Task 6: Clean Up
Delete all the pods you created:

# Delete by name
kubectl delete pod nginx-pod
kubectl delete pod busybox-pod
kubectl delete pod redis-pod

# Or delete using the manifest file
kubectl delete -f nginx-pod.yaml

<img width="1226" height="134" alt="task6" src="https://github.com/user-attachments/assets/48760c46-a43a-41ab-a9ac-d6c3802f2522" />


# Verify everything is gone
kubectl get pods

<img width="1126" height="271" alt="task6-b" src="https://github.com/user-attachments/assets/4c869d07-cfbe-40dc-aa8e-da548820af45" />

Notice that when you delete a standalone Pod, it is gone forever. There is no controller to recreate it. This is why in production you use Deployments (coming on Day 52) instead of bare Pods.
