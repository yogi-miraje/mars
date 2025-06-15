from click.testing import CliRunner
from mars.cli import cli


def test_cli_demo(monkeypatch):
    runner = CliRunner()
    monkeypatch.setattr(
        "requests.post",
        lambda url, params: type("Resp", (), {"json": lambda self=None: {"task_id": "1", "result": {"echo": params}}})(),
    )
    result = runner.invoke(cli, ["demo", "u1", "p1", "hi"])
    assert result.exit_code == 0
