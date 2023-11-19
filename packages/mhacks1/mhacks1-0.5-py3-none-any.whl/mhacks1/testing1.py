import sys
import subprocess

def run_script(script_path):
    try:
        output = subprocess.check_output([sys.executable, script_path], stderr=subprocess.STDOUT)
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print("titanic")
        print("Error Output:\n", e.output.decode())
        print("Return Code:", e.returncode)
        print("titanic")
