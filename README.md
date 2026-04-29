🚀 Telecom Control Panel API

A FastAPI-based monitoring and incident detection platform for Kubernetes-based 5G Core Network Functions (CNFs) such as AMF, SMF, and UPF.

This project provides API-driven visibility, incident classification, and operator-assisted troubleshooting for cloud-native telecom environments.

🧠 Overview

5G Core networks run as containerized network functions on Kubernetes.
Troubleshooting using manual kubectl commands is inefficient and time-consuming.

This project introduces an API layer on top of Kubernetes and observability tools to:

Detect abnormal CNF behavior
Classify incidents in a structured way
Provide actionable troubleshooting guidance
Assist operators in faster decision-making

🏗 Architecture

FastAPI → kubectl → Kubernetes (kubeadm) → Calico CNI → free5GC CNFs
                                      ↓
                        Prometheus → Grafana → Loki

⚙️ Environment
Kubernetes (kubeadm-based cluster)
Calico CNI (networking)
free5GC Core (CNFs)
UERANSIM (UE/gNB simulation)
Prometheus (metrics collection)
Grafana (visualization dashboards)
Loki (log aggregation)
Python + FastAPI

🎯 CURRENT FEATURES (IMPLEMENTED)

🔹 1. Pod Monitoring API
GET /pods
Lists Kubernetes pods
Provides quick cluster-level visibility

🔹 2. AMF Status API
GET /amf
Retrieves AMF pod name and status
Helps validate control-plane availability

🔹 3. Incident Detection & Classification API
GET /incidents
Detects non-healthy CNFs
Classifies incidents using:
Severity → CRITICAL / HIGH / WARNING
Category → ACTIVE_FAILURE / DEPENDENCY / RECOVERED
Risk → HIGH / MEDIUM / LOW
Provides actionable troubleshooting recommendations

🔹 4. Observability Integration

The system is integrated with:

Prometheus → metrics collection
Grafana → visualization dashboards
Loki → centralized logs

👉 These tools provide raw data, while this API provides:

Detection + Classification + Recommendation
📊 Example Response (/incidents)
{
  "incidents": [
    {
      "nf": "UPF",
      "status": "CrashLoopBackOff",
      "restarts": 12,
      "severity": "CRITICAL",
      "category": "ACTIVE_FAILURE",
      "risk": "HIGH",
      "message": "Pod crashing repeatedly",
      "recommendation": "Check GTP module, N3/N9 interfaces"
    },
    {
      "nf": "SMF",
      "status": "Running",
      "restarts": 2,
      "severity": "WARNING",
      "category": "RECOVERED",
      "risk": "MEDIUM",
      "message": "Pod restarted but currently stable",
      "recommendation": "Check logs for root cause"
    }
  ]
}
🚀 Industry Value & Differentiation

Modern telecom environments already use Prometheus, Grafana, and Loki.
However, these tools provide metrics and logs, not operational decisions.

This project adds an intelligence layer:

🔹 1. From Data → Actionable Insight
Metrics + Logs → Manual analysis ❌

This system:

Detects → Classifies → Suggests next steps ✅
🔹 2. Faster Troubleshooting (Reduced MTTR)

Instead of:

kubectl → logs → metrics → analysis

You get:

Single API → structured incident + recommendation
🔹 3. Standardized Incident Handling

Provides consistent structure:

Severity
Category
Risk

👉 Avoids inconsistent debugging approaches across engineers

🔹 4. Telecom-Aware Context

Unlike generic tools, this system understands:

AMF (control plane issues → NRF/SBI checks)
UPF (data plane issues → GTP/N3/N9 checks)
🔹 5. Foundation for OSS / AIOps

Acts as a base layer for:

OSS platforms
Alarm correlation systems
Future AI-driven analytics

⚙️ Installation
pip install -r requirements.txt

▶️ Run
uvicorn incident:app --reload --host 0.0.0.0 --port 8000

🧠 PROJECT ROADMAP (IN PROGRESS)

🔜 Monitoring Enhancements
GET /pods/{namespace}
GET /pods/{name}/status
GET /pods/{name}/logs

🔜 Control (Operator-Assisted Only)
POST /pods/{name}/restart (manual trigger, not automatic)

🔜 5G-Specific APIs
GET /sessions
GET /ue/status
GET /gnb/status

🔜 Advanced (Realistic)
Log-based Root Cause Analysis (RCA)
Cross-NF incident correlation
Recommendation engine (decision support, not auto-action)

💬 Author Note

The environment was migrated from MicroK8s to a kubeadm-based Kubernetes cluster with Calico CNI to achieve better networking stability and simulate real-world telecom deployments.
