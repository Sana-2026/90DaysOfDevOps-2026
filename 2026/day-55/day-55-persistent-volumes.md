
# Day 55 – Persistent Volumes (PV) and Persistent Volume Claims (PVC)

## Challenge Tasks

### Task 1: See the Problem — Data Lost on Pod Deletion
1. Write a Pod manifest that uses an `emptyDir` volume and writes a timestamped message to `/data/message.txt`
2. Apply it, verify the data exists with `kubectl exec`
3. Delete the Pod, recreate it, check the file again — the old message is gone

**Verify:** Is the timestamp the same or different after recreation? timestamp is different

<img width="792" height="169" alt="task1-a" src="https://github.com/user-attachments/assets/0c599814-30bc-45e8-b319-43c432a0de4b" />

<img width="1362" height="255" alt="task1-b" src="https://github.com/user-attachments/assets/c522557c-d136-44df-a543-3f87fd01f01a" />

<img width="817" height="656" alt="task1-last" src="https://github.com/user-attachments/assets/71b58caa-e715-4f74-a0a5-1a458e300c5c" />


---

### Task 2: Create a PersistentVolume (Static Provisioning)
1. Write a PV manifest with `capacity: 1Gi`, `accessModes: ReadWriteOnce`, `persistentVolumeReclaimPolicy: Retain`, and `hostPath` pointing to `/tmp/k8s-pv-data`
2. Apply it and check `kubectl get pv` — status should be `Available`

Access modes to know:
- `ReadWriteOnce (RWO)` — read-write by a single node
- `ReadOnlyMany (ROX)` — read-only by many nodes
- `ReadWriteMany (RWX)` — read-write by many nodes

`hostPath` is fine for learning, not for production.

**Verify:** What is the STATUS of the PV? Available

<img width="689" height="238" alt="task2-b" src="https://github.com/user-attachments/assets/8269ccef-ebf1-4de7-80bd-a52b23433ebd" />


---

### Task 3: Create a PersistentVolumeClaim
1. Write a PVC manifest requesting `500Mi` of storage with `ReadWriteOnce` access
2. Apply it and check both `kubectl get pvc` and `kubectl get pv`
3. Both should show `Bound` — Kubernetes matched them by capacity and access mode

**Verify:** What does the VOLUME column in `kubectl get pvc` show?

<img width="1366" height="518" alt="task3" src="https://github.com/user-attachments/assets/91505c6d-8573-49ba-b45e-fbd9a71ef1ef" />
---

### Task 4: Use the PVC in a Pod — Data That Survives
1. Write a Pod manifest that mounts the PVC at `/data` using `persistentVolumeClaim.claimName`
2. Write data to `/data/message.txt`, then delete and recreate the Pod
3. Check the file — it should contain data from both Pods

**Verify:** Does the file contain data from both the first and second Pod?

<img width="1332" height="722" alt="task4" src="https://github.com/user-attachments/assets/d6bc3664-31f7-4bf0-896c-532d822931a1" />

<img width="704" height="323" alt="task4-last" src="https://github.com/user-attachments/assets/297f065f-4d97-4e36-a346-4e1ec8d49036" />

---

### Task 5: StorageClasses and Dynamic Provisioning
1. Run `kubectl get storageclass` and `kubectl describe storageclass`
2. Note the provisioner, reclaim policy, and volume binding mode
3. With dynamic provisioning, developers only create PVCs — the StorageClass handles PV creation automatically

In dynamic provisioning:

Developer creates only a PersistentVolumeClaim (PVC)
Kubernetes uses the StorageClass
Storage backend automatically creates the PersistentVolume (PV)

Flow:

PVC  →  StorageClass  →  Dynamic PV Creation

Static provisioning flow:

Admin creates PV manually
        ↓
Developer creates PVC
        ↓
PVC binds to existing PV

Dynamic provisioning flow:

Developer creates PVC
        ↓
StorageClass provisioner creates PV automatically
        ↓
PVC binds automatically

<img width="1366" height="406" alt="task5" src="https://github.com/user-attachments/assets/0f17cc94-79f1-4bac-be39-8f6cb1f073b5" />

**Verify:** What is the default StorageClass in your cluster? Standard 

---

### Task 6: Dynamic Provisioning
1. Write a PVC manifest that includes `storageClassName: standard` (or your cluster's default)
2. Apply it — a PV should appear automatically in `kubectl get pv`
3. Use this PVC in a Pod, write data, verify it works

**Verify:** How many PVs exist now? Which was manual, which was dynamic?
2 PVs 

Which PV was Manual?
hostpath-demo

Why?

We created it yourself using a PV manifest
Uses:
hostPath
storageClassName: manual
Static provisioning

Flow:

Admin creates PV manually
        ↓
PVC binds to existing PV


Which PV was Dynamic?
pvc-315c89ac-f8d6-4cb0-a516-39a08aa7e241

Why?

Kubernetes created it automatically
Triggered by PVC using:
storageClassName: standard
Provisioned by:
rancher.io/local-path

Flow:


PVC created
   ↓
StorageClass used
   ↓
Provisioner auto-created PV


<img width="1243" height="452" alt="task6" src="https://github.com/user-attachments/assets/0a53aa6a-9fb2-404d-8375-828e71616f09" />



---

### Task 7: Clean Up
1. Delete all pods first
2. Delete PVCs — check `kubectl get pv` to see what happened
3. The dynamic PV is gone (Delete reclaim policy). The manual PV shows `Released` (Retain policy).

What happened after deleting PVCs:

Dynamic PV disappeared automatically because:
reclaim policy = Delete
Manual PV stayed and became:
STATUS = Released

because:

reclaim policy = Retain

This is expected Kubernetes behavior.

5. Delete the remaining PV manually

<img width="1364" height="705" alt="task7-a" src="https://github.com/user-attachments/assets/4023cbd1-f702-4db9-8761-f544c45a327a" />

<img width="1366" height="343" alt="task7-c" src="https://github.com/user-attachments/assets/c786f545-3a3b-4494-b703-b6a5cfb45ea1" />


**Verify:** Which PV was auto-deleted and which was retained? Why?


Auto-deleted PV
pvc-315c89ac-f8d6-4cb0-a516-39a08aa7e241

This was the dynamic PV created automatically by the standard StorageClass.

It was auto-deleted because its reclaim policy was:

Delete

Flow:

PVC deleted
   ↓
Kubernetes automatically deleted PV
   ↓
Underlying storage cleaned up
Retained PV
hostpath-demo

This was the manual/static PV you created yourself.

It was retained because its reclaim policy was:

Retain

Flow:

PVC deleted
   ↓
PV moved to Released state
   ↓
Admin must manually clean/delete it
Why Kubernetes behaves this way
Delete reclaim policy

Used when storage can be safely removed automatically.

Common for:

temporary workloads
cloud dynamic volumes
short-lived applications
Retain reclaim policy

Used when data must be preserved even after PVC deletion.

Common for:

databases
critical production data
backup/recovery scenarios

---

