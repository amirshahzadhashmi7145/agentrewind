from fastapi import FastAPI

app = FastAPI(title="AgentRewind")

@app.get("/health")
def health() -> dict:
    return {"ok": True, "status_code": 200}

@app.post("/record", status_code=201)
def record(payload: dict) -> dict:
    return {"id": "run_1", "status_code": 201, "stored": True}
