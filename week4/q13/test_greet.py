import pytest
from greetlab.cli import main
import sys
from io import StringIO


def test_normal_name(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["sdt-greet", "--name", "Tom"])
    main()
    captured = capsys.readouterr()
    assert "Hello, Tom!" in captured.out


def test_blank_name(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["sdt-greet", "--name", "   "])
    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 2
