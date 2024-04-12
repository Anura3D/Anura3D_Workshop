import subprocess
import os

def run_executable(executable_path, argument):
    try:
        # Run the executable with the specified argument
        subprocess.run([executable_path, argument], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except FileNotFoundError:
        print("Error: Executable not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_highest_file(directory, base_extension):
    # Get a list of files in the directory
    files = os.listdir(directory)
    
    # Filter the files to only include those with the specified extension
    files = [file for file in files if base_extension in file]
    
    if not files:
        return None  # No matching files found

    # Extract the numeric parts of the filenames and convert them to integers
    file_numbers = [int(file.split(base_extension)[1]) for file in files]
    
    # Find the maximum number
    highest_number = max(file_numbers)
    
    highest_file_extension = f"{base_extension}{highest_number:03d}"
    # Construct the filename with the highest number
    highest_file = [file for file in files if highest_file_extension in file][0]  # Assuming the filenames are zero-padded
    
    return highest_file

def overwrite_line_after_string(filename, target_string, new_value):
    # Open the file in read mode
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Open the file in write mode to overwrite it
    with open(filename, 'w') as file:
        found_string = False
        for i, line in enumerate(lines):
            # Check if the target string is found in the current line
            if target_string in line:
                found_string = True
                # Write the string unchanged
                file.write(line)
            # If the target string was found in the previous line, overwrite the current line
            elif found_string:
                file.write(new_value + '\n')
                found_string = False
            # Otherwise, write the current line unchanged
            else:
                file.write(line)
    #TODO: Add

def delete_files_with_extensions(directory, keep_extensions):
    try:
        # List all files in the directory
        files = os.listdir(directory)
        
        # Filter out the files with extensions you want to keep
        files_to_keep = [file for file in files if any(file.endswith(ext) for ext in keep_extensions)]
        
        # Delete the files that don't have the specified extensions
        for file in files:
            if file not in files_to_keep:
                os.remove(os.path.join(directory, file))
        
        print("Files deleted successfully.")
    except Exception as e:
        print("An error occurred:", e)