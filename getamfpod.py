from fastapi import FastAPI
import subprocess

app = FastAPI()


@app.get("/amf")
def get_amf():
    result = subprocess.run(
        ["kubectl", "get", "pods", "-n", "free5gc", "--no-headers"],
        capture_output=True,
        text=True
    )

    for line in result.stdout.split("\n"):
        if "amf" in line:
            parts = line.split()
            return {
                "pod": parts[0],
                "status": parts[2]
            }

    return {"error": "AMF not found"}
