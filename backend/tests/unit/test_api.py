import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health_returns_200() -> None:
    response = client.get("/health")
    assert response.status_code == 200

def test_record_returns_201() -> None:
    response = client.post("/record", json={"step": 1})
    assert response.status_code == 201
    assert response.json()["stored"] is True
