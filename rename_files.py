import os

def rename_files(directory, prefix):
    """
    Renames all files in the specified directory by adding a prefix.

    :param directory: The path to the directory containing files to rename.
    :param prefix: The prefix to add to each file name.
    """
    try:
        # List all files in the directory
        files = os.listdir(directory)
        
        for filename in files:
            # Construct the old and new file names
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, f"{prefix}_{filename}")
            
            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed: {old_file} to {new_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
#directory_path = '/path/to/your/directory'
directory_path = 'C:/test'
prefix = 'new'
rename_files(directory_path, prefix)
