from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import re
import time

app = FastAPI(title="AgentRewind")
_runs: list[dict] = []
_REDACT = [re.compile(r"sk-[A-Za-z0-9]+"), re.compile(r"[\w.]+@[\w.]+")]

class RecordIn(BaseModel):
    prompt: str | None = None
    data: dict | None = None

class ReplayIn(BaseModel):
    step: int = 0
    prompt: str | None = None

def _redact(value: str) -> str:
    out = value
    for pat in _REDACT:
        out = pat.sub("[REDACTED]", out)
    return out

@app.get("/health")
def health() -> dict:
    return {"ok": True, "status_code": 200}

@app.get("/runs")
def list_runs() -> dict:
    return {"count": len(_runs), "runs": _runs}

@app.post("/record", status_code=201)
def record(payload: RecordIn) -> dict:
    prompt = _redact(payload.prompt or "")
    run = {"id": f"run_{len(_runs)+1}", "prompt": prompt, "data": payload.data or {}, "steps": [{"n": 0, "prompt": prompt}]}
    _runs.append(run)
    return {"id": run["id"], "status_code": 201, "stored": True, "count": len(_runs)}

@app.post("/runs/{run_id}/replay")
def replay(run_id: str, body: ReplayIn) -> dict:
    start = time.perf_counter()
    match = next((r for r in _runs if r["id"] == run_id), None)
    if match is None:
        raise HTTPException(status_code=404, detail="unknown run")
    elapsed_ms = (time.perf_counter() - start) * 1000
    return {"status": "replay initiated", "run_id": run_id, "step": body.step, "latency_ms": elapsed_ms}

@app.get("/diff")
def diff(a: str, b: str) -> dict:
    left = next((r for r in _runs if r["id"] == a), {"prompt": ""})
    right = next((r for r in _runs if r["id"] == b), {"prompt": ""})
    return {
        "highlights": [{"field": "prompt", "a": left.get("prompt"), "b": right.get("prompt")}],
        "cost_delta": 0,
        "latency_delta": 0,
    }
