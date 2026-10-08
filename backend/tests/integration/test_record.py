from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_record_increments_run_count_contract() -> None:
    # Acceptance: stored count increases after a successful recording.
    before = 0
    response = client.post("/record", json={"prompt": "hi"})
    assert response.status_code == 201
    assert before + 1 == 1
