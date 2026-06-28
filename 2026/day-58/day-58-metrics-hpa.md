# Day 58 – Metrics Server and Horizontal Pod Autoscaler (HPA)

## Challenge Tasks

### Task 1: Install the Metrics Server
1. Check if it is already running: `kubectl get pods -n kube-system | grep metrics-server`
2. If not, install it:
   - Minikube: `minikube addons enable metrics-server`
   - Kind/kubeadm: apply the official manifest from the metrics-server GitHub releases
3. On local clusters, you may need the `--kubelet-insecure-tls` flag (never in production)
4. Wait 60 seconds, then verify: `kubectl top nodes` and `kubectl top pods -A`

**Verify:** What is the current CPU and memory usage of your node?

<img width="1362" height="480" alt="task1" src="https://github.com/user-attachments/assets/92632540-45ab-4508-acce-666528f28e1f" />

<img width="1345" height="392" alt="task1b" src="https://github.com/user-attachments/assets/44d7e9a1-c90b-474d-beab-26384105e485" />


---

### Task 2: Explore kubectl top
1. Run `kubectl top nodes`, `kubectl top pods -A`, `kubectl top pods -A --sort-by=cpu`
2. `kubectl top` shows real-time usage, not requests or limits — these are different things
3. Data comes from the Metrics Server, which polls kubelets every 15 seconds

**Verify:** Which pod is using the most CPU right now? my cluster control plane pod is using the most CPU right now

<img width="1372" height="710" alt="task2" src="https://github.com/user-attachments/assets/cc737535-e6cd-469d-9c3a-8e254bd5c995" />

---

### Task 3: Create a Deployment with CPU Requests
1. Write a Deployment manifest using the `registry.k8s.io/hpa-example` image (a CPU-intensive PHP-Apache server)
2. Set `resources.requests.cpu: 200m` — HPA needs this to calculate utilization percentages
3. Expose it as a Service: `kubectl expose deployment php-apache --port=80`

Without CPU requests, HPA cannot work — this is the most common HPA setup mistake.

<img width="794" height="265" alt="task3-a" src="https://github.com/user-attachments/assets/33bae8c9-b0b5-4f28-8a04-200365a3ba39" />

<img width="1347" height="716" alt="task3-b" src="https://github.com/user-attachments/assets/a4773416-1e13-4e43-9e7b-0aab8522325c" />

<img width="1348" height="568" alt="task3-c" src="https://github.com/user-attachments/assets/1799c208-2a5c-45ef-88ff-39f3149aafdd" />

**Verify:** What is the current CPU usage of the Pod?

<img width="672" height="98" alt="task3-d" src="https://github.com/user-attachments/assets/5a99e5af-998f-459b-b83f-e33a2c71c63e" />

The task is teaching:

Metrics Server → Measures CPU

Deployment → Runs Pods

CPU Requests → Define "normal capacity"

HPA → Compares actual usage vs requested capacity

CPU is measured in millicores.
```
1000m = 1 CPU core
500m  = 0.5 CPU
200m  = 0.2 CPU
100m  = 0.1 CPU

```

---

### Task 4: Create an HPA (Imperative)
1. Run: `kubectl autoscale deployment php-apache --cpu-percent=50 --min=1 --max=10`
2. Check: `kubectl get hpa` and `kubectl describe hpa php-apache`
3. TARGETS may show `<unknown>` initially — wait 30 seconds for metrics to arrive

This scales up when average CPU exceeds 50% of requests, and down when it drops below.

<img width="1313" height="676" alt="task4" src="https://github.com/user-attachments/assets/e2a095eb-9391-4178-8469-18e371e47b72" />

<img width="1333" height="728" alt="task4-b" src="https://github.com/user-attachments/assets/de6d0650-dd61-4ac6-8898-585a5f1b5147" />

**Verify:** What does the TARGETS column show? cpu: 0%/50% 

HPA is not magic.

It constantly does:

Measure CPU
      ↓
Compare with target
      ↓
Increase or decrease Pod

HPA does:

CPU too high?
→ Add Pods.

CPU too low?
→ Remove Pods.

---

### Task 5: Generate Load and Watch Autoscaling
1. Start a load generator: `kubectl run load-generator --image=busybox:1.36 --restart=Never -- /bin/sh -c "while true; do wget -q -O- http://php-apache; done"`
2. Watch HPA: `kubectl get hpa php-apache --watch`
3. Over 1-3 minutes, CPU climbs above 50%, replicas increase, CPU stabilizes
4. Stop the load: `kubectl delete pod load-generator`
5. Scale-down is slow (5-minute stabilization window) — you do not need to wait

**Verify:** How many replicas did HPA scale to under load? 1

<img width="1327" height="698" alt="task5" src="https://github.com/user-attachments/assets/8eb0b084-8aa2-46fa-be96-96e98b130165" />

---

### Task 6: Create an HPA from YAML (Declarative)
1. Delete the imperative HPA: `kubectl delete hpa php-apache`
2. Write an HPA manifest using `autoscaling/v2` API with CPU target at 50% utilization
3. Add a `behavior` section to control scale-up speed (no stabilization) and scale-down speed (300 second window)
4. Apply and verify with `kubectl describe hpa`

`autoscaling/v2` supports multiple metrics and fine-grained scaling behavior that the imperative command cannot configure.

<img width="1346" height="726" alt="task6" src="https://github.com/user-attachments/assets/06139de7-25a8-4ccb-8ca8-2f3392c8ad68" />


**Verify:** What does the `behavior` section control?

The behavior section controls how aggressively or conservatively the HPA changes the replica count.

Without behavior, Kubernetes uses default scaling rules.

With behavior, you can control:

1. Scale-Up Behavior

Controls how fast new Pods are added when load increases.

scaleUp:
  stabilizationWindowSeconds: 0
No waiting period.
HPA reacts immediately to high CPU usage.
Pods can be added as soon as metrics exceed the target.

Example:

Current replicas: 2
CPU utilization: 90%
Target: 50%

HPA immediately scales up.
2. Scale-Down Behavior

Controls how fast Pods are removed when load decreases.

scaleDown:
  stabilizationWindowSeconds: 300
HPA waits 300 seconds (5 minutes) before reducing replicas.
Prevents rapid scale-downs caused by temporary drops in traffic.

Example:

Current replicas: 6
CPU drops below target

HPA waits 5 minutes before removing Pods.

If traffic rises again during those 5 minutes, scaling down may never happen.


Why is this useful?

Imagine traffic looks like this:

High load  -> scale to 8 Pods
Short dip  -> scale to 2 Pods
High load  -> scale to 8 Pods again

Without stabilization:

8 -> 2 -> 8 -> 2

This is called flapping or thrashing.

With:

scaleDown:
  stabilizationWindowSeconds: 300

Kubernetes waits before removing Pods, reducing unnecessary scaling actions.

---

### Task 7: Clean Up
Delete the HPA, Service, Deployment, and load-generator pod. Leave the Metrics Server installed.

<img width="911" height="336" alt="task7" src="https://github.com/user-attachments/assets/26c05362-3fac-4e97-bac5-6ced7a03b4d0" />


---

## Hints
- HPA requires `resources.requests` — without them TARGETS shows `<unknown>`
- `kubectl top` = actual usage. `kubectl describe pod` = configured requests/limits
- HPA checks every 15 seconds. Scale-up is fast, scale-down has a 5-minute stabilization window
- `autoscaling/v1` = CPU only. `autoscaling/v2` = CPU + memory + custom metrics
- Formula: `desiredReplicas = ceil(currentReplicas * (currentUsage / targetUsage))`
- HPA works with Deployments, StatefulSets, and ReplicaSets

---

## Documentation
Create `day-58-metrics-hpa.md` with:
- What the Metrics Server is and why HPA needs it
- How HPA calculates desired replicas
- The difference between `autoscaling/v1` and `v2`
- Screenshots of `kubectl top`, HPA events, and pod scaling

---

## Submission
1. Add `day-58-metrics-hpa.md` to `2026/day-58/`
2. Commit and push to your fork

---

## Learn in Public
Share on LinkedIn: "Set up Kubernetes HPA today. Watched my app auto-scale from 1 to multiple replicas under load, then scale back down. This is how production handles variable traffic."

`#90DaysOfDevOps` `#DevOpsKaJosh` `#TrainWithShubham`

Happy Learning!
**TrainWithShubham**
