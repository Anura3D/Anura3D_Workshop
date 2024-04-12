import subprocess

# def run_executable(executable_path, argument):
#     try:
#         # Open the executable with the specified argument
#         process = subprocess.Popen([executable_path, argument], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        
#         print("Hello")
#         # Read the output while the process is running
#         output_text = ''
#         while True:
#             output = process.stdout.readline()
#             if output == '' and process.poll() is not None:
#                 break
#             if output:
#                 output_text += output.strip() + '\n'
        
#         # Return the captured output
#         return output_text
#     except FileNotFoundError:
#         return "Error: Executable not found."
#     except Exception as e:
#         return f"An error occurred: {e}"

def run_executable(executable_path, argument):
    try:
        # Open the executable with the specified argument
        process = subprocess.Popen([executable_path, argument], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        
        # Communicate with the process and capture stdout and stderr
        stdout, stderr = process.communicate()
        
        # Check if there was any error
        if process.returncode != 0:
            return f"Error: {stderr}"
        
        # Return the captured output
        return stdout.strip()
    except FileNotFoundError:
        return "Error: Executable not found."
    except Exception as e:
        return f"An error occurred: {e}"