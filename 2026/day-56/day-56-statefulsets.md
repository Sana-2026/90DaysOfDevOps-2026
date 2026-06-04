# Day 56 – Kubernetes StatefulSets

## Task
Deployments work great for stateless apps, but what about databases? You need stable pod names, ordered startup, and persistent storage per replica. Today you learn StatefulSets — the workload designed for stateful applications like MySQL, PostgreSQL, and Kafka.

---

## Challenge Tasks

### Task 1: Understand the Problem
1. Create a Deployment with 3 replicas using nginx
2. Check the pod names — they are random (`app-xyz-abc`)
3. Delete a pod and notice the replacement gets a different random name


<img width="1002" height="379" alt="task1-a" src="https://github.com/user-attachments/assets/41e64ca5-dddb-4b50-86e3-c6dd404fcc52" />

<img width="705" height="344" alt="task1-b" src="https://github.com/user-attachments/assets/bc155544-6fd6-42c5-970d-f0ca314134b0" />

This is fine for web servers but not for databases where you need stable identity.

| Feature | Deployment | StatefulSet |
|---|---|---|
| Pod names | Random | Stable, ordered (`app-0`, `app-1`) |
| Startup order | All at once | Ordered: pod-0, then pod-1, then pod-2 |
| Storage | Shared PVC | Each pod gets its own PVC |
| Network identity | No stable hostname | Stable DNS per pod |


Delete the Deployment before moving on.

**Verify:** Why would random pod names be a problem for a database cluster?

Random pod names are a problem for a database cluster because databases need stable identity, predictable hostnames, and persistent storage.

When a Deployment pod is deleted, Kubernetes creates a new pod with a different random name:

Before: mysql-7d8c9f4b5-abcde
After : mysql-7d8c9f4b5-xyz12

Other database nodes may be configured to communicate with the old hostname, causing replication or cluster communication issues.

A database cluster needs members that can always be reached at the same address. That's why StatefulSets create pods with fixed names such as:

mysql-0
mysql-1
mysql-2

Even if mysql-1 is deleted and recreated, it comes back as mysql-1 with the same identity and storage.

---

### Task 2: Create a Headless Service
1. Write a Service manifest with `clusterIP: None` — this is a Headless Service
2. Set the selector to match the labels you will use on your StatefulSet pods
3. Apply it and confirm CLUSTER-IP shows `None`

A Headless Service creates individual DNS entries for each pod instead of load-balancing to one IP. StatefulSets require this.

**Verify:** What does the CLUSTER-IP column show?
What does the CLUSTER-IP column show?

None

This confirms the Service is a Headless Service.

#### Normal Service

Pods
 ↓
Service IP (Load Balancer)
 ↓
Traffic distributed

Clients connect to one Service IP.

#### Headless Service

Pod-0 → DNS record
Pod-1 → DNS record
Pod-2 → DNS record

No Service IP is created.

Each pod gets its own stable DNS name, such as:

nginx-0.nginx-headless.default.svc.cluster.local
nginx-1.nginx-headless.default.svc.cluster.local
nginx-2.nginx-headless.default.svc.cluster.local

That's exactly why StatefulSets require a Headless Service: databases need to reach specific pods, not a random pod behind a load balancer.

---

### Task 3: Create a StatefulSet
1. Write a StatefulSet manifest with `serviceName` pointing to your Headless Service
2. Set replicas to 3, use the nginx image
3. Add a `volumeClaimTemplates` section requesting 100Mi of ReadWriteOnce storage
4. Apply and watch: `kubectl get pods -l <your-label> -w`

Observe ordered creation — `web-0` first, then `web-1` after `web-0` is Ready, then `web-2`.

Check the PVCs: `kubectl get pvc` — you should see `web-data-web-0`, `web-data-web-1`, `web-data-web-2` (names follow the pattern `<template-name>-<pod-name>`).

**Verify:** What are the exact pod names and PVC names?

nginx-stateful-0
nginx-stateful-1
nginx-stateful-2

PVC Names:
- web-data-nginx-stateful-0
- web-data-nginx-stateful-1
- web-data-nginx-stateful-2

<img width="1366" height="626" alt="task3-correct" src="https://github.com/user-attachments/assets/9d38a22d-281d-47cf-8bea-0425cc60406c" />



---

### Task 4: Stable Network Identity
Each StatefulSet pod gets a DNS name: `<pod-name>.<service-name>.<namespace>.svc.cluster.local`

1. Run a temporary busybox pod and use `nslookup` to resolve `web-0.<your-headless-service>.default.svc.cluster.local`
2. Do the same for `web-1` and `web-2`
3. Confirm the IPs match `kubectl get pods -o wide`

**Verify:** Does the nslookup IP match the pod IP?

---

### Task 5: Stable Storage — Data Survives Pod Deletion
1. Write unique data to each pod: `kubectl exec web-0 -- sh -c "echo 'Data from web-0' > /usr/share/nginx/html/index.html"`
2. Delete `web-0`: `kubectl delete pod web-0`
3. Wait for it to come back, then check the data — it should still be "Data from web-0"

The new pod reconnected to the same PVC.

**Verify:** Is the data identical after pod recreation?

---

### Task 6: Ordered Scaling
1. Scale up to 5: `kubectl scale statefulset web --replicas=5` — pods create in order (web-3, then web-4)
2. Scale down to 3 — pods terminate in reverse order (web-4, then web-3)
3. Check `kubectl get pvc` — all five PVCs still exist. Kubernetes keeps them on scale-down so data is preserved if you scale back up.

**Verify:** After scaling down, how many PVCs exist?

---

### Task 7: Clean Up
1. Delete the StatefulSet and the Headless Service
2. Check `kubectl get pvc` — PVCs are still there (safety feature)
3. Delete PVCs manually

**Verify:** Were PVCs auto-deleted with the StatefulSet?

---

## Hints
- `kubectl get sts` is the short name for StatefulSets
- `serviceName` must match an existing Headless Service
- Pod DNS: `<pod-name>.<service-name>.<namespace>.svc.cluster.local`
- PVC naming: `<template-name>-<statefulset-name>-<ordinal>`
- Pods create in order (0, 1, 2) and terminate in reverse (2, 1, 0)
- Scaling down does not delete PVCs — data is preserved
- Deleting a StatefulSet does not delete PVCs — clean up separately

---

## Documentation
Create `day-56-statefulsets.md` with:
- What StatefulSets are and when to use them vs Deployments
- The comparison table
- How Headless Services, stable DNS, and volumeClaimTemplates work
- Screenshots of pods, PVCs, and DNS resolution

---

## Submission
1. Add `day-56-statefulsets.md` to `2026/day-56/`
2. Commit and push to your fork

---

## Learn in Public
Share on LinkedIn: "Learned Kubernetes StatefulSets today. Stable pod names, per-pod DNS, and persistent storage that survives deletion — now I understand why databases need StatefulSets."

`#90DaysOfDevOps` `#DevOpsKaJosh` `#TrainWithShubham`

Happy Learning!
**TrainWithShubham**
