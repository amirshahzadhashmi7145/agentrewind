import json
from pathlib import Path

from backend.cli import changed_ids, replay_fixtures


def test_changed_ids_empty() -> None:
    assert changed_ids([{"id": "a", "changed": False}]) == []


def test_changed_ids_reports_ids() -> None:
    assert changed_ids([{"id": "b", "changed": True}]) == ["b"]


def test_replay_fixtures_writes_changed_count(tmp_path: Path, capsys) -> None:
    path = tmp_path / "fx.json"
    path.write_text(json.dumps([{"id": "a", "changed": False}]), encoding="utf-8")
    try:
        replay_fixtures(path)
    except SystemExit as exc:
        assert exc.code == 0
    assert "changed=0" in capsys.readouterr().out
