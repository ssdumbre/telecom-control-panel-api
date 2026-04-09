from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/pods")
def get_pods():
    result = subprocess.run(
        ["kubectl", "get", "pods"],
        capture_output=True,
        text=True
    )
    return {"pods": result.stdout}
