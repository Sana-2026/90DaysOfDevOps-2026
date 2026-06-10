# Day 57 – Resource Requests, Limits, and Probes

## Challenge Tasks

### Task 1: Resource Requests and Limits
1. Write a Pod manifest with `resources.requests` (cpu: 100m, memory: 128Mi) and `resources.limits` (cpu: 250m, memory: 256Mi)
2. Apply and inspect with `kubectl describe pod` — look for the Requests, Limits, and QoS Class sections
3. Since requests and limits differ, the QoS class is `Burstable`. If equal, it would be `Guaranteed`. If missing, `BestEffort`.

CPU is in millicores: `100m` = 0.1 CPU. Memory is in mebibytes: `128Mi`.

<img width="1366" height="705" alt="task1" src="https://github.com/user-attachments/assets/cc993289-877c-4435-a27b-9745ffdb6c1b" />

<img width="1370" height="701" alt="task1-b" src="https://github.com/user-attachments/assets/51365fda-8b58-4d71-974e-cf8c01a2b851" />



**Requests** = guaranteed minimum (scheduler uses this for placement). **Limits** = maximum allowed (kubelet enforces at runtime).

**Verify:** What QoS class does your Pod have? The Pod's QoS class is Burstable because requests and limits are defined but are not equal.

Kubernetes automatically assigns a QoS class.

#### 1. Guaranteed

Requests = Limits for every resource.

requests:
  cpu: 200m
  memory: 128Mi

limits:
  cpu: 200m
  memory: 128Mi

  Result:

QoS Class: Guaranteed

Highest priority during node pressure.

#### 2. Burstable

Requests and limits exist but are different.

requests:
  cpu: 100m
  memory: 128Mi

limits:
  cpu: 250m
  memory: 256Mi

Result:

QoS Class: Burstable

#### 3. BestEffort

No requests and no limits.

resources: {}

Result:

QoS Class: BestEffort

Lowest priority and first to be evicted when a node runs out of resources.

---

### Task 2: OOMKilled — Exceeding Memory Limits

1. Write a Pod manifest using the `polinux/stress` image with a memory limit of `100Mi`
2. Set the stress command to allocate 200M of memory: `command: ["stress"] args: ["--vm", "1", "--vm-bytes", "200M", "--vm-hang", "1"]`
3. Apply and watch — the container gets killed immediately

CPU is throttled when over limit. Memory is killed — no mercy.

Check `kubectl describe pod` for `Reason: OOMKilled` and `Exit Code: 137` (128 + SIGKILL).

<img width="1366" height="664" alt="task2" src="https://github.com/user-attachments/assets/fb3e6992-e605-4863-931f-39827274bc1a" />

<img width="1366" height="734" alt="task2-a" src="https://github.com/user-attachments/assets/3c4b9f4c-dfc9-401b-8ab5-e5c00445f4be" />


**Verify:** What exit code does an OOMKilled container have? 137

#### Why Does It Happen?

The container tries to allocate:

200M

But Kubernetes allows only:

100Mi

Memory usage exceeds the limit.

The Linux OOM Killer terminates the process.

#### Understanding Exit Code 137

Linux exit codes:

137 = 128 + 9

Where:

128 = Process terminated by signal
9 = SIGKILL

So:

137 = SIGKILL

An OOMKilled container almost always shows:

Exit Code: 137


#### Troubleshooting Rule

When a Pod is:

Status	                  First Command

Pending            	      kubectl describe pod
CrashLoopBackOff	        kubectl logs
OOMKilled	kubectl         describe pod
Running but failing	      kubectl logs

---

### Task 3: Pending Pod — Requesting Too Much
1. Write a Pod manifest requesting `cpu: 100` and `memory: 128Gi`
2. Apply and check — STATUS stays `Pending` forever
3. Run `kubectl describe pod` and read the Events — the scheduler says exactly why: insufficient resources

<img width="1381" height="753" alt="task3" src="https://github.com/user-attachments/assets/d7478ca6-5aa6-4dba-a2ce-6b0fbf124ce6" />

<img width="1357" height="643" alt="tsk3-b" src="https://github.com/user-attachments/assets/994a5815-15b2-4f36-8398-e87b5f69d3bc" />


**Verify:** What event message does the scheduler produce?

Warning  FailedScheduling  default-scheduler  0/1 nodes are available: 1 Insufficient cpu, 1 Insufficient memory.

Depending on your cluster size, it might be:

0/2 nodes are available: 2 Insufficient cpu, 2 Insufficient memory.

or

0/3 nodes are available: 3 Insufficient cpu, 3 Insufficient memory.

**Why?**

The scheduler checks every node and asks:

"Can any node provide 100 CPU cores and 128Gi RAM?"

For a Kind cluster (usually 2–4 CPUs and a few GB of RAM), the answer is No, so the Pod remains Pending.

---

### Task 4: Liveness Probe
A liveness probe detects stuck containers. If it fails, Kubernetes restarts the container.

1. Write a Pod manifest with a busybox container that creates `/tmp/healthy` on startup, then deletes it after 30 seconds
2. Add a liveness probe using `exec` that runs `cat /tmp/healthy`, with `periodSeconds: 5` and `failureThreshold: 3`
3. After the file is deleted, 3 consecutive failures trigger a restart. Watch with `kubectl get pod -w`

**Verify:** How many times has the container restarted?

---

### Task 5: Readiness Probe
A readiness probe controls traffic. Failure removes the Pod from Service endpoints but does NOT restart it.

1. Write a Pod manifest with nginx and a `readinessProbe` using `httpGet` on path `/` port `80`
2. Expose it as a Service: `kubectl expose pod <name> --port=80 --name=readiness-svc`
3. Check `kubectl get endpoints readiness-svc` — the Pod IP is listed
4. Break the probe: `kubectl exec <pod> -- rm /usr/share/nginx/html/index.html`
5. Wait 15 seconds — Pod shows `0/1` READY, endpoints are empty, but the container is NOT restarted

**Verify:** When readiness failed, was the container restarted?

---

### Task 6: Startup Probe
A startup probe gives slow-starting containers extra time. While it runs, liveness and readiness probes are disabled.

1. Write a Pod manifest where the container takes 20 seconds to start (e.g., `sleep 20 && touch /tmp/started`)
2. Add a `startupProbe` checking for `/tmp/started` with `periodSeconds: 5` and `failureThreshold: 12` (60 second budget)
3. Add a `livenessProbe` that checks the same file — it only kicks in after startup succeeds

**Verify:** What would happen if `failureThreshold` were 2 instead of 12?

---

### Task 7: Clean Up
Delete all pods and services you created.

---

## Hints
- CPU is compressible (throttled); memory is incompressible (OOMKilled)
- CPU: `1` = 1 core = `1000m`. Memory: `Mi` (mebibytes), `Gi` (gibibytes)
- QoS: Guaranteed (requests == limits), Burstable (requests < limits), BestEffort (none set)
- Probe types: `httpGet`, `exec`, `tcpSocket`
- Liveness failure = restart. Readiness failure = remove from endpoints. Startup failure = kill.
- `initialDelaySeconds`, `periodSeconds`, `failureThreshold` control probe timing
- Exit code 137 = OOMKilled (128 + SIGKILL)

---

## Documentation
Create `day-57-resources-probes.md` with:
- Requests vs limits (scheduling vs enforcement)
- What happens when CPU or memory limits are exceeded
- Liveness vs readiness vs startup probes
- Screenshots of OOMKilled, Pending, and probe events

---

## Submission
1. Add `day-57-resources-probes.md` to `2026/day-57/`
2. Commit and push to your fork

---

## Learn in Public
Share on LinkedIn: "Set resource requests and limits in Kubernetes today, watched a pod get OOMKilled, and added liveness, readiness, and startup probes for self-healing."

`#90DaysOfDevOps` `#DevOpsKaJosh` `#TrainWithShubham`

Happy Learning!
**TrainWithShubham**
