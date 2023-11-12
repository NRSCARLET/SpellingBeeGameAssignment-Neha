"""import subprocess
import sys

def restart_program():
    python_script = "Onlinehelpstuff.py"  # Replace with your main script name
    subprocess.run(["python", python_script])

if __name__ == "__main__":
    try:
        # Your main program logic here
        print("Starting the program.")
        # ...

        # Simulate exit
        sys.exit()
    except SystemExit:
        # Restart the program
        print("Restarting the program.")
        restart_program()"""

# launcher_script.py
import subprocess

def restart_program():
    python_script = "Onlinehelpstuff.py"
    subprocess.run(["python", python_script])

if __name__ == "__main__":
    try:
        raise SystemExit
    except SystemExit:
        # Restart the program
        print("Restarting the program.")
        restart_program()
