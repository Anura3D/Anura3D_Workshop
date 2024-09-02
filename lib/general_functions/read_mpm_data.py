import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def process_parfiles(directories):
    """
    Loop through each directory in the list, call the read_par_data function, 
    and store the results in a dictionary.
    
    Parameters:
    - directories: A list of directory paths to process.

    Returns:
    - A dictionary where keys are directory paths and values are dictionaries of DataFrames.
    """
    par_dataframes_by_directory = {}

    for dir in directories:
        print(f"Processing '{dir}'")  # Debug print

        try:
            dataframes = read_par_data(dir)  # Call the function
            if dataframes:
                par_dataframes_by_directory[dir] = dataframes  # Store the DataFrames
            else:
                print(f"No data found in '{dir}'")
        except FileNotFoundError:
            print(f"The directory '{dir}' does not exist.")
        except Exception as e:
            print(f"An error occurred while processing '{dir}': {e}")

    return par_dataframes_by_directory



def read_par_data(directory, file_pattern_suffix="PAR_*"):
    """
    Read MPM data from a specified directory and store DataFrames in a dictionary.

    Parameters:
    - directory: The base directory to search for files.
    - file_pattern_suffix: Suffix for the file pattern to find matching files e.g. PAR files.

    Returns:
    - A dictionary with DataFrames for each matching file.
    """

    # Check if the directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")

    # Get the base name and file name without extension
    base_name = os.path.basename(directory)
    file_name = os.path.splitext(base_name)[0]

    print("base name", base_name)
    print("file name:", file_name)

    # Find all files matching the pattern
    file_pattern = f"{directory}/{file_name}.{file_pattern_suffix}"
    matching_files = glob.glob(file_pattern) # matching files 

    # Store DataFrames in a dictionary
    dataframe_dict = {}

    # Read each file into the dictionary with filename as key
    for file in matching_files:
        key = file.split('\\')[-1]  # Get the filename without the extension
        df = pd.read_csv(file, sep="\s+")
        dataframe_dict[key] = df

    return dataframe_dict


# def plot_analytical_numerical_solutions(par_dataframes_by_directory, u_z, DepthArray, NondimensionalTime, TractionLoad):
#     """
#     Plot analytical and numerical solutions for each directory in par_dataframes_by_directory.

#     Parameters:
#     - par_dataframes_by_directory: Dictionary with DataFrames from different directories.
#     - u_z: Analytical solution data (e.g., Fourier series).
#     - DepthArray: Array representing depths.
#     - NondimensionalTime: Array of non-dimensional times.
#     - target_times: Array of times to compare with.
#     - Traction load for normalization
#     """

#     # Define line styles, markers, and colors for variety
#     line_styles = ["-", "--", ":", "-."]
#     markers = ["o", "s", "^", "d"]
#     colors = ["r", "g", "b", "y", "m", "c"]

    
#     #TractionLoad = -10  # Normalize numerical isochrone

#     # Plot Analytical and Numerical Solutions for each directory
#     for dir_key, dataframes in par_dataframes_by_directory.items():  # Loop through each directory
#         plt.figure(figsize=(10, 6))  # Set the plot size

#         # Plot the Analytical Solution
#         for kk in range(len(NondimensionalTime)):
#             style = line_styles[kk % len(line_styles)]
#             marker = markers[kk % len(markers)]

#             plt.plot(
#                 u_z[:, kk],
#                 DepthArray,
#                 color='black',  # All lines are black
#                 linestyle=style,
#                 marker=marker,
#                 markersize=4,
#                 markerfacecolor='none',
#                 #label=f'Analytical - Time {NondimensionalTime[kk]}'  # Label for legend
#             )

#         # Plot Data from the Current Directory
#         for key, df in dataframes.items():  # Loop through the DataFrames for this directory
#             for j, t in enumerate(NondimensionalTime):  # Loop through target times
#                 color = colors[j % len(colors)]  # Color based on target times

#                 # Find the closest index to the target time
#                 closest_index = np.argmin(np.abs(df["Time"] - t)) # minimize the difference

#                 # Get the corresponding row
#                 row = df.iloc[closest_index]

#                 # Plot with open circles (same color for the same time)
#                 plt.plot(
#                     row["WPressure"] / TractionLoad,
#                     row["Y"],
#                     linestyle='-',  # Connect with lines
#                     marker='o',
#                     markersize=6,
#                     markerfacecolor='none',
#                     markeredgecolor=color,
#                     color=color,
#                     #label=f"Numerical - {key} (Time: {t:.2e})"  # Label for legend
#                 )

#         # Customize the plot for clarity
#         plt.xlabel("Normalized Pore Pressure, $p/p_0$ (-)")  # X-axis label
#         plt.ylabel("Depth, $Y$ (m)")  # Y-axis label
#         plt.title(f"Depth vs. Normalized Pore Pressure - {dir_key}")  # Plot title
#         plt.grid(True)  # Add gridlines

#         # Add the legend for clarity
#         #plt.legend()

#         # Show the plot for this directory
#         plt.show()



def plot_analytical_numerical_solutions(par_dataframes_by_directory, u_z, DepthArray, NondimensionalTime, TractionLoad):
    if TractionLoad == 0:
        raise ValueError("TractionLoad must not be zero.")

    if not par_dataframes_by_directory:
        raise ValueError("The provided 'par_dataframes_by_directory' is empty.")

    # Define line styles, markers, and colors for variety
    line_styles = ["-", "--", ":", "-."]
    markers = ["o", "s", "^", "d"]
    colors = ["r", "g", "b", "y", "m", "c"]

    for dir_key, dataframes in par_dataframes_by_directory.items():
        plt.figure(figsize=(10, 6))  # Set the plot size

        # Plot the Analytical Solution
        for kk in range(len(NondimensionalTime)):
            style = line_styles[kk % len(line_styles)]
            marker = markers[kk % len(line_styles)]

            plt.plot(
                u_z[:, kk],
                DepthArray,
                color='black', 
                linestyle=style,
                marker=marker,
                markersize=4,
                markerfacecolor='none',
            )

        # Plot Data from the Current Directory
        required_columns = ["Time", "WPressure", "Y"]
        for key, df in dataframes.items():
            if not all(col in df.columns for col in required_columns):
                raise KeyError(f"Missing required columns in DataFrame '{key}'")

            for j, t in enumerate(NondimensionalTime):
                color = colors[j % len(colors)]

                closest_index = np.argmin(np.abs(df["Time"] - t))

                # Ensure the closest index is within bounds
                if closest_index >= len(df):
                    raise IndexError(f"Closest index '{closest_index}' is out of bounds.")

                row = df.iloc[closest_index]

                plt.plot(
                    row["WPressure"]/ TractionLoad,
                    row["Y"],
                    linestyle='-', 
                    marker='o',
                    markersize=6,
                    markerfacecolor='none',
                    markeredgecolor=color,
                    color=color,
                )

        # Customize the plot for clarity
        plt.xlabel("Normalized Pore Pressure, $p/p_0$ (-)")
        plt.ylabel("Depth, $Y$ (m)")
        plt.title(f"Depth vs. Normalized Pore Pressure - {dir_key}")
        plt.grid(True)

        # Add the legend if needed
        # plt.legend()

        plt.show()




def get_par_variables(directory, par_number, variables):
    """
    Retrieve specified variables from a given directory and PAR file number.

    Parameters:
    - directory: The base directory where the PAR files are stored.
    - par_number: The PAR file number to search for.
    - variables: A list of variable names to return (e.g., ["Uy", "Time"]).

    Returns:
    - A dictionary with the specified variables, or an error message if the file/variables don't exist.
    """

    # Check if the directory exists
    if not os.path.exists(directory):
        return {"error": f"The directory '{directory}' does not exist."}

    # Create the pattern to find the correct PAR file based on the given number
    file_pattern = f"{directory}/*PAR_{str(par_number).zfill(3)}"
    matching_files = glob.glob(file_pattern)

    if not matching_files:
        return {"error": f"No PAR file found with the number '{par_number}' in '{directory}'."}

    # Read the first matching file
    file_path = matching_files[0]
    df = pd.read_csv(file_path, delim_whitespace=True)

    # Check if the specified variables exist in the DataFrame
    missing_vars = [var for var in variables if var not in df.columns]

    if missing_vars:
        return {"error": f"Missing variables in the PAR file: {', '.join(missing_vars)}"}

    # Return a dictionary with the specified variables
    result = {var: df[var] for var in variables}

    return result


# Function to extract specified variables from `par_dataframes_by_directory`
def extract_variables_from_par_dataframes(par_dataframes_by_directory, directory_key, par_number, variable_names=[]):
    """
    Extract specified variables from a given directory and PAR number in `par_dataframes_by_directory`.

    Parameters:
    - par_dataframes_by_directory: A dictionary containing DataFrames for each directory and PAR file.
    - directory_key: The key identifying the desired directory.
    - par_number: The PAR file number to search for.
    - variable_names: A list of variable names to extract (e.g., ["Uy", "Ux", "Time"]).

    Returns:
    - A dictionary with the specified variables, or an error message if the file/variables don't exist.
    """

    # Check if the specified directory exists in the dictionary
    if directory_key not in par_dataframes_by_directory:
        return {"error": f"Directory '{directory_key}' not found."}

    # Get the sub-dictionary for the specified directory
    directory_data = par_dataframes_by_directory[directory_key]

    # Construct the PAR key
    par_key = f"PAR_{str(par_number).zfill(3)}"  # Zero-padded PAR number

    # Check if the specified PAR key exists in the directory data
    if par_key not in directory_data:
        return {"error": f"PAR file '{par_key}' not found in directory '{directory_key}'."}

    # Get the DataFrame for the specified PAR number
    df = directory_data[par_key]

    # Check if the required variables exist in the DataFrame
    missing_vars = [var for var in variable_names if var not in df.columns]
    
    if missing_vars:
        return {"error": f"Missing variables in the DataFrame: {', '.join(missing_vars)}"}

    # Extract the specified variables into a dictionary
    extracted_vars = {var: df[var].values for var in variable_names}

    return extracted_vars  # Return the dictionary with the specified variables