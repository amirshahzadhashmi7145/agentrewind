import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from fastapi.testclient import TestClient
from backend.main import app

def test_record_redacts_api_keys_and_emails() -> None:
    client = TestClient(app)
    response = client.post(
        "/record",
        json={"prompt": "key sk-ABC123email user@example.com"},
    )
    assert response.status_code == 201
    stored = client.get("/runs").json()["runs"][-1]["prompt"]
    assert "sk-ABC123" not in stored
    assert "user@example.com" not in stored
    assert "[REDACTED]" in stored
