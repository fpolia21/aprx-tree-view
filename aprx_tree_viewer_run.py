print(f"> Loading aprx_tree-view from command prompt..")
print(f"> Loading ArcPY libraries..")
import arcpy
import os
from datetime import datetime
import sys

def run_toolbox(toolbox_path, aprx_path):
    try:
        # Check if the toolbox and aprx paths exist
        if not os.path.exists(toolbox_path):
            raise FileNotFoundError(f"Toolbox file not found: {toolbox_path}")
        
        if not os.path.exists(aprx_path):
            raise FileNotFoundError(f"APR file not found: {aprx_path}")

        # Import the toolbox
        arcpy.ImportToolbox(toolbox_path)
        
        # Assuming the toolbox contains a tool named "TreeViewer" that takes the APRX path as a parameter
        # Replace "TreeViewer" with the actual tool name inside your toolbox.
        result = arcpy.AprxTreeView(aprx_path)
        
        # Print the result messages
        arcpy.AddMessage("Tool executed successfully.")
        print(result)
    except Exception as e:
        print(f"> An error occurred: {e} [run tool]")

# Example usage
if __name__ == "__main__":
    # Ensure at least one argument (the APRX path) is provided
    if len(sys.argv) < 2:
        print("Usage: python aprx_tree_viewer_run.py <path_to_aprx>")
        sys.exit(1)

    # get the latest .pyt
    current_directory = os.path.dirname(os.path.abspath(__file__))
    pyt_files = []
    for root, dirs, files in os.walk(current_directory):
        for file in files:
            if file.startswith('aprx-tree-viewer') and file.endswith('.pyt'):
                file_path = os.path.join(root, file)
                last_modified_time = os.path.getmtime(file_path)
                pyt_files.append((file_path, last_modified_time))
        # Output the results
    if pyt_files:
        # Find the most recent file by last modified time
        latest_file = max(pyt_files, key=lambda item: item[1])
        latest_file_path, latest_file_time = latest_file

        # Convert the timestamp to a readable format
        readable_time = datetime.fromtimestamp(latest_file_time).strftime('%Y-%m-%d %H:%M:%S')

        # Print the most recent .pyt file
        # print(f"The latest .pyt file is: {latest_file_path}")
        # print(f"Last modified on: {readable_time}")
    else:
        print("> No matching .pyt files found in the current directory. \n> Please download the latest .pyt and copy it next to the aprx_tree_viewer_run.py\n> end.")
        exit (1)

    toolbox_path = latest_file_path  # Replace with actual path if needed
    aprx_path = sys.argv[1]  # Get the APRX path from the command-line argument
    print(f"> Opening {aprx_path}..")
    run_toolbox(toolbox_path, aprx_path)
