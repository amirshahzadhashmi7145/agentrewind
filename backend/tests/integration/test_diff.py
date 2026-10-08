import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from fastapi.testclient import TestClient
from backend.main import app

def test_diff_highlights_output_changes() -> None:
    client = TestClient(app)
    a = client.post("/record", json={"prompt": "one"}).json()["id"]
    b = client.post("/record", json={"prompt": "two"}).json()["id"]
    response = client.get("/diff", params={"a": a, "b": b})
    assert response.status_code == 200
    body = response.json()
    assert body["highlights"]
    assert "cost_delta" in body and "latency_delta" in body
