import sys
import subprocess

def run_script(script_path):
    try:
        subprocess.check_call([sys.executable, script_path])
    except subprocess.CalledProcessError as e:
        print("titanic")
        print(e)
        print("titanic")
