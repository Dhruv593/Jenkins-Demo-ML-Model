# Docker-Based Microservices ML System

## Overview

This project demonstrates a simple microservices architecture using Docker and Docker Compose.  
It consists of multiple containerized services connected through a custom Docker bridge network, with Nginx acting as a reverse proxy and single entry point.

The system showcases:

- Docker containerization
- Service-to-service communication via Docker networking
- Reverse proxy architecture using Nginx
- Multi-container orchestration with Docker Compose

---

## Services

### 1. Frontend Service
Provides the user interface and sends API requests through the Nginx gateway.

### 2. Backend Service
Handles REST API requests and communicates internally with the ML service for predictions.

### 3. ML Service
Hosts the machine learning model and exposes prediction and health endpoints.  
Accessible only within the Docker network.

### 4. Nginx Gateway
Acts as a reverse proxy:
- Routes `/` → Frontend
- Routes `/api/` → Backend
- Exposes a single public port
- Protects internal services

Internal container communication example:

---

## Prerequisites

Make sure the following are installed:

- Docker
- Docker Compose (v2+)

Verify installation:

```bash
docker --version
docker compose version
```
---
## How to Clone and Run

### 1. Clone the Repository

```bash
git clone https://github.com/Dhruv593/Docker-Network-Iris-Classification.git
cd Docker-Network-Iris-Classification
```

### 2. Build All Services

```bash
docker compose build
```

### 3. Start the Application

```bash
docker compose up -d
```

### 4. Access the Application

```bash
http://localhost:8080
```

### 5. View logs (optional)

```bash
docker compose logs -f
```

### 6. Stop the Application

```bash
docker compose down
```