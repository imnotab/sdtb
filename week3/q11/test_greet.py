import subprocess
import pytest

def test_normal_name():
    ret = subprocess.run(["sdt-greet", "--name", "Alice"], capture_output=True, text=True)
    assert ret.returncode == 0
    assert "Hello, Alice!" in ret.stdout

def test_blank_name():
    ret = subprocess.run(["sdt-greet", "--name", "   "], capture_output=True, text=True)
    assert ret.returncode == 2
