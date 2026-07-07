
# Day 59 – Helm — Kubernetes Package Manager

---

## Challenge Tasks

### Task 1: Install Helm
1. Install Helm (brew, curl script, or chocolatey depending on your OS)
2. Verify with `helm version` and `helm env`

Three core concepts:
- **Chart** — a package of Kubernetes manifest templates
- **Release** — a specific installation of a chart in your cluster
- **Repository** — a collection of charts (like a package repo)

**Verify:** What version of Helm is installed?

<img width="1354" height="683" alt="task1" src="https://github.com/user-attachments/assets/7955ea07-4cf8-4466-890e-a2a71acb3175" />

---

### Task 2: Add a Repository and Search
1. Add the Bitnami repository: `helm repo add bitnami https://charts.bitnami.com/bitnami`
2. Update: `helm repo update`
3. Search: `helm search repo nginx` and `helm search repo bitnami`

**Verify:** How many charts does Bitnami have?

---

### Task 3: Install a Chart
1. Deploy nginx: `helm install my-nginx bitnami/nginx`
2. Check what was created: `kubectl get all`
3. Inspect the release: `helm list`, `helm status my-nginx`, `helm get manifest my-nginx`

One command replaced writing a Deployment, Service, and ConfigMap by hand.

Helm created:

✅ 1 Deployment
✅ 1 ReplicaSet
✅ 1 Pod
✅ 1 Service (LoadBalancer)

**Verify:** How many Pods are running? What Service type was created?


<img width="1365" height="678" alt="task3-a" src="https://github.com/user-attachments/assets/bbc7e2ba-bbbe-4558-abfe-df62d5b913ec" />

<img width="1349" height="483" alt="task3-b" src="https://github.com/user-attachments/assets/0871a29e-a7bb-40d2-a90a-f3d9dcd8a9ee" />

<img width="1366" height="722" alt="task3-c" src="https://github.com/user-attachments/assets/96107c13-c7ef-4608-b65d-57fb0889563c" />

<img width="1366" height="708" alt="task3-d" src="https://github.com/user-attachments/assets/ca4b480e-18ea-4ded-8734-0c480f73ca6a" />

<img width="1365" height="117" alt="task3-e" src="https://github.com/user-attachments/assets/d24eca8b-a96a-415f-be18-70fd2047ede6" />



---

### Task 4: Customize with Values
1. View defaults: `helm show values bitnami/nginx`
2. Install a custom release with `--set replicaCount=3 --set service.type=NodePort`
3. Create a `custom-values.yaml` file with replicaCount, service type, and resource limits
4. Install another release using `-f custom-values.yaml`
5. Check overrides: `helm get values <release-name>`

**Verify:** Does the values file release have the correct replicas and service type? yes

<img width="1356" height="726" alt="task4-a" src="https://github.com/user-attachments/assets/295312ce-2183-4bff-a542-f821fad6b622" />

<img width="1345" height="734" alt="task4-2-a" src="https://github.com/user-attachments/assets/821aca50-b9ec-4911-8550-2f2b12d019eb" />

<img width="779" height="149" alt="task4-2-b" src="https://github.com/user-attachments/assets/42bfaec6-f993-480a-bf78-8a2c133f17ed" />


<img width="1366" height="715" alt="task4-3-a" src="https://github.com/user-attachments/assets/21fb9908-4f2e-492d-9c4d-a2004689ec43" />

<img width="1240" height="539" alt="task4-3-b" src="https://github.com/user-attachments/assets/53516551-e6ba-49dd-a756-6ec37e35221d" />


---

### Task 5: Upgrade and Rollback
1. Upgrade: `helm upgrade my-nginx bitnami/nginx --set replicaCount=5`
2. Check history: `helm history my-nginx`
3. Rollback: `helm rollback my-nginx 1`
4. Check history again — rollback creates a new revision (3), not overwriting revision 2

Same concept as Deployment rollouts from Day 52, but at the full stack level.

**Verify:** How many revisions after the rollback? 3

<img width="1366" height="725" alt="task-5-a" src="https://github.com/user-attachments/assets/92e0edf1-eab9-436e-8e5e-3170011983c0" />

<img width="1366" height="184" alt="task5-1-b" src="https://github.com/user-attachments/assets/04c511eb-1df4-431c-b933-532f3e5bda1b" />

<img width="1304" height="391" alt="task5-c" src="https://github.com/user-attachments/assets/8cb5d0ee-f3b8-48a7-9fc5-708e18884fdb" />


---

### Task 6: Create Your Own Chart
1. Scaffold: `helm create my-app`
2. Explore the directory: `Chart.yaml`, `values.yaml`, `templates/deployment.yaml`
3. Look at the Go template syntax in templates: `{{ .Values.replicaCount }}`, `{{ .Chart.Name }}`
4. Edit `values.yaml` — set replicaCount to 3 and image to nginx:1.25
5. Validate: `helm lint my-app`
6. Preview: `helm template my-release ./my-app`
7. Install: `helm install my-release ./my-app`
8. Upgrade: `helm upgrade my-release ./my-app --set replicaCount=5`

**Verify:** After installing, 3 replicas? After upgrading, 5?

---

### Task 7: Clean Up
1. Uninstall all releases: `helm uninstall <name>` for each
2. Remove chart directory and values file
3. Use `--keep-history` if you want to retain release history for auditing

**Verify:** Does `helm list` show zero releases?

---

## Hints
- `helm show values <chart>` — see what you can customize
- `--set key=value` for single overrides, `-f values.yaml` for files
- Nested values use dots: `--set service.type=NodePort`
- `helm get values <release>` shows overrides, `--all` for everything
- `helm template` renders without installing — great for debugging
- `helm lint` validates chart structure before installing
- Templates: `{{ .Values.key }}`, `{{ .Chart.Name }}`, `{{ .Release.Name }}`

---

## Documentation
Create `day-59-helm.md` with:
- What Helm is and the three core concepts
- How to install, customize, upgrade, and rollback
- The structure of a Helm chart and how Go templating works
- Your `custom-values.yaml` with explanations

---

## Submission
1. Add `day-59-helm.md` and `custom-values.yaml` to `2026/day-59/`
2. Commit and push to your fork

---

## Learn in Public
Share on LinkedIn: "Learned Helm today — deployed charts, customized with values, performed rollbacks, and created my own chart from scratch. One command replaces dozens of YAML files."

`#90DaysOfDevOps` `#DevOpsKaJosh` `#TrainWithShubham`

Happy Learning!
**TrainWithShubham**
