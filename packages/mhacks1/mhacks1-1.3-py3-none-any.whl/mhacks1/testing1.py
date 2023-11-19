import sys
import subprocess
import openai
import glob
import os
import platform

is_code_block = False
def color_terminal_code_blocks(text):
    for char in text:
        if char == '`':
            global is_code_block
            is_code_block = not is_code_block
            if is_code_block:
                text = text.replace('`', f'\033[32m`', 1)
            else:
                text = text.replace('`', '\033[0m`', 1)
    return text

def get_and_format_environment_details():
    python_version = sys.version
    operating_system = platform.platform()
    installed_packages = subprocess.getoutput("pip list")
    formatted_details = f"Python Version: {python_version}\n" + \
                        f"Operating System: {operating_system}\n" + \
                        f"Installed Packages:\n{installed_packages}"
    return formatted_details

def get_python_files_contents(script_path):
    script_dir = os.path.dirname(script_path)
    python_files = glob.glob(os.path.join(script_dir, '**', '*.py'), recursive=True)
    files_contents = ""
    for file in python_files:
        with open(file, 'r') as f:
            files_contents += f"\nFile: {os.path.basename(file)}\n\n"
            files_contents += f.read() + "\n"
    return files_contents

def explain_error_with_gpt(error_message):
    openai.api_key = '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'
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that provides precise and concise programming error analyses."},
                {"role": "user", "content": f"Analyze this Python error, provide an explanation, suggest a fix, and identify the file as well as line number to change:\n\n{error_message}"}
            ],
            stream=True
        )
        for message in response:
            if message.choices[0].delta != {}:
                print(color_terminal_code_blocks(message.choices[0].delta.content), end="")
        return ""
    except Exception as e:
        return f"error in contacting OpenAI API: {str(e)}"

def run_script(script_path, custom_prompt=""):
    try:
        output = subprocess.check_output([sys.executable, script_path], stderr=subprocess.STDOUT)
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print("\n\nError Message: ---------------------------------------------------------------------------------------------------------------------------------\n")
        error_output = e.output.decode()
        print("\033[31m" + error_output + "\033[0m")
        print("\nError Analysis: ---------------------------------------------------------------------------------------------------------------------------------\n")
        env_details = get_and_format_environment_details()
        all_files_contents = get_python_files_contents(script_path)
        combined_input = f"Custom Prompt:\n{custom_prompt}\n\nError Output:\n{error_output}\n\nPython Files Contents:\n{all_files_contents}\nEnvironment Details:\n{env_details}"
        explanation = explain_error_with_gpt(combined_input)
        print(explanation + "\n\n")

def main():
    if len(sys.argv) < 2:
        print("usage: mhacks <script_path>")
        sys.exit(1)

    script_path = sys.argv[1]
    custom_prompt = sys.argv[2] if len(sys.argv) > 2 else ""
    run_script(script_path, custom_prompt)

if __name__ == "__main__":
    main()
