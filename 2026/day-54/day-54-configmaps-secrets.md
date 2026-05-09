# Day 54 – Kubernetes ConfigMaps and Secrets

## Challenge Tasks

### Task 1: Create a ConfigMap from Literals

1. Use `kubectl create configmap` with `--from-literal` to create a ConfigMap called `app-config` with keys `APP_ENV=production`, `APP_DEBUG=false`, and `APP_PORT=8080`

<img width="1352" height="669" alt="task1" src="https://github.com/user-attachments/assets/abb80fd5-2f73-43d7-be99-ac8204a7a099" />

 
2. Inspect it with `kubectl describe configmap app-config` and `kubectl get configmap app-config -o yaml`

 <img width="960" height="312" alt="task2-b" src="https://github.com/user-attachments/assets/2d6a9de4-12c0-4087-bfac-b67db1e850b3" /> 

 
3. Notice the data is stored as plain text — no encoding, no encryption
   
  ConfigMap = Non-sensitive data

  + env vars
  + configs
  + feature flags
    
**Verify:** Can you see all three key-value pairs? yes

---

### Task 2: Create a ConfigMap from a File
1. Write a custom Nginx config file that adds a `/health` endpoint returning "healthy"
3. Create a ConfigMap from this file using `kubectl create configmap nginx-config --from-file=default.conf=<your-file>`
4. The key name (`default.conf`) becomes the filename when mounted into a Pod

**Verify:** Does `kubectl get configmap nginx-config -o yaml` show the file contents? yes

<img width="1112" height="557" alt="task2" src="https://github.com/user-attachments/assets/c714d711-a53b-4ec4-9a4f-9372385513e6" />

<img width="960" height="312" alt="task2-b" src="https://github.com/user-attachments/assets/3e1b6bbc-b86c-4e8f-b6a2-8022d6f68e5a" />

<img width="1126" height="206" alt="task3-3" src="https://github.com/user-attachments/assets/e9bb8df2-eba5-4306-b331-56811e4d2421" />

---

### Task 3: Use ConfigMaps in a Pod
1. Write a Pod manifest that uses `envFrom` with `configMapRef` to inject all keys from `app-config` as environment variables. Use a busybox container that prints the values.
2. Write a second Pod manifest that mounts `nginx-config` as a volume at `/etc/nginx/conf.d`. Use the nginx image.
3. Test that the mounted config works: `kubectl exec <pod> -- curl -s http://localhost/health`

Use environment variables for simple key-value settings. Use volume mounts for full config files.

**Verify:** Does the `/health` endpoint respond?

<img width="729" height="172" alt="task3a" src="https://github.com/user-attachments/assets/11a1a1e5-ac73-4dfa-9156-48d790aa199e" />

<img width="888" height="453" alt="task3c" src="https://github.com/user-attachments/assets/e3080e1b-eeba-4e89-a0f3-bac93d5d5af2" />

<img width="1126" height="206" alt="task3-3" src="https://github.com/user-attachments/assets/20bdf472-a0fd-4bff-afce-8bbd068edfae" />

<img width="837" height="239" alt="task3-d" src="https://github.com/user-attachments/assets/589acb82-b367-423c-a74c-e989f991569f" />

---

### Task 4: Create a Secret
1. Use `kubectl create secret generic db-credentials` with `--from-literal` to store `DB_USER=admin` and `DB_PASSWORD=s3cureP@ssw0rd

  
<img width="1359" height="629" alt="task4-secrets" src="https://github.com/user-attachments/assets/82934381-993c-4660-9c6c-922f312290a9" />

 <img width="1348" height="723" alt="task4b" src="https://github.com/user-attachments/assets/3c74335a-d417-41cd-92bd-8d4b0c69c0d1" />

 <img width="1360" height="714" alt="task4c" src="https://github.com/user-attachments/assets/1ba66aeb-328f-465d-a93a-cbe2ea2a495c" />
 
2. Inspect with `kubectl get secret db-credentials -o yaml` — the values are base64-encoded

3. Decode a value: `echo '<base64-value>' | base64 --decode`


<img width="1349" height="621" alt="TASK4-LAST" src="https://github.com/user-attachments/assets/330dd3fc-4ab3-4ac0-a408-bcf286bd1621" />


**base64 is encoding, not encryption.** Anyone with cluster access can decode Secrets. The real advantages are RBAC separation, tmpfs storage on nodes, and optional encryption at rest.

**Verify:** Can you decode the password back to plaintext? yes 

### RBAC (Role-Based Access Control)

RBAC is Kubernetes’ authorization system.

It controls:

WHO can do WHAT on WHICH resource

#### Why RBAC Matters for Secrets

Secrets contain sensitive information:

Database passwords
API tokens
JWT secrets
TLS certificates

#### Without RBAC:

Any user with cluster access could read all Secrets.

That would be a huge security risk.

#### RBAC Core Components

Kubernetes RBAC mainly uses:

| Component | Purpose |
|---|---|
| Role | Defines permissions inside a namespace |
| ClusterRole | Defines cluster-wide permissions |
| RoleBinding | Attaches a Role to a user, group, or service account |
| ClusterRoleBinding | Attaches a ClusterRole cluster-wide |

#### Service Accounts and Secrets

Pods usually interact with Kubernetes using:

Service Accounts

Each Pod gets an identity.

RBAC controls what that Pod can access.

Example:

Frontend Pod → cannot access DB secrets
Backend Pod → can access DB secrets

This is extremely important in production clusters.

### 2) tmpfs in Kubernetes Secrets
What is tmpfs?

tmpfs is:

A temporary in-memory filesystem

Meaning:

Stored in RAM
Not permanently stored on disk

Linux creates it dynamically.

Why Kubernetes Uses tmpfs for Secrets

When Secrets are mounted into Pods:

Kubernetes often stores them in tmpfs on the node.

Reason:

Sensitive data should avoid persistent disk storage

This reduces leakage risk.

#### Secret Mount Flow
Secret stored in etcd
       ↓
Kubelet retrieves Secret
       ↓
Stored temporarily in tmpfs
       ↓
Mounted into container

#### Volatile Memory Concept

RAM loses data after:

Reboot
Shutdown
Crash

That makes tmpfs safer than normal disk storage.


---

### Task 5: Use Secrets in a Pod
1. Write a Pod manifest that injects `DB_USER` as an environment variable using `secretKeyRef`
2. In the same Pod, mount the entire `db-credentials` Secret as a volume at `/etc/db-credentials` with `readOnly: true`
3. Verify: each Secret key becomes a file, and the content is the decoded plaintext value

**Verify:** Are the mounted file values plaintext or base64?

---

### Task 6: Update a ConfigMap and Observe Propagation
1. Create a ConfigMap `live-config` with a key `message=hello`
2. Write a Pod that mounts this ConfigMap as a volume and reads the file in a loop every 5 seconds
3. Update the ConfigMap: `kubectl patch configmap live-config --type merge -p '{"data":{"message":"world"}}'`
4. Wait 30-60 seconds — the volume-mounted value updates automatically
5. Environment variables from earlier tasks do NOT update — they are set at pod startup only

**Verify:** Did the volume-mounted value change without a pod restart?

---

### Task 7: Clean Up
Delete all pods, ConfigMaps, and Secrets you created.

---
