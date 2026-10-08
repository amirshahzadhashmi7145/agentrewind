from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AgentRewind")
_runs: list[dict] = []

class RecordIn(BaseModel):
    prompt: str | None = None
    data: dict | None = None

@app.get("/health")
def health() -> dict:
    return {"ok": True, "status_code": 200}

@app.get("/runs")
def list_runs() -> dict:
    return {"count": len(_runs), "runs": _runs}

@app.post("/record", status_code=201)
def record(payload: RecordIn) -> dict:
    run = {"id": f"run_{len(_runs)+1}", "prompt": payload.prompt, "data": payload.data or {}}
    _runs.append(run)
    return {"id": run["id"], "status_code": 201, "stored": True, "count": len(_runs)}
