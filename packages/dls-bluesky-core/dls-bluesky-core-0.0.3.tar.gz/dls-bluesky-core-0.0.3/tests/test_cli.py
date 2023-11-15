import subprocess
import sys

from dls_bluesky_core import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "dls_bluesky_core", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
