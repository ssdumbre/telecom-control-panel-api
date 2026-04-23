# Telecom Control Panel API

A FastAPI-based REST API for monitoring free5GC : 5G Core Network Functions running on Kubernetes.

## What This Does
- Exposes REST endpoints to monitor live 5G NF pods
- Retrieves real-time pod status from Kubernetes cluster
- Validates free5GC deployment health via API

## Prerequisites
- free5GC deployed on Kubernetes (MicroK8s)
- Python 3.8+
- kubectl configured

## Installation
pip install -r requirements.txt

## Run
uvicorn main:app --reload --host 0.0.0.0 --port 8000

## Endpoints
GET /amf    → AMF pod status
GET /pods   → All free5GC pods

## Example Response
{
  "pod": "free5gc-helm-free5gc-amf-amf-5c795dc8c5",
  "status": "Running"
}

## Tech Stack
FastAPI, Python, kubectl, Kubernetes, free5GC
