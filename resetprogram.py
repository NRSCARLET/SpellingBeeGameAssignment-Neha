import subprocess


def relaunch():
    python_script = "MenuWindow.py"
    subprocess.run(["python", python_script])


def RP():
    try:
        raise SystemExit
    except SystemExit:
        print("loading... Please wait...")
        relaunch()

RP()