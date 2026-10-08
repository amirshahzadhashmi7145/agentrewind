import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from fastapi.testclient import TestClient
from backend.main import app

def test_recording_increases_stored_count_by_one() -> None:
    client = TestClient(app)
    before = client.get("/runs").json()["count"]
    response = client.post("/record", json={"prompt": "store"})
    assert response.status_code == 201
    assert client.get("/runs").json()["count"] == before + 1
