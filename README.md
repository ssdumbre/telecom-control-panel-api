# Telecom Control Panel API

A FastAPI-based REST API for monitoring free5GC 5G Core Network Functions running on Kubernetes.

## Overview

This project provides simple REST endpoints to retrieve the status of free5GC network function pods from a Kubernetes cluster.
It helps avoid manual kubectl commands for basic monitoring and troubleshooting.

UERANSIM is used in the setup to simulate UE/gNB traffic towards the 5G Core.

## What This Does

* Retrieves real-time pod status of 5G Core network functions (e.g., AMF)
* Lists all free5GC pods in the Kubernetes namespace
* Helps verify whether network functions are running or failing

## Architecture Flow

FastAPI → kubectl → Kubernetes → free5GC Pods

## Prerequisites

* free5GC deployed on Kubernetes (MicroK8s)
* UERANSIM for UE/gNB simulation
* Python 3.8+
* kubectl configured with cluster access

## Installation

pip install -r requirements.txt

## Run

uvicorn main:app --reload --host 0.0.0.0 --port 8000

## Endpoints

* GET /amf
  Returns status of AMF pod

* GET /pods
  Returns list of all free5GC pods

## Example Response

{
"pod": "free5gc-helm-free5gc-amf-amf-5c795dc8c5",
"status": "Running"
}

## Tech Stack

* FastAPI
* Python
* Kubernetes
* kubectl
* free5GC
* UERANSIM

## Use Case

This project can be used in telecom environments or lab setups to provide API-based monitoring of 5G Core network functions.
It can serve as a lightweight building block for OSS systems where automated visibility of CNFs is required.
