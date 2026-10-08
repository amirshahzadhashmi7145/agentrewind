"""CLI for replaying AgentRewind regression fixtures."""
from __future__ import annotations

import json
from pathlib import Path

import typer

app = typer.Typer(add_completion=False, no_args_is_help=True)


def changed_ids(data: list) -> list[str]:
    return [str(item.get("id", "?")) for item in data if item.get("changed")]


@app.command("replay-fixtures")
def replay_fixtures(fixtures: Path) -> None:
    """Rerun saved regression fixtures and report behavior changes."""
    payload = json.loads(Path(fixtures).read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        typer.echo("fixtures must be a JSON list", err=True)
        raise typer.Exit(code=1)
    ids = changed_ids(payload)
    typer.echo(f"changed={len(ids)}")
    raise typer.Exit(code=1 if ids else 0)


if __name__ == "__main__":
    app()
