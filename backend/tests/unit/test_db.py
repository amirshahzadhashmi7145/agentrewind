from backend.db import connect

def test_sqlite_connects_and_creates_runs_table() -> None:
    conn = connect()
    rows = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='runs'"
    ).fetchall()
    assert rows == [("runs",)]
