# 🚀 DevOps Lab Project – CI/CD Pipeline for Flask Web Application

**Student:** Manahil Khan  
**Course:** DevOps – Lab Project  

This project demonstrates a **complete DevOps workflow** by building, containerizing, deploying, and monitoring a **Flask + MySQL web application** using **CI/CD automation, Docker, Kubernetes, Jenkins, Prometheus, and Grafana**.

---

## 🎯 Project Objectives

- Build a simple web application using **Flask & MySQL**
- Implement **CI/CD automation** using Jenkins
- Containerize the application using **Docker**
- Deploy the application on **Kubernetes**
- Automate builds & deployments via **GitHub Webhooks**
- Monitor application & cluster metrics using **Prometheus & Grafana**

---

## 🏗️ System Architecture

**Pipeline Flow:**

GitHub  
→ Jenkins CI/CD  
→ Docker Build & Push  
→ DockerHub  
→ Kubernetes Deployment  
→ Flask Web App + MySQL  
→ Monitoring (Prometheus & Grafana)

---

## 🌐 Application Overview

### Web Application
- **Backend:** Flask (Python)
- **Database:** MySQL
- **Containerized:** Docker
- **Deployed on:** Kubernetes

### Features
- Flask-based web interface
- MySQL persistent database
- Scalable deployment using Kubernetes replicas
- Automated deployment via Jenkins pipeline

---

## ⚙️ Tools & Technologies Used

| Category | Tools |
|------|------|
| CI/CD | Jenkins |
| Version Control | GitHub |
| Containers | Docker |
| Orchestration | Kubernetes |
| Monitoring | Prometheus, Grafana |
| Cloud | AWS EC2 |
| Backend | Flask (Python) |
| Database | MySQL |

---

## 🔁 CI/CD Pipeline (Jenkins)

### Pipeline Stages
1. **Code Fetch** – Pull code from GitHub
2. **Docker Build** – Build Flask application image
3. **Docker Push** – Push image to DockerHub
4. **Kubernetes Deploy** – Deploy app & MySQL
5. **Monitoring Validation** – Verify Prometheus & Grafana

### Automation Features
- GitHub Webhook triggers pipeline automatically
- DockerHub credentials securely stored in Jenkins
- Kubernetes manifests applied via pipeline

---

## 🐳 Docker Configuration

### Dockerfile Highlights
- Python 3.10 slim base image
- Dependency installation via `requirements.txt`
- Flask app exposed on port `5000`
- Lightweight and production-ready image

---

## ☸️ Kubernetes Deployment

### Kubernetes Components
- **Deployment**
  - Flask Web App (2 replicas)
  - MySQL Database (1 replica)
- **Services**
  - NodePort service for web app
  - ClusterIP service for MySQL
- **Persistent Storage**
  - PVC for MySQL data persistence

### Benefits
- High availability
- Scalability
- Persistent data storage

---

## 📦 Kubernetes Files Included

- `deployment.yaml` – Flask application deployment
- `service.yaml` – Web app service
- `mysql-deployment.yaml` – MySQL deployment
- `mysql-service.yaml` – MySQL service
- `pvc.yaml` – Persistent Volume Claim

---

## 📊 Monitoring & Observability

### Prometheus
- Collects Kubernetes & application metrics
- Queries executed:
  - Pod status
  - Memory usage
  - Pod information

### Grafana
- Visual dashboards for:
  - Pod health
  - Resource utilization
  - Cluster monitoring

### Access
- **Prometheus:** `http://<EC2-IP>:9090`
- **Grafana:** `http://<EC2-IP>:3000`  
  *(Default credentials: admin/admin)*

---

## 🔍 Sample Prometheus Queries

```text
kube_pod_status_phase{namespace="default"}
container_memory_usage_bytes{namespace="default"}
kube_pod_info{namespace="default"}
