# AI-BankApp-DevOps

A production-ready full-stack banking application built with Spring Boot and MySQL, featuring secure authentication, account management, and transaction processing. Integrated with a complete DevOps pipeline using Docker, GitHub Actions CI/CD, Kubernetes, Helm, Terraform, Prometheus, and ArgoCD for scalable, automated, and observable deployments.

<img width="1355" height="635" alt="dashboard-app" src="https://github.com/user-attachments/assets/28458f41-f104-4acd-9f86-e16fd49536de" />

## 🏗️ Architecture 

A cloud-native AI banking application built with Spring Boot, containerized using Docker, and deployed via GitHub Actions CI/CD. It leverages Kubernetes for scalability, ArgoCD for GitOps, and Prometheus & Grafana for monitoring.

![architecture](https://github.com/user-attachments/assets/3daa07a3-51b6-4918-b87f-63cb48d7a278)


## 🧰 Tech Stack

| Category        | Technologies |
|----------------|-------------|
| **Backend**     | Spring Boot 3.4.1, Java 21, Spring Security, JPA/Hibernate |
| **Frontend**    | Thymeleaf, Bootstrap 5, Glassmorphism UI (Dark/Light Theme) |
| **Database**    | MySQL 8.0 |
| **AI**          | Ollama (Self-hosted LLM chatbot) |
| **Containerization** | Docker |
| **CI/CD**       | GitHub Actions |
| **Orchestration** | Kubernetes |
| **Package Management** | Helm |
| **Infrastructure as Code** | Terraform |
| **Monitoring**  | Prometheus, Grafana |
| **GitOps**      | ArgoCD |


## ⚙️ Features

- 🤖 AI-powered banking assistant  
- 🔐 Secure authentication  
- 🌗 Dark/Light themed UI  
- 🐳 Dockerized application  
- ☁️ Cloud-ready architecture  
- 📊 Monitoring-ready setup

## Getting Started
Run with Docker Compose 
```
git clone https://github.com/Sana-2026/AI-BankApp-DevOps
AI-BankApp-DevOps
docker compose up --build
```
---

## ☁️ Deployment

* Hosted on AWS EC2
* Containerized using Docker
* Future-ready for Kubernetes deployment

---

## 🔄 CI/CD Pipeline

A fully automated CI/CD pipeline is implemented using GitHub Actions, triggered on every push and pull request to the `main` branch:

- 🏗️ **Build & Test:** Compile the application and run unit tests using Maven  
- 🐳 **Docker Build:** Create optimized multi-stage Docker images  
- 🧪 **Health Check:** Validate application using `test-health.sh`  
- 📦 **Image Push:** Push Docker image to Docker Hub with:
  - Unique tag (`git SHA`)
  - Stable tag (`latest`)
    
---

## 📊 Monitoring & Observability

* Prometheus (Metrics collection)
* Grafana (Visualization dashboards)

---

## 🚀 Future Enhancements

* Kubernetes auto-deployment with Helm
* GitOps using ArgoCD
* Terraform-based infrastructure provisioning
* Advanced AI banking features

---

## 👨‍💻 Author

Sana Shaik

---

🔥 Built as part of DevOps Capstone Project



   
