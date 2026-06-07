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

<img width="1352" height="712" alt="task4" src="https://github.com/user-attachments/assets/59b60b86-c71c-4fcf-9973-495cfcdd8d9e" />

Yes. The IP returned by nslookup matches the Pod IP shown by kubectl get pods -o wide.

This proves that the Headless Service created a stable DNS record for each StatefulSet pod:

So applications can connect to a specific pod by name instead of relying on changing IP addresses. That's one of the key reasons StatefulSets are used for databases and clustered applications. 🚀

---

### Task 5: Stable Storage — Data Survives Pod Deletion
1. Write unique data to each pod: `kubectl exec web-0 -- sh -c "echo 'Data from web-0' > /usr/share/nginx/html/index.html"`
2. Delete `web-0`: `kubectl delete pod web-0`
3. Wait for it to come back, then check the data — it should still be "Data from web-0"


<img width="1018" height="313" alt="task5" src="https://github.com/user-attachments/assets/2b01772e-0c9d-46bd-8f56-d506c72049ba" />

<img width="1026" height="498" alt="task5-b" src="https://github.com/user-attachments/assets/c063e1ed-7f80-4721-b6d0-87234a7715dd" />

The new pod reconnected to the same PVC.

**Verify:** Is the data identical after pod recreation?

Yes. After deleting nginx-stateful-0, Kubernetes recreated the pod with the same identity and reattached its original PersistentVolumeClaim. The file still contained "Data from nginx-stateful-0", proving that the data persisted even though the pod was deleted.


Deployment:
```
Delete Pod
    ↓
New Pod
    ↓
New Identity


StatefulSet:

Delete Pod
    ↓
Same Pod Name
    ↓
Same PVC
    ↓
Same Data

```
---

### Task 6: Ordered Scaling
1. Scale up to 5: `kubectl scale statefulset web --replicas=5` — pods create in order (web-3, then web-4)
2. Scale down to 3 — pods terminate in reverse order (web-4, then web-3)
3. Check `kubectl get pvc` — all five PVCs still exist. Kubernetes keeps them on scale-down so data is preserved if you scale back up.

<img width="1353" height="596" alt="task6-a" src="https://github.com/user-attachments/assets/61e6ad92-19c6-4380-897f-5de011318f56" />

<img width="1363" height="479" alt="task6-b" src="https://github.com/user-attachments/assets/535e1056-9c2d-46d7-824d-48fef68ac862" />

**Verify:** After scaling down, how many PVCs exist?

After scaling down from 5 replicas to 3 replicas, all 5 PVCs still existed. StatefulSets retain PVCs during scale-down to preserve data and allow pods to recover their storage if scaled up again.

---

### Task 7: Clean Up
1. Delete the StatefulSet and the Headless Service
2. Check `kubectl get pvc` — PVCs are still there (safety feature)
3. Delete PVCs manually

**Verify:** Were PVCs auto-deleted with the StatefulSet?


<img width="1366" height="702" alt="task7" src="https://github.com/user-attachments/assets/f961c893-d524-4b2f-8fe6-5efd112b6d9d" />

<img width="665" height="248" alt="image" src="https://github.com/user-attachments/assets/58a98665-a1a0-414f-bc5c-4bf291ab7af3" />


---


