"""Import this at the top of any build script. It refuses to let a build run
from a tree where the templates have drifted."""
import subprocess, sys, pathlib
_P = pathlib.Path(__file__).resolve().parent

def preflight():
    if "--skip-verify" in sys.argv:
        print("!! template check SKIPPED - do not publish this output")
        return
    r = subprocess.run([sys.executable, str(_P / "verify.py")],
                       capture_output=True, text=True)
    sys.stdout.write(r.stdout)
    if r.returncode != 0:
        sys.stderr.write(r.stderr)
        sys.exit("\nBuild aborted: the templates no longer match. "
                 "Fix them, or re-bless if the change was intended.")
