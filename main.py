import os
from fastapi import FastAPI, Response, status

app = FastAPI()
DB_PASSWORD = os.getenv("DB_PASSWORD", "default_pass")

@app.get("/")
def root():
    return {"status": "ok", "message": "Hello T-Bank!"}

@app.get("/healthz")
def liveness():
    return {"status": "healthy"}

@app.get("/ready")
def readiness():
    if DB_PASSWORD:
        return {"status": "ready"}
    return Response(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)