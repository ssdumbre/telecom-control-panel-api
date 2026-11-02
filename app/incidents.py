from fastapi import FastAPI
import subprocess

app = FastAPI()


# 🔹 Helper function (only hint, not full RCA)
def get_incident_hint(nf, status, restarts):

    if "CrashLoopBackOff" in status:

        if restarts > 5:

            if nf == "SMF":
                return "SMF crashing repeatedly → check smfcfg.yaml, PFCP/UPF connectivity"

            elif nf == "AMF":
                return "AMF crashing repeatedly → check config, NRF registration, SBI/N2 interfaces"

            elif nf == "UPF":
                return "UPF crashing repeatedly → check GTP module, N3/N9 interfaces"

            else:
                return "Repeated crashes → likely application/config issue"

        else:
            return "Pod restarting → possible transient issue"

    elif "Init" in status:
        return "Pod stuck in Init → dependency issue (NRF/DB/service not ready)"

    elif "Error" in status:
        return "Container exited with error → check logs"

    return "Unknown issue"


@app.get("/incidents")
def get_incidents():

    result = subprocess.run(
        ["kubectl", "get", "pods", "-n", "free5gc", "--no-headers"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return {"error": "Failed to get pod status", "details": result.stderr}

    incidents = []

    for line in result.stdout.strip().splitlines():

        parts = line.split()

        # Expected: NAME READY STATUS RESTARTS AGE
        if len(parts) < 5:
            continue

        name = parts[0]
        status = parts[2]

        try:
            restarts = int(parts[3])
        except:
            restarts = 0

        # 🔹 NF mapping
        if "amf" in name:
            nf = "AMF"
        elif "smf" in name:
            nf = "SMF"
        elif "upf" in name:
            nf = "UPF"
        elif "nrf" in name:
            nf = "NRF"
        elif "pcf" in name:
            nf = "PCF"
        else:
            nf = "UNKNOWN"

        # 🔹 Severity + classification logic
        if status == "Running":
            if restarts == 0:
                continue
            else:
                severity = "WARNING"
                category = "RECOVERED"
                risk = "MEDIUM"
                message = "Pod restarted but currently stable"
                recommendation = "Check logs for root cause"

        elif "CrashLoopBackOff" in status:
            severity = "CRITICAL"
            category = "ACTIVE_FAILURE"
            risk = "HIGH"
            message = "Pod crashing repeatedly"
            recommendation = get_incident_hint(nf, status, restarts)

        elif "Init" in status:
            severity = "HIGH"
            category = "DEPENDENCY_ISSUE"
            risk = "HIGH"
            message = "Pod stuck in initialization"
            recommendation = "Check dependent services (NRF/DB)"

        else:
            severity = "MEDIUM"
            category = "UNKNOWN"
            risk = "LOW"
            message = "Unclassified issue"
            recommendation = "Check logs"

        incidents.append({
            "nf": nf,
            "pod_name": name,
            "status": status,
            "restarts": restarts,
            "severity": severity,
            "category": category,
            "risk": risk,
            "message": message,
            "recommendation": recommendation
        })

    return {"incidents": incidents}