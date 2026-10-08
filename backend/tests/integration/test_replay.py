import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from fastapi.testclient import TestClient
from backend.main import app

def test_replay_initiated_response() -> None:
    client = TestClient(app)
    run_id = client.post("/record", json={"prompt": "x"}).json()["id"]
    response = client.post(f"/runs/{run_id}/replay", json={"step": 0})
    assert response.status_code == 200
    assert response.json()["status"] == "replay initiated"
    assert response.json()["latency_ms"] < 200
