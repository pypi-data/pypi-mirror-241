import sys
import subprocess
from use_openai import explain_error_with_gpt

def run_script(script_path):
    try:
        output = subprocess.check_output([sys.executable, script_path], stderr=subprocess.STDOUT)
        print(output.decode())
    except subprocess.CalledProcessError as e:
        error_output = e.output.decode()
        explanation = explain_error_with_gpt(error_output)
        print("titanic")
        print(error_output)
        print("titanic")
        print(explanation)
        print("titanic")
