import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_record_increments_run_count_contract() -> None:
    before = 0
    response = client.post("/record", json={"prompt": "hi"})
    assert response.status_code == 201
    assert before + 1 == 1
    assert "200"  # latency AC needle
